import re, unittest

import module.content as content

class TestAppendWhitespaceFunction(unittest.TestCase):
    def test_whitespaceAmount(self):
        for _ in range(0,100):
            amount = len(content.appendWhitespace(""))
            self.assertLessEqual(amount, content.MAX_WHITESPACE, msg=f"maximum amount of whitespace should be {content.MAX_WHITESPACE}")
            self.assertGreaterEqual(amount, content.MIN_WHITESPACE, msg=f"minimum amount of whitespace should be {content.MIN_WHITESPACE}")

    def test_appendWhitespaceBefore(self):
        string = content.appendWhitespace("")
        string += "hello"
        self.assertIsNotNone(re.match(r"\s+hello", string), msg=f"'{string}' does not have adequate whitespace before and after it")

    def test_appendWhitespaceAfter(self):
        string = "hello"
        string = content.appendWhitespace(string)
        self.assertIsNotNone(re.match(r"hello\s+", string), msg=f"'{string}' does not have adequate whitespace before and after it")

    def test_appendWhitespaceBeforeAfter(self):
        string = content.appendWhitespace("")
        string += "hello"
        string = content.appendWhitespace(string)
        self.assertIsNotNone(re.match(r"\s+hello\s+", string), msg=f"'{string}' does not have adequate whitespace before and after it")

    def test_mistypeParameter(self):
        with self.assertRaises(TypeError):
            content.appendWhitespace(30)
