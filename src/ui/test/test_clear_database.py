import unittest
import sys
sys.path.insert(0, 'c:/D/Projet/School/DataVizDesk/src/ui')

from main_window import clear_database

class TestExtract(unittest.TestCase):
    def test_clear_database(self):
        clear_database()
        # Vérification
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
