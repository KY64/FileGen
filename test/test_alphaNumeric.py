import re, unittest

import module.content as content

class TestAlphaNumericFunction(unittest.TestCase):
    def test_returnType(self):
        self.assertIsInstance(content.alphaNumeric(20), str)

    def test_returnAlphaNumeric(self):
        string = content.alphaNumeric(20).strip()
        message = f"alphaNumeric() should return string containing alphabet and number not '{string}'"

        with self.subTest(string=string):
            self.assertIsNotNone(re.fullmatch(r"[a-zA-Z0-9]+", string), msg=message)
        with self.subTest(string=string):
            self.assertRegex(string, r"\d+") # similar with re.search()
        with self.subTest(string=string):
            self.assertRegex(string, r"[a-zA-Z]+")

    def test_lengthOfString(self):
        string = content.alphaNumeric(20).strip()
        self.assertEqual(len(string), 20)

    def test_containWhitespace(self):
        string = content.alphaNumeric(20)
        self.assertIsNotNone(re.fullmatch(r"^\s+[a-zA-Z0-9]+\s+", string), msg=f"alphaNumeric() should has whitespaces before and after the string")

    def test_mistypeParameter(self):
        with self.assertRaises(TypeError):
            content.alphaNumeric("a")
