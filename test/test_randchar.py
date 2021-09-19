import re, unittest

import module.content as content

class TestRandCharFunction(unittest.TestCase):
    def test_returnString(self):
        self.assertIsInstance(content.randchar(), str)

    def test_returnAlphabet(self):
        char = content.randchar()
        self.assertIsNotNone(re.match(r"[a-zA-Z]", char), msg=f"randchar() should return alphabet not {char}")

    def test_returnSingleCharacter(self):
        length = len(content.randchar())
        self.assertEqual(length, 1)

    def test_shouldHaveNoParameter(self):
        with self.assertRaises(TypeError):
            content.randchar("a")
