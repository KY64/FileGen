import unittest

import module.content as content

class TestGenerateContentFunction(unittest.TestCase):
    def test_returnType(self):
        string = content.generateContent(1000)
        self.assertIsInstance(string, str)

    def test_lengthOfString(self):
        length = [1, 12, 24, 40, 320]
        for i in length:
            with self.subTest(i=i):
                string = content.generateContent(i)
                self.assertEqual(len(string), i)

    def test_lessThanOneLength(self):
        with self.assertRaises(ValueError):
            content.generateContent(-1)
        with self.assertRaises(ValueError):
            content.generateContent(0)

    def test_mistypeParameter(self):
        with self.assertRaises(TypeError):
            content.generateContent("a")

    def test_stringVariation(self):
        string = content.generateContent(1000)

        with self.subTest(string=string):
            self.assertRegex(string, r"[a-zA-Z]+", msg="Content should contains alphabetical string")
        with self.subTest(string=string):
            self.assertRegex(string, r"\s+\w+\s+", msg="Content should contains alphanumeric")
        with self.subTest(string=string):
            self.assertRegex(string, r"\d+\.\d+", msg="Content should contains real number")
        with self.subTest(string=string):
            self.assertRegex(string, r"\d+", msg="Content should contains integer")
