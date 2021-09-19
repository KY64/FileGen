import unittest

import module.content as content

class TestRealNumberFunction(unittest.TestCase):
    def test_returnType(self):
        self.assertIsInstance(content.realnumber(), float)

    def test_realNumberRange(self):
        self.assertLessEqual(content.realnumber(), content.MAX_RANGE, msg=f"realnumber() should return value less than equal to {content.MAX_RANGE}")
        self.assertGreaterEqual(content.realnumber(), content.MIN_RANGE, msg=f"realnumber() should return value more than equal to {content.MIN_RANGE}")

