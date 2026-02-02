"""sql_prevention_examples.py

Mini‑projet pédagogique (prévention SQL injection).

Objectif : montrer des exemples de requêtes paramétrées (placeholders) et
des garde‑fous côté serveur. Ce fichier n'est pas un outil d'attaque.
"""

import sqlite3


def setup_db(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.executescript(
        """
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE
        );
        INSERT INTO users(username) VALUES ('alice'), ('bob'), ('charlie');
        """
    )
    conn.commit()


def safe_lookup_user_id(conn: sqlite3.Connection, username: str) -> int | None:
    """Exemple SÛR : requête paramétrée (aucune concaténation)."""
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    return row[0] if row else None


def validate_username(username: str) -> str:
    """Validation simple (exemple). À adapter selon vos contraintes."""
    username = username.strip()
    if not (1 <= len(username) <= 32):
        raise ValueError("username : longueur invalide")
    # Exemple : autoriser lettres, chiffres, _ et -
    for ch in username:
        if not (ch.isalnum() or ch in "_-."):
            raise ValueError("username : caractère invalide")
    return username


def main() -> None:
    conn = sqlite3.connect(":memory:")
    setup_db(conn)

    # Exemple d'entrée utilisateur (à valider)
    raw = "alice"
    username = validate_username(raw)
    user_id = safe_lookup_user_id(conn, username)
    print(f"user_id({username}) = {user_id}")

    # Astuce : en production, ajoutez aussi
    # - Moindres privilèges côté DB
    # - Gestion d'erreurs non bavarde
    # - Tests de non-régression


if __name__ == "__main__":
    main()
