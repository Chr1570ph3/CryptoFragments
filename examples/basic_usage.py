import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.share import create_shares
from src.encrypt import encrypt_share
from src.utils import save_to_file

# Parameters
seed_phrase = "emotion parent journey army family grocery height pond biology skin hamster bonus grass quote crisp little blast food install flight index muffin fade pelican"
total_shares = 5
threshold = 3

# Step 1: Generate shares
shares = create_shares(seed_phrase, total_shares, threshold)
print(f"Shares generated: {shares}")

# Step 2: Encrypt and save the shares
for i, share in enumerate(shares):
    encrypted_share, key = encrypt_share(share.encode('utf-8'))
    save_to_file(f"share_{i + 1}.enc", encrypted_share)  # Save encrypted share
    save_to_file(f"key_{i + 1}.key", key)  # Save encryption key
    print(f"Share {i + 1} encrypted and saved.")
