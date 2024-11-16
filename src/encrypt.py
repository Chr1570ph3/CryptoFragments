from cryptography.fernet import Fernet

def encrypt_share(share):
    """Chiffre une part."""
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_share = fernet.encrypt(share)
    return encrypted_share, key