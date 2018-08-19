import unittest
import hello


class Test_Hello(unittest.TestCase):
    def test_world(self):
        self.assertEquals(hello.world("Hello, World!"), "Hello, World!")

    def test_world_capitalize(self):
        self.assertEquals(hello.world_capitalize(
            "Hello, World!"), "Hello, world!")

    def test_world_split(self):
        self.assertEquals(hello.world_split("Hello, World!"), ["Hello,", "World!"])


if __name__ == '__main__':
    unittest.main()
