import unittest
import cube


class Test_Cube(unittest.TestCase):
    def test_cube(self):
        self.assertEquals(cube.cube(3), 27)


if __name__ == '__main':
    unittest.main()
