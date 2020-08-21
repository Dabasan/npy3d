import unittest
import numpy as np
import math
from matrix import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_init(self):
        m1=Matrix()
        m2=Matrix(1.0)

        #print(m1)
        #print(m2)

    def test_from_matrix(self):
        m1=Matrix(4.5)
        m2=Matrix.from_matrix(m1)

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(m1.get(i,j),m2.get(i,j),delta=1.0e-6)
    def test_from_ndarray(self):
        arr=np.random.rand(4,4)
        m=Matrix.from_ndarray(arr)

        #print(m)
    
    def test_add(self):
        m1=Matrix.random()
        m2=Matrix.random()
        add=m1.add(m2)

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(m1.get(i,j)+m2.get(i,j),add.get(i,j),delta=1.0e-6)
    def test_sub(self):
        m1=Matrix.random()
        m2=Matrix.random()
        add=m1.sub(m2)

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(m1.get(i,j)-m2.get(i,j),add.get(i,j),delta=1.0e-6)
    def test_mult(self):
        m1=Matrix.random()
        m2=Matrix.random()
        mult=m1.mult(m2)

        #print(m1)
        #print(m2)
        #print(mult)

    def test_transpose(self):
        m=Matrix.random()
        transposed=m.transpose()

        #print(m)
        #print(transposed)
    def test_invert(self):
        m=Matrix.random()
        invert=m.invert()

        #print(m)
        #print(invert)

    def test_identity(self):
        identity=Matrix.identity()
        #print(identity)

if __name__=="__main__":
    unittest.main()
