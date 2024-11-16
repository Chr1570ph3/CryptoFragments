from cryptography.fernet import Fernet

def decrypt_share(encrypted_share, key):
    """Déchiffre une part."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_share)
