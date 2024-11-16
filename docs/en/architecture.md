# Technical Architecture of the Project

## Overview

The project is organized into modules, ensuring a clear separation of responsibilities:
- **Sharing and recovery**: Handles splitting and recovering the seed phrase using Shamir's Secret Sharing.
- **Encryption and decryption**: Secures the generated shares using symmetric encryption.
- **Utilities**: Functions for file management.

## Main Modules

### 1. `main.py`
- Entry point of the program.
- Orchestrates key steps: sharing, encryption, storage, and recovery.

### 2. `share.py`
- Implements secret sharing and reconstruction using `shamir-mnemonic`.
- Key functions:
  - `create_shares(seed_phrase, total_shares, threshold)`
  - `recover_secret(shares)`

### 3. `encrypt.py`
- Handles encryption of shares using `cryptography`.
- Key functions:
  - `encrypt_share(share)`

### 4. `decrypt.py`
- Handles decryption of shares using `cryptography`.
- Key functions:
  - `decrypt_share(encrypted_share, key)`


### 5. `utils.py`
- Manages file storage for encrypted data.
- Key functions:
  - `save_to_file(filename, data)`
  - `load_from_file(filename)`
  - `export_to_qrcode`
  - `decode_qrcode`

## Program Flow

1. **Share Generation**:
   - The seed phrase is split into shares with a recovery threshold.
2. **Encryption**:
   - Each share is encrypted with a unique key.
3. **Storage**:
   - Encrypted shares and keys are stored in files.
4. **Recovery**:
   - Files are decrypted, and shares are combined to reconstruct the seed phrase.

## Libraries Used

- `shamir-mnemonic`: Implements Shamir's Secret Sharing.
- `cryptography`: Provides symmetric encryption and decryption.
- `unittest`: Unit testing for core functions.
- `pillow` : Used to open and handle QR code image files for decoding. 
- `pyzbar` : Used to extract encoded data from QR code images.
- `qrcode` : Used to create QR code images that store encrypted shares and keys.