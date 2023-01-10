import unittest
from translator import french_to_english, english_to_french

class Test_FrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test2(self):
        self.assertEqual(french_to_english(""), "")

class Test_EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        self.assertEqual(english_to_french(""), "")

unittest.main()