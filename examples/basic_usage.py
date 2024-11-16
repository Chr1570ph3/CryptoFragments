import sys
import os
import argparse

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.share import create_shares
from src.encrypt import encrypt_share
from src.utils import save_to_file, export_to_qrcode

# Paramètres pour la fragmentation de la seed phrase
SEED_PHRASE = "your seed phrase here"  # Remplacez par votre seed ou chargez depuis un fichier
TOTAL_SHARES = 5
THRESHOLD = 3
OUTPUT_DIR = "output"

def main():
    # Argument parser pour la ligne de commande
    parser = argparse.ArgumentParser(description="CryptoFragments: Fragment and secure your seed phrase.")
    parser.add_argument("--seed", help="Seed phrase to process (as a parameter).", required=False)
    parser.add_argument("--seed-file", help="Path to a .txt file containing the seed phrase.", required=False)
    parser.add_argument("--output-dir", help="Directory to save shares, keys, and QR codes.", default="output")
    parser.add_argument("--export-qrcode", help="Export shares and keys as QR codes.", action="store_true")
    parser.add_argument("--total-shares", help="Number of shares to create.", type=int, default=5)
    parser.add_argument("--threshold", help="Number of shares required to recover the seed phrase.", type=int, default=3)

    args = parser.parse_args()

    # Charger la seed phrase
    if args.seed:
        seed_phrase = args.seed
    elif args.seed_file:
        with open(args.seed_file, "r") as f:
            seed_phrase = f.read().strip()
    else:
        print("Error: You must provide a seed phrase either as a parameter or via a .txt file.")
        return

    # Valider les paramètres
    if args.threshold > args.total_shares:
        print("Error: Threshold cannot be greater than the total number of shares.")
        return

    # Créer le dossier de sortie si nécessaire
    os.makedirs(args.output_dir, exist_ok=True)

    # Fragmentation de la seed phrase
    shares = create_shares(seed_phrase, args.total_shares, args.threshold)

    # Encryptez et sauvegardez chaque part
    for i, share in enumerate(shares):
        encrypted_share, key = encrypt_share(share.encode('utf-8'))

        # Sauvegarder les fichiers chiffrés et les clés
        share_filename = f"share_{i + 1}.enc"
        key_filename = f"key_{i + 1}.key"

        # Exporter les QR codes si l'option est activée
        if args.export_qrcode:
            export_to_qrcode(encrypted_share.decode('latin-1'), f"share_{i + 1}.png", args.output_dir)
            export_to_qrcode(key.decode('latin-1'), f"key_{i + 1}.png", args.output_dir)
            print(f"QR Code for Share {i + 1} and Key exported.")
        else:
            save_to_file(os.path.join(args.output_dir, share_filename), encrypted_share)
            save_to_file(os.path.join(args.output_dir, key_filename), key)
            print(f"Encrypted Share {i + 1} and Key saved.")


    print(f"Process completed successfully. Output saved in: {args.output_dir}")


if __name__ == "__main__":
    main()