# CryptoFragments

CryptoFragments est un outil basé sur Python qui permet de fragmenter, chiffrer et gérer en toute sécurité des phrases de récupération (seed phrases) en utilisant le schéma de partage secret de Shamir (Shamir's Secret Sharing). Ce projet permet de diviser une phrase sensible en plusieurs parts, de les chiffrer et de les stocker en toute sécurité, puis de reconstituer la phrase d'origine à l'aide d'un nombre minimal de parts.


---

## Fonctionnalités

- **Fragmentation des Phrases de Récupération** : Divisez une phrase en plusieurs parts de manière sécurisée grâce au schéma de partage secret de Shamir.
- **Récupération à Seuil** : Reconstituez la phrase d'origine avec un nombre minimal (seuil) de parts.
- **Chiffrement** : Chiffrez chaque part avec AES pour une sécurité renforcée.
- **Gestion Automatique des Fichiers** : Détectez et gérez automatiquement les fichiers de parts et de clés.
- **Détection Dynamique du Seuil** : Extrayez le seuil requis dynamiquement à partir des métadonnées des parts.
- **Gestion des Erreurs** : Une gestion complète des erreurs liées aux fichiers, au déchiffrement et à la récupération.

---

## Comment ça fonctionne

1. **Fragmentation** :
   - La phrase de récupération est divisée en `n` parts, et un nombre minimal (`seuil`) de parts est requis pour la reconstituer.

2. **Chiffrement** :
   - Chaque part est chiffrée avec une clé unique pour garantir un stockage sécurisé.

3. **Gestion des Fichiers** :
   - Les parts chiffrées et leurs clés sont sauvegardées sous forme de fichiers (`share_*.enc` et `key_*.key`).

4. **Récupération** :
   - La phrase de récupération originale est reconstituée à l'aide d'un nombre minimal de parts déchiffrées.

---

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Environnement virtuel (optionnel, mais recommandé)

### Étapes d'installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Chr1570ph3/CryptoFragments.git
   cd CryptoFragments
    ```

1. Créez et activez un environnement virtuel :

    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows: env\Scripts\activate
    ```

1. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

---

## Utilisation
### Fragmenter et Chiffrer une Phrase de Récupération
Exécutez le script `basic_usage.py` pour fragmenter et chiffrer une phrase de récupération :

```bash
python examples/basic_usage.py
```

Cela permettra de :

- Diviser votre phrase en plusieurs parts.
- Chiffrer chaque part et les sauvegarder sous forme de fichiers `share_*.enc`.
- Sauvegarder les clés de chiffrement correspondantes sous forme de fichiers `key_*.key`.

## Reconstituer une Phrase de Récupération
Exécutez le script `recovery_test.py` pour reconstituer une phrase de récupération :
```bash
python examples/recovery_test.py
```

Cela permettra de :

- Détecter automatiquement les fichiers disponibles (`share_*.enc` et `key_*.key`).
- Déchiffrer et traiter jusqu'à atteindre le seuil requis de parts.
- Reconstituer la phrase de récupération originale.

---
## Structure des Fichiers

```bash
CryptoFragments/
├── src/
│   ├── share.py            # Implémente le schéma de partage secret de Shamir
│   ├── encrypt.py          # Gère le chiffrement et le déchiffrement
│   ├── utils.py            # Utilitaires pour la gestion des fichiers
├── examples/
│   ├── basic_usage.py      # Exemple : Fragmentation et chiffrement
│   ├── advanced_usage.py   # Exemple : Flux de travail complet
│   ├── recovery_test.py    # Exemple : Récupération à partir des parts
├── tests/
│   ├── test_share.py       # Tests unitaires pour share.py
│   ├── test_encrypt.py     # Tests unitaires pour encrypt.py
│   ├── test_utils.py       # Tests unitaires pour utils.py
├── docs/
│   ├── en/
│   │   ├── architecture.md # Architecture technique (en anglais)
│   │   ├── overview.md     # Vue générale du projet (en anglais)
│   │   ├── security.md     # Pratiques de sécurité (en anglais)
│   ├── fr/
│   │   ├── securite.md     # Pratiques de sécurité (en français)
│   │   ├── vue_generale.md # Vue générale du projet (en français)
├── .gitignore
├── requirements.txt        # Dépendances Python
├── README.md               # Documentation du projet (en)
├── README_fr.md            # Documentation du projet (fr)
```

---
## Bonnes Pratiques
1. Exécutez Hors Ligne : Exécutez toujours le programme sur un ordinateur hors ligne et sécurisé pour minimiser les risques.
1. Stockage Sécurisé : Stockez les fichiers `share_*.enc` et `key_*.key` dans des emplacements séparés et sécurisés.
1. Sauvegardes Redondantes : Conservez plusieurs sauvegardes de vos parts et de vos clés.
1. Conscience du Seuil : Assurez-vous de toujours avoir le nombre minimal de parts requis (`seuil`) pour la récupération.
1. Testez la Récupération : Testez régulièrement le processus de récupération avec des données fictives pour garantir que tout fonctionne comme prévu.

## Contribution
Les contributions sont les bienvenues ! Suivez ces étapes pour contribuer :

1. Forkez le dépôt.
1. Créez une nouvelle branche :
    ```bash
    git checkout -b feature-name
    ```
1. Commitez vos modifications :
    ```bash
    git commit -m "Ajoutez votre message ici"
    ```
1. Poussez votre branche et créez une pull request.

## License
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](https://opensource.org/licenses/MIT) pour plus de détails.
*

## Contact
Pour toute question ou retour, veuillez contacter :
GitHub: [Chr1570ph3](https://github.com/Chr1570ph3/)

