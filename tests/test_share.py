import unittest
from src.share import create_shares, recover_secret

class TestShareFunctions(unittest.TestCase):
    def test_create_shares(self):
        seed_phrase = "test seed phrase"
        total_shares = 5
        threshold = 3

        shares = create_shares(seed_phrase, total_shares, threshold)
        self.assertEqual(len(shares), total_shares)
        self.assertIsInstance(shares, list)

    def test_recover_secret(self):
        seed_phrase = "test seed phrase"
        total_shares = 5
        threshold = 3

        shares = create_shares(seed_phrase, total_shares, threshold)
        recovered_seed = recover_secret(shares[:threshold])

        # Décodage de bytes en chaîne si nécessaire
        if isinstance(recovered_seed, bytes):
            recovered_seed = recovered_seed.decode('utf-8')

        self.assertEqual(seed_phrase, recovered_seed)

    def test_recover_secret_insufficient_shares(self):
        seed_phrase = "test seed phrase"
        total_shares = 5
        threshold = 3

        shares = create_shares(seed_phrase, total_shares, threshold)
        with self.assertRaises(Exception):
            recover_secret(shares[:threshold - 1])  # Moins que le seuil

if __name__ == "__main__":
    unittest.main()
