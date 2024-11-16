import unittest
import os
from src.utils import save_to_file, load_from_file

class TestUtilsFunctions(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_file.txt"
        self.test_data = b"test data"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_and_load_file(self):
        save_to_file(self.test_filename, self.test_data)
        loaded_data = load_from_file(self.test_filename)
        self.assertEqual(self.test_data, loaded_data)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_from_file("nonexistent_file.txt")

if __name__ == "__main__":
    unittest.main()
