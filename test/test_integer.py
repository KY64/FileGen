import unittest

import module.content as content

class TestIntegerFunction(unittest.TestCase):
    def test_returnType(self):
        self.assertEqual(type(content.integer()), int)

    def test_integerRange(self):
        self.assertLessEqual(content.integer(), content.MAX_RANGE, msg=f"integer() should return value less than equal to {content.MAX_RANGE}")
        self.assertGreaterEqual(content.integer(), content.MIN_RANGE, msg=f"integer() should return value more than equal to {content.MIN_RANGE}")
