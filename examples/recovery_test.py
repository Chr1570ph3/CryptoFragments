import sys
import os
import argparse


# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.share import recover_secret
from src.utils import load_from_file, decode_qrcode
from src.decrypt import decrypt_share

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Recover seed phrase from shares and keys.")
    parser.add_argument("--directory", help="Directory where the shares and keys are stored", required=True)
    parser.add_argument("--threshold", help="Minimum number of shares required to recover the seed phrase", type=int, required=False, default=3)
    args = parser.parse_args()

    # Directory where the shares and keys are stored
    SHARES_DIRECTORY = args.directory

    # Automatically detect available shares and keys (including QR codes)
    share_files = sorted([f for f in os.listdir(SHARES_DIRECTORY) if f.startswith("share_") and (f.endswith(".enc") or f.endswith(".png"))])
    key_files = sorted([f for f in os.listdir(SHARES_DIRECTORY) if f.startswith("key_") and (f.endswith(".key") or f.endswith(".png"))])

    # Debugging: Print detected files
    print(f"Detected share files: {share_files}")
    print(f"Detected key files: {key_files}")

    # Match shares with corresponding keys
    available_indices = []

    for share_file in share_files:
        index = share_file.split("_")[1].split(".")[0]  # Extract the index from the filename
        key_file = f"key_{index}.key" if share_file.endswith(".enc") else f"key_{index}.png"
        if key_file in key_files:  # Check if the key file exists
            available_indices.append(int(index))

    # Debugging: Print matched indices
    print(f"Matched indices: {available_indices}")

    recovered_shares = []

    # Process available shares
    for index in available_indices:
        try:
            # Load encrypted share (from files or QR codes)
            share_path = os.path.join(SHARES_DIRECTORY, f"share_{index}.enc") if f"share_{index}.enc" in share_files else os.path.join(SHARES_DIRECTORY, f"share_{index}.png")
            print(f"Processing share file: {share_path}")

            if share_path.endswith(".enc"):
                encrypted_share = load_from_file(share_path)
            elif share_path.endswith(".png"):
                encrypted_share = decode_qrcode(share_path)
            else:
                print(f"Warning: Share file for index {index} not found. Skipping this share.")
                continue

            # Load key (from files or QR codes)
            key_path = os.path.join(SHARES_DIRECTORY, f"key_{index}.key") if f"key_{index}.key" in key_files else os.path.join(SHARES_DIRECTORY, f"key_{index}.png")
            print(f"Processing key file: {key_path}")

            if key_path.endswith(".key"):
                key = load_from_file(key_path)
            elif key_path.endswith(".png"):
                key = decode_qrcode(key_path)
            else:
                print(f"Warning: Key file for index {index} not found. Skipping this share.")
                continue

            # Decrypt the share
            decrypted_share = decrypt_share(encrypted_share, key).decode('utf-8')
            recovered_shares.append(decrypted_share)

        except FileNotFoundError as e:
            print(f"Error: File not found - {e.filename}. Skipping this share.")
        except ValueError as e:
            print(f"Error: Failed to decode QR code or read file for index {index}. Details: {e}. Skipping this share.")
        except Exception as e:
            print(f"Error: Failed to process share {index}. Details: {e}. Skipping this share.")

    # Check if there are enough shares for recovery
    if not recovered_shares:
        print("Error: No valid shares were recovered. Ensure the required files are available and readable.")
    elif len(recovered_shares) < args.threshold:
        print(f"Error: Not enough valid shares to recover the seed phrase. {len(recovered_shares)} shares found, at least {args.threshold} required.")
    else:
        # Attempt to recover the seed phrase
        try:
            recovered_seed = recover_secret(recovered_shares)
            print(f"Successfully Recovered Seed Phrase: {recovered_seed}")
        except Exception as e:
            print(f"Error: Failed to recover seed phrase. Details: {e}")

if __name__ == "__main__":
    main()