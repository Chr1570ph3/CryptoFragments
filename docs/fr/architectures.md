# Architecture Technique du Projet
## Vue d'ensemble
Le projet est organisé en modules pour assurer une séparation claire des responsabilités :

- Partage et récupération : Gère la division et la récupération de la phrase secrète à l'aide du schéma de Shamir.
- Chiffrement et déchiffrement : Sécurise les parts générées en utilisant le chiffrement symétrique.
- Utilitaires : Fournit des fonctions pour la gestion des fichiers et des QR codes.

## Modules Principaux
1. `main.py`
    - Point d'entrée principal du programme.
    - Coordonne les étapes clés : partage, chiffrement, stockage et récupération.

1. `share.py`
    - Implémente le partage secret et la reconstruction à l'aide de `shamir-mnemonic`.
    - Fonctions principales :
        - `create_shares(seed_phrase, total_shares, threshold)`
        - `recover_secret(shares)`

1. `encrypt.py`
    - Gère le chiffrement des parts à l'aide de `cryptography`.
    - Fonctions principales :
        - `encrypt_share(share)`

1. `decrypt.py`
    - Gère le déchiffrement des parts à l'aide de `cryptography`.
    - Fonctions principales :
        - `decrypt_share(encrypted_share, key)`

1. `utils.py`
    - Gère le stockage des données chiffrées et la gestion des QR codes.
    - Fonctions principales :
        - `save_to_file(filename, data)`
        - `load_from_file(filename)`
        - `export_to_qrcode`
        - `decode_qrcode`


## Flux du Programme

1. *Génération des Parts* :
    - La phrase secrète est divisée en plusieurs parts avec un seuil de récupération.

1. *Chiffrement* :
    - Chaque part est chiffrée avec une clé unique.
1. *Stockage* :
    - Les parts chiffrées et les clés sont stockées dans des fichiers ou exportées en QR codes.
1. *Récupération* :
    - Les fichiers ou QR codes sont déchiffrés, et les parts sont combinées pour reconstruire la phrase secrète.

## Bibliothèques Utilisées

- `shamir-mnemonic` : Implémente le schéma de partage secret de Shamir.
- `cryptography` : Fournit les fonctions de chiffrement et de déchiffrement symétrique.
- `unittest` : Permet les tests unitaires des fonctions principales.
- `pillow` : Gère l'ouverture et le traitement des fichiers d'image QR code pour le décodage.
- `pyzbar` : Extrait les données encodées des images QR code.
- `qrcode` : Crée des images QR code pour stocker les parts et les clés chiffrées.