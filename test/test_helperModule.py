import os, unittest

import module.helper as helper
from module.content import generateContent

class TestHelperFunction(unittest.TestCase):
    def test_isAlphabet(self):
        with self.subTest():
            self.assertIsNotNone(helper.isAlphabet("halo"))
        with self.subTest():
            self.assertIsNone(helper.isAlphabet("123"))

    def test_isAlphanumeric(self):
        with self.subTest():
            self.assertIsNotNone(helper.isAlphanumeric(" as2f4X    "))
        with self.subTest():
            self.assertIsNone(helper.isAlphanumeric("as2f4X"))
        with self.assertRaises(ValueError):
            helper.isAlphanumeric("halo")
        with self.assertRaises(ValueError):
            helper.isAlphanumeric("123")

    def test_isInteger(self):
        with self.subTest():
            self.assertIsNotNone(helper.isNumber("123"))
        with self.subTest():
            self.assertIsNone(helper.isNumber("123.321"))

    def test_isFloat(self):
        with self.subTest():
            self.assertIsNotNone(helper.isFloat("123.321"))
        with self.subTest():
            self.assertIsNone(helper.isFloat("123"))

    def test_isFileExists(self):
        path = "test-file.pytest"
        with self.subTest():
            self.assertEqual(helper.isFileExists(path), path)
        with self.subTest():
            f = open(path, "w")
            f.write("test")
            f.close()
            arr = path.split('.')
            newPath = f"{arr[0]}-002.{arr[1]}"
            self.assertEqual(helper.isFileExists(path), newPath)
            os.remove(path)

    def test_fitContent(self):
        string = generateContent(40)
        trim_string = helper.fitContent(string, 30)
        self.assertEqual(len(trim_string), 30)
        with self.assertRaises(ValueError):
            helper.fitContent(string, 0)
        with self.assertRaises(TypeError):
            helper.fitContent(19, string)
