import unittest
import numpy as np
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

        #print(v1)
        #print(v2)

    def test_from_angles(self):
        expected=(0.5774, 0.5774, -0.5774)
        v=Vector.from_angles(math.pi/4.0,math.pi/4.0)

        self.assertAlmostEqual(expected[0],v.get_x(),delta=1.0e-3)
        self.assertAlmostEqual(expected[1],v.get_y(),delta=1.0e-3)
        self.assertAlmostEqual(expected[2],v.get_z(),delta=1.0e-3)
    def test_from_vector(self):
        v1=Vector((1.0,2.0,3.0))
        v2=Vector.from_vector(v1)

        self.assertAlmostEqual(v1.get_x(),v2.get_x(),delta=1.0e-6)
        self.assertAlmostEqual(v1.get_y(),v2.get_y(),delta=1.0e-6)
        self.assertAlmostEqual(v1.get_z(),v2.get_z(),delta=1.0e-6)
    def test_from_ndarray(self):
        arr=np.random.rand(4,1)
        v=Vector.from_ndarray(arr)

        #print(v)

    def test_get_square_size(self):
        expected=3.0
        v=Vector((1.0,1.0,1.0))
        actual=v.get_square_size()

        self.assertAlmostEqual(expected,actual,1.0e-6)
    def test_get_size(self):
        expected=math.sqrt(3.0)
        v=Vector((1.0,1.0,1.0))
        actual=v.get_size()

        self.assertAlmostEqual(expected,actual,1.0e-6)

    def test_normalize(self):
        expected=(0.57735,0.57735,0.57735)
        v=Vector((1.0,1.0,1.0))
        normalized_v=v.normalize()

        self.assertAlmostEqual(expected[0],normalized_v.get_x(),delta=1.0e-3)
        self.assertAlmostEqual(expected[1],normalized_v.get_y(),delta=1.0e-3)
        self.assertAlmostEqual(expected[2],normalized_v.get_z(),delta=1.0e-3)

    def test_add(self):
        expected=(5.0,9.0,1.0)

        v1=Vector((1.0,2.0,3.0))
        v2=Vector((4.0,7.0,-2.0))
        add=v1.add(v2)
        
        self.assertAlmostEqual(expected[0],add.get_x(),1.0e-6)
        self.assertAlmostEqual(expected[1],add.get_y(),1.0e-6)
        self.assertAlmostEqual(expected[2],add.get_z(),1.0e-6)
    def test_sub(self):
        expected=(-3.0,-5.0,5.0)

        v1=Vector((1.0,2.0,3.0))
        v2=Vector((4.0,7.0,-2.0))
        add=v1.sub(v2)
        
        self.assertAlmostEqual(expected[0],add.get_x(),1.0e-6)
        self.assertAlmostEqual(expected[1],add.get_y(),1.0e-6)
        self.assertAlmostEqual(expected[2],add.get_z(),1.0e-6)
    def test_scale(self):
        expected=(2.0,3.0,4.0)

        v=Vector((1.0,1.5,2.0))
        scale=v.scale(2.0)

        self.assertAlmostEqual(expected[0],scale.get_x(),1.0e-6)
        self.assertAlmostEqual(expected[1],scale.get_y(),1.0e-6)
        self.assertAlmostEqual(expected[2],scale.get_z(),1.0e-6)
    def test_cross(self):
        expected=(13.0,-12.0,9.0)

        v1=Vector((3.0,4.0,1.0))
        v2=Vector((3.0,7.0,5.0))
        cross=v1.cross(v2)

        self.assertAlmostEqual(expected[0],cross.get_x(),1.0e-6)
        self.assertAlmostEqual(expected[1],cross.get_y(),1.0e-6)
        self.assertAlmostEqual(expected[2],cross.get_z(),1.0e-6)
    def test_dot(self):
        expected=42.0

        v1=Vector((3.0,4.0,1.0))
        v2=Vector((3.0,7.0,5.0))
        actual=v1.dot(v2)

        self.assertAlmostEqual(expected,actual,1.0e-6)

if __name__=="__main__":
    unittest.main()
