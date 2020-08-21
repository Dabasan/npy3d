import unittest
import math
from vector import Vector

class VectorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_init(self):
        v1=Vector()
        v2=Vector((1.0,-2.0,4.5))

        print(v1)
        print(v2)

    def test_from_angles(self):
        v=Vector.from_angles(math.pi/4.0,math.pi/4.0)
        expected=(0.5774, 0.5774, -0.5774)

        self.assertAlmostEqual(v.get_x(),expected[0],delta=1.0e-3)
        self.assertAlmostEqual(v.get_y(),expected[1],delta=1.0e-3)
        self.assertAlmostEqual(v.get_z(),expected[2],delta=1.0e-3)

if __name__=="__main__":
    unittest.main()
