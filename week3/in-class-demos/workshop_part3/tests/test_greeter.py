import setup

setup.setup_path()

import unittest
from src.greeter import greet


class Test_TestGreeting(unittest.TestCase):
    def test_greets_hello_world(self):
        self.assertEqual("Hello, World!", greet())


if __name__ == "__main__":
    unittest.main()
