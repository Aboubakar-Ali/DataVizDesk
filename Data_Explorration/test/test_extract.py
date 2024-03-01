import unittest
import sys
sys.path.insert(0, 'c:/D/Projet/School/DataVizDesk/Data_Explorration')
from extract import extract_metadata_and_first_chapter



class TestExtract(unittest.TestCase):
    def test_extract_metadata_and_first_chapter(self):
        filepath = 'Data_Explorration/livre.txt'
        title, author, first_chapter = extract_metadata_and_first_chapter(filepath)
        
        # VVérification
        self.assertEqual(title, 'A history of the Peninsular War, Vol. 6')
        self.assertEqual(author, 'Charles Oman')
        
        self.assertTrue('WELLINGTON IN THE NORTH: BURGOS INVESTE' in first_chapter)

if __name__ == '__main__':
    unittest.main()
