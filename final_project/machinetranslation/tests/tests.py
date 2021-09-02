import unittest

from translator import englishtofrench
from translator import frenchtoenglish

class TestTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertEqual(englishtofrench("How are you?"), "Comment es-tu?")
        self.assertEqual(englishtofrench("Good night"), "Bonne nuit")
        self.assertRaises(ValueError,englishtofrench,None)

class TestEnglishToFrenchNull(unittest.TestCase):
    def test2(self):
        self.assertRaises(ValueError,englishtofrench,None)

class TestTranslatorFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")
        self.assertEqual(frenchtoenglish("Comment es-tu?"), "How are you?")
        self.assertEqual(frenchtoenglish("Bonne nuit"), "Good night")
        self.assertRaises(ValueError,frenchtoenglish,None)

class TestFrencToEnglishhNull(unittest.TestCase):
    def test2(self):
        self.assertRaises(ValueError,frenchtoenglish,None)

unittest.main()
