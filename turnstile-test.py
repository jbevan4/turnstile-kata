import unittest

from turnstile import transition


class MyTestCase(unittest.TestCase):
    def test_framework_is_working(self):
        self.assertEqual(True, True)

    def test_turnstile_exists(self):
        self.assertTrue(hasattr(transition, '__call__'))


if __name__ == '__main__':
    unittest.main()
