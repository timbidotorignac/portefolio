"""log_bruteforce_detector.py

Mini‑outil défensif : analyser un fichier de logs et compter des rafales
d'échecs d'authentification (ex : SSH) afin d'identifier des comportements
suspects.

Ce script n'exécute aucune action offensive.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter


PATTERN = re.compile(r"Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Détection simple de rafales d'échecs (logs)")
    parser.add_argument("logfile", help="Chemin vers le fichier de logs (ex : /var/log/auth.log)")
    parser.add_argument("--top", type=int, default=10, help="Nombre d'IP à afficher")
    args = parser.parse_args()

    counts: Counter[str] = Counter()

    with open(args.logfile, "r", errors="ignore") as f:
        for line in f:
            m = PATTERN.search(line)
            if m:
                counts[m.group("ip")] += 1

    for ip, n in counts.most_common(args.top):
        print(f"{ip}\t{n}")


if __name__ == "__main__":
    main()
