import unittest
from src.encrypt import encrypt_share
from src.decrypt import decrypt_share

class TestEncryptFunctions(unittest.TestCase):
    def test_encrypt_decrypt_share(self):
        share = "test share".encode('utf-8')

        encrypted_share, key = encrypt_share(share)
        self.assertIsInstance(encrypted_share, bytes)
        self.assertIsInstance(key, bytes)

        decrypted_share = decrypt_share(encrypted_share, key)
        self.assertEqual(decrypted_share, share)

    def test_decrypt_with_wrong_key(self):
        share = "test share".encode('utf-8')

        encrypted_share, key = encrypt_share(share)
        _, wrong_key = encrypt_share(share)  # Génère une autre clé

        with self.assertRaises(Exception):
            decrypt_share(encrypted_share, wrong_key)

if __name__ == "__main__":
    unittest.main()
