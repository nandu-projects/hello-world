import unittest
import os
import sys

# Ensure project root is in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import get_greeting

class TestHelloWorld(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(get_greeting(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(get_greeting("Antigravity"), "Hello, Antigravity!")

    def test_whitespace_name(self):
        self.assertEqual(get_greeting("  Nandu  "), "Hello, Nandu!")

    def test_empty_string(self):
        self.assertEqual(get_greeting(""), "Hello, World!")

    def test_none_value(self):
        self.assertEqual(get_greeting(None), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
