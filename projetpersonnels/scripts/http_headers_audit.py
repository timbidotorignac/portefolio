"""http_headers_audit.py

Mini‑outil d'inventaire d'entêtes HTTP de sécurité.

Usage prévu : environnements de test / sites dont vous avez l'autorisation.
"""

from __future__ import annotations

import argparse
from urllib.request import Request, urlopen


SEC_HEADERS = [
    "strict-transport-security",
    "content-security-policy",
    "x-frame-options",
    "x-content-type-options",
    "referrer-policy",
    "permissions-policy",
]


def audit_url(url: str, timeout: int = 10) -> tuple[list[str], dict[str, str]]:
    req = Request(url, method="HEAD")
    with urlopen(req, timeout=timeout) as r:
        headers = {k.lower(): v for k, v in r.headers.items()}
    missing = [h for h in SEC_HEADERS if h not in headers]
    return missing, headers


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit simple des headers HTTP de sécurité")
    parser.add_argument("urls", nargs="+", help="URL(s) à auditer (ex : https://example.com)")
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    for url in args.urls:
        try:
            missing, _headers = audit_url(url, timeout=args.timeout)
            if missing:
                print(f"{url} -> missing: {', '.join(missing)}")
            else:
                print(f"{url} -> OK (headers présents)")
        except Exception as e:
            print(f"{url} -> erreur: {e}")


if __name__ == "__main__":
    main()
