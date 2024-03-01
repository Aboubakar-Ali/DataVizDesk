import unittest
import sys
sys.path.insert(0, 'c:/D/Projet/School/DataVizDesk/Data_Exploration')
from viz import analyse_distribution_paragraphes

class TestViz(unittest.TestCase):
    def test_analyse_distribution_paragraphes(self):
        filepath = 'Data_Exploration/livre.txt'
        
        # test the function
        result = analyse_distribution_paragraphes(filepath)
        
        # assertions
        self.assertIn((0, 16), result)
        self.assertIn((10, 567), result)
        self.assertIn((20, 33), result)


if __name__ == '__main__':
    unittest.main()
