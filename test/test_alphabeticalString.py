import re, unittest

import module.content as content

class TestAlphabeticalStringFunction(unittest.TestCase):
    def test_returnType(self):
        self.assertIsInstance(content.alphabeticalString(20), str)

    def test_returnAlphabeticalString(self):
        string = content.alphabeticalString(20)
        self.assertIsNotNone(re.fullmatch(r"[a-zA-Z]+", string), msg=f"alphabeticalString() should return string containing alphabet only, not '{string}'")

    def test_lengthOfString(self):
        string = content.alphabeticalString(20)
        self.assertEqual(len(string), 20)

    def test_mistypeParameter(self):
        with self.assertRaises(TypeError):
            content.alphabeticalString("a")

