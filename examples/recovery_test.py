import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.share import recover_secret
from src.utils import load_from_file
from src.decrypt import decrypt_share  # Make sure this is correctly imported

# Directory where the shares and keys are stored
SHARES_DIRECTORY = "."

# Automatically detect available shares and keys
share_files = sorted([f for f in os.listdir(SHARES_DIRECTORY) if f.startswith("share_") and f.endswith(".enc")])
key_files = sorted([f for f in os.listdir(SHARES_DIRECTORY) if f.startswith("key_") and f.endswith(".key")])

# Debugging: Print detected files
print(f"Detected share files: {share_files}")
print(f"Detected key files: {key_files}")

# Match shares with corresponding keys
available_indices = []

for share_file in share_files:
    index = share_file.split("_")[1].split(".")[0]  # Extract the index from the filename
    key_file = f"key_{index}.key"  # Construct the corresponding key filename
    if key_file in key_files:  # Check if the key file exists
        available_indices.append(int(index))

# Debugging: Print matched indices
print(f"Matched indices: {available_indices}")

recovered_shares = []

# Process available shares
for index in available_indices:
    try:
        encrypted_share = load_from_file(f"share_{index}.enc")  # Load encrypted share
        key = load_from_file(f"key_{index}.key")  # Load encryption key
        decrypted_share = decrypt_share(encrypted_share, key).decode('utf-8')  # Decrypt share
        recovered_shares.append(decrypted_share)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}. Skipping this share.")
    except Exception as e:
        print(f"Error: Failed to process share {index}. Details: {e}. Skipping this share.")

# Attempt to recover the seed phrase dynamically
try:
    recovered_seed = recover_secret(recovered_shares)
    print(f"Successfully Recovered Seed Phrase: {recovered_seed}")
except Exception as e:
    if "threshold" in str(e).lower():  # Check if the error mentions the threshold
        print("Error: Not enough valid shares to recover the seed phrase. Ensure sufficient shares are available.")
    else:
        print(f"Error: Failed to recover seed phrase. Details: {e}")


def extract_threshold_from_share(decrypted_share):
    """
    Extracts the threshold value from the decrypted share.

    :param decrypted_share: The decrypted share as a string.
    :return: The threshold value as an integer.
    """
    # Example: If the share contains metadata like "threshold:3|data:..."
    parts = decrypted_share.split("|")
    for part in parts:
        if part.startswith("threshold:"):
            return int(part.split(":")[1])
    raise ValueError("Threshold metadata not found in share.")
