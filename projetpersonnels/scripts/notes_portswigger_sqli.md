# Notes — SQL injection (cadre lab)

> Ces notes sont une **synthèse** orientée **remédiation**. Je n'inclus pas de
> payloads ni d'étapes d’exploitation.

## Pourquoi la SQLi existe ?

- Entrées utilisateur injectées dans des requêtes construites par concaténation.
- Gestion d’erreurs trop bavarde.
- Privilèges DB trop larges.

## Contre‑mesures (prioritaires)

- Requêtes **paramétrées** (prepared statements) partout.
- Validation/normalisation côté serveur (format, longueur, whitelists).
- Moindres privilèges côté base de données.
- Gestion d’erreurs sobre (pas de détails SQL en production).
- Journalisation & alertes (détection des anomalies).

## Vérification (approche)

- Tests de non‑régression (cas attendus / cas limites).
- Revue de code : rechercher la concaténation SQL.
- Contrôler les endpoints critiques (auth, recherche, filtres).

## Référence

- PortSwigger Web Security Academy — SQL injection :
  https://portswigger.net/web-security/sql-injection
