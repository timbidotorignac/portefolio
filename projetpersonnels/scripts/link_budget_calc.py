"""link_budget_calc.py

Calculateur de budget de liaison (version simplifiée).

But : documenter rapidement un lien (pertes / gains / marge) lors d'un TP.
"""


def link_budget(
    ptx_dbm: float,
    gain_db: float,
    loss_db: float,
    rx_sens_dbm: float,
) -> tuple[float, float]:
    """Retourne (Prx_dBm, marge_dB)."""
    prx_dbm = ptx_dbm + gain_db - loss_db
    margin_db = prx_dbm - rx_sens_dbm
    return prx_dbm, margin_db


def main() -> None:
    # Exemple de valeurs (à adapter)
    ptx_dbm = 0.0
    gain_db = 6.0
    loss_db = 12.0
    rx_sens_dbm = -80.0

    prx_dbm, margin_db = link_budget(ptx_dbm, gain_db, loss_db, rx_sens_dbm)
    print(f"Prx(dBm) = {prx_dbm:.2f}")
    print(f"Marge(dB) = {margin_db:.2f}")


if __name__ == "__main__":
    main()
