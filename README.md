# CryptoFragments

CryptoFragments is a Python-based tool that securely fragments, encrypts, and manages seed phrases using Shamir's Secret Sharing scheme. This project allows you to split a sensitive seed phrase into multiple shares, encrypt and store them safely, and recover the original seed phrase with a threshold number of shares.

---

## Features

- **Seed Phrase Fragmentation**: Securely split a seed phrase into multiple shares using Shamir's Secret Sharing.
- **Threshold Recovery**: Recover the original seed phrase with a minimum threshold of shares.
- **Encryption**: Encrypt each share using AES encryption for enhanced security.
- **Automatic File Management**: Automatically detect and manage share and key files.
- **Dynamic Threshold Detection**: Extract the required threshold dynamically from the share metadata.
- **Error Handling**: Comprehensive handling of file, decryption, and recovery errors.

---

## How It Works

1. **Fragmentation**:
   - The seed phrase is split into `n` shares, and only a `threshold` number of shares are required to recover it.

2. **Encryption**:
   - Each share is encrypted with a unique key to ensure secure storage.

3. **File Management**:
   - Encrypted shares and their keys are saved as files (`share_*.enc` and `key_*.key`).

4. **Recovery**:
   - The original seed phrase is recovered using a minimum threshold of decrypted shares.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment (optional, but recommended)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Chr1570ph3/CryptoFragments.git
   cd CryptoFragments
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage
### Fragment and Encrypt a Seed Phrase
Run the `basic_usage.py` script to fragment and encrypt a seed phrase:
```bash
python examples/basic_usage.py
```

This will:
- Split your seed phrase into shares.
- Encrypt each share and save it as `share_*.enc`.
- Save the corresponding encryption keys as `key_*.key`.

## Recover a Seed Phrase
Run the `recovery_test.py` script to recover a seed phrase:
```bash
python examples/recovery_test.py
```

This will:

- Automatically detect the available `share_*.enc` and `key_*.key` files.
- Decrypt and process up to the required threshold of shares.
- Recover the original seed phrase.

---
## File Structure
```bash
CryptoFragments/
├── src/
│   ├── share.py            # Implements Shamir's Secret Sharing
│   ├── encrypt.py          # Handles encryption and decryption
│   ├── utils.py            # File I/O utilities
├── examples/
│   ├── basic_usage.py      # Example: Fragmentation and encryption
│   ├── advanced_usage.py   # Example: Full workflow
│   ├── recovery_test.py    # Example: Recovery from shares
├── tests/
│   ├── test_share.py       # Unit tests for share.py
│   ├── test_encrypt.py     # Unit tests for encrypt.py
│   ├── test_utils.py       # Unit tests for utils.py
├── docs/
│   ├── en/
│   │   ├── architecture.md # Technical architecture (English)
│   │   ├── overview.md     # Project overview (English)
│   │   ├── security.md     # Security practices (English)
│   ├── fr/
│   │   ├── securite.md     # Security practices (French)
│   │   ├── vue_generale.md # Project overview (French)
├── .gitignore
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (en)
├── README.md               # Project documentation (fr)
```

---
## Best Practices
1. Run Offline: Always run the program on an offline, secure computer to minimize exposure.
1. Secure Storage: Store share_*.enc and key_*.key files in separate, secure locations.
1. Redundant Backups: Maintain multiple backups of your shares and keys.
1. Threshold Awareness: Ensure you always have the minimum number of shares (threshold) required for recovery.
1. Test Recovery: Regularly test the recovery process with dummy data to ensure everything works as expected.

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
1. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
1. Commit your changes:
    ```bash
    git commit -m "Add your message here"
    ```
1. Push your branch and create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Contact
For questions or feedback, please contact:

GitHub: [Chr1570ph3](https://github.com/Chr1570ph3/)

