import os
import argparse
from src.share import create_shares
from src.encrypt import encrypt_share
from src.utils import save_to_file, export_to_qrcode  

def main():
    parser = argparse.ArgumentParser(description="CryptoFragments: Fragment and secure your seed phrase.")
    parser.add_argument("--seed", help="Seed phrase to process (as a parameter).", required=False)
    parser.add_argument("--seed-file", help="Path to a .txt file containing the seed phrase.", required=False)
    parser.add_argument("--output-dir", help="Directory to save shares, keys, and QR codes.", default="output")
    parser.add_argument("--export-qrcode", help="Export shares and keys as QR codes.", action="store_true")

    args = parser.parse_args()

    # Load the seed phrase
    if args.seed:
        seed_phrase = args.seed
    elif args.seed_file:
        with open(args.seed_file, "r") as f:
            seed_phrase = f.read().strip()
    else:
        print("Error: You must provide a seed phrase either as a parameter or via a .txt file.")
        return

    # Parameters for Shamir's Secret Sharing
    total_shares = 5
    threshold = 3

    # Create shares
    shares = create_shares(seed_phrase, total_shares, threshold)

    # Output directory
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    # Encrypt and save each share
    for i, share in enumerate(shares):
        encrypted_share, key = encrypt_share(share.encode('utf-8'))
        
        # Save encrypted share and key to files
        share_filename = f"share_{i + 1}.enc"
        key_filename = f"key_{i + 1}.key"
        save_to_file(os.path.join(output_dir, share_filename), encrypted_share)
        save_to_file(os.path.join(output_dir, key_filename), key)
        print(f"Encrypted Share {i + 1} and Key saved.")

        # Export QR codes if the option is enabled
        if args.export_qrcode:
            export_to_qrcode(encrypted_share.decode('latin-1'), f"share_{i + 1}.png", output_dir)
            export_to_qrcode(key.decode('latin-1'), f"key_{i + 1}.png", output_dir)

    print("Process completed successfully.")

if __name__ == "__main__":
    main()