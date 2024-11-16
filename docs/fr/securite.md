# Meilleures Pratiques de Sécurité

## Objectifs
Garantir la sécurité des seed phrases en combinant le partage de secret et le chiffrement.

## Recommandations Générales

1. **Chiffrement Fort** :
   - Utilisez un chiffrement robuste (AES via `cryptography`).
   - Ne partagez jamais les clés de chiffrement.

2. **Stockage Sécurisé** :
   - Conservez les fichiers dans des emplacements protégés, comme un coffre-fort physique ou un stockage chiffré.
   - Évitez de stocker des fichiers sensibles sur des services cloud non chiffrés.

3. **Multiplication des Lieux** :
   - Stockez les parts dans des emplacements géographiques distincts.
   - Utilisez plusieurs dispositifs sécurisés (clés USB chiffrées, disques durs sécurisés).

4. **Authentification** :
   - Ajoutez une étape d’authentification (mot de passe ou biométrie) pour accéder aux fichiers ou exécuter le programme.

## Bonnes Pratiques Techniques

1. **Exécution Hors Ligne** :
   - Exécutez le programme sur un ordinateur isolé, non connecté à Internet.
   - Cela réduit le risque de compromission par des logiciels malveillants.

2. **Matériel Sécurisé** :
   - Préférez des appareils de confiance, sans logiciels tiers suspects installés.
   - Utilisez des systèmes d'exploitation sécurisés (Linux orienté sécurité, comme Tails).

3. **Mises à Jour** :
   - Maintenez à jour les bibliothèques utilisées (`shamir-mnemonic`, `cryptography`) pour éviter les failles connues.

4. **Supprimez les Données Temporaires** :
   - Nettoyez régulièrement les fichiers temporaires ou inutilisés, en utilisant des outils de suppression sécurisée.

5. **Testez la Récupération** :
   - Avant de déployer le système pour des secrets réels, simulez la récupération avec des données de test pour vérifier la robustesse du processus.

6. **Isolation des Secrets** :
   - Ne mélangez pas les données sensibles avec d'autres fichiers ou dossiers.
   - Créez un environnement dédié pour stocker et gérer les parts.

## Recommandations Spécifiques au Projet

- **Longueur Paire des Secrets** :
  - Assurez-vous que la longueur des seed phrases en bytes est paire avant de les partager.
- **Destruction Sécurisée** :
  - Utilisez des outils comme `shred` ou `srm` pour supprimer définitivement les fichiers sensibles après utilisation.

## Rappel
La sécurité est un processus continu. Réévaluez régulièrement vos pratiques pour garantir la protection de vos données.