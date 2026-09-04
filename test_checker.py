import unittest
from checker import check

class TestCheck(unittest.TestCase):
    def test_ready(self):
        self.assertEqual(check("1.0.0", "staging"), "READY: 1.0.0 on staging")
    def test_bad_version(self):
        self.assertEqual(check("1", "prod"), "NOT READY: invalid version")
    def test_bad_env(self):
        self.assertEqual(check("1.0.0", "qa"), "NOT READY: invalid environment")

if __name__ == "__main__":
    unittest.main()
