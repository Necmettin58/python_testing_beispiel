import unittest
from programm import plusmal, unterschreiben, kubieren

class TestProgrammFunctions(unittest.TestCase):

    def test_plusmal(self):
        self.assertEqual(plusmal(2, 3), 10)  
        self.assertEqual(plusmal(0, 0), 0)    
        self.assertEqual(plusmal(-2, 5), 6)   

    def test_unterschreiben(self):
        self.assertEqual(unterschreiben("test"), "test_unterschrieben")
        self.assertEqual(unterschreiben(""), "_unterschrieben")
        self.assertEqual(unterschreiben("123"), "123_unterschrieben")

    def test_kubieren(self):
        self.assertEqual(kubieren(2), 8)      
        self.assertEqual(kubieren(3), 27)     
        self.assertEqual(kubieren(0), 0)      

if __name__ == '__main__':
    unittest.main()
