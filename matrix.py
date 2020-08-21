"""
4x4 matrix
"""

import numpy as np
import math

class Matrix(object):
    """
    4x4 matrix
    """
    def __init__(self,fill_value:float=None):
        super().__init__()

        if fill_value is None:
            self.m=np.zeros((4,4))
        else:
            self.m=np.full((4,4),fill_value)

    @classmethod
    def from_matrix(cls,matrix:Matrix)->Matrix:
        ret=Matrix()
        for i in range(4):
            for j in range(4):
                ret.set(i,j,matrix.get(i,j))

        return ret
    @classmethod
    def from_ndarray(cls,arr:np.ndarray)->Matrix:
        if arr.shape!=(4,4):
            message="Expected shape (4,4) but got {}.".format(arr.shape)
            raise ValueError(message)

        ret=Matrix()
        for i in range(4):
            for j in range(4):
                ret.set(i,j,arr[i,j])

        return ret

    def __str__(self):
        ret=""
        for i in range(4):
            for j in range(4):
                ret+=str(self.m[i,j])
                ret+=" "
            ret+="\n"

        ret=ret[:len(ret)-1]

        return ret

    def get_ndarray(self)->np.ndarray:
        """
        Returns the underlying ndarray instance.
        """
        return self.m

    def get(self,row:int,col:int)->float:
        return self.m[row,col]
    
    def set(self,row:int,col:int,value:float):
        self.m[row,col]=value

    def add(self,mat:Matrix)->Matrix:
        ret=Matrix()
        for i in range(4):
            for j in range(4):
                v1=self.m[i,j]
                v2=mat.m[i,j]

                ret.set(i,j,v1+v2)
        
        return ret
    def sub(self,mat:Matrix)->Matrix:
        ret=Matrix()
        for i in range(4):
            for j in range(4):
                v1=self.m[i,j]
                v2=mat.m[i,j]

                ret.set(i,j,v1-v2)
        
        return ret
    def mult(self,mat:Matrix)->Matrix:
        mult_arr=np.matmul(self.m,mat.m)
        return Matrix.from_ndarray(mult_arr)

    def transpose(self)->Matrix:
        ret=Matrix()
        for i in range(4):
            for j in range(4):
                ret.set(i,j,self.m[j,i])

        return ret
    def invert(self)->Matrix:
        inv_arr=np.linalg.inv(self.m)
        return Matrix.from_ndarray(inv_arr)

    @classmethod
    def identity(cls)->Matrix:
        ret=Matrix(0.0)
        for i in range(4):
            ret.set(i,i,1.0)

        return ret
    @classmethod
    def random(cls)->Matrix:
        rand_arr=np.random.rand(4,4)
        return Matrix.from_ndarray(rand_arr)
    @classmethod
    def translaion(cls,translation_x:float,translation_y:float,translation_z:float)->Matrix:
        ret=Matrix(0.0)
        ret.set(0,0,1.0)
        ret.set(0,3,translation_x)
        ret.set(1,1,1.0)
        ret.set(1,3,translation_y)
        ret.set(2,2,1.0)
        ret.set(2,3,translation_z)
        ret.set(3,3,1.0)

        return ret
    @classmethod
    def scaling(cls,scale_x:float,scale_y:float,scale_z:float)->Matrix:
        ret=Matrix(0.0)
        ret.set(0,0,scale_x)
        ret.set(1,1,scale_y)
        ret.set(2,2,scale_z)
        ret.set(3,3,1.0);

        return ret
    @classmethod
    def rotation_x(cls,th:float)->Matrix:
        ret=Matrix(0.0)
        ret.set(0, 0, 1.0)
        ret.set(1,1,math.cos(th))
        ret.set(1,2,-math.sin(th))
        ret.set(2,1,math.sin(th))
        ret.set(2,2,math.cos(th))
        ret.set(3,3,1.0)

        return ret
    @classmethod
    def rotation_y(cls,th:float)->Matrix:
        ret=Matrix(0.0)
        ret.set(0,0,math.cos(th))
        ret.set(0,2,math.sin(th))
        ret.set(1,1,1.0)
        ret.set(2,0,-math.sin(th))
        ret.set(2,2,math.cos(th))
        ret.set(3,3,1.0)

        return ret
    @classmethod
    def rotation_z(cls,th:float)->Matrix:
        ret=Matrix(0.0)
        ret.set(0,0,math.cos(th))
        ret.set(0,1,-math.sin(th))
        ret.set(1,0,math.sin(th))
        ret.set(1,1,math.cos(th))
        ret.set(2,2,1.0)
        ret.set(3,3,1.0)

        return ret
    @classmethod
    def rotation(cls,axis_x:float,axis_y:float,axis_z:float,th:float)->Matrix:
        cos_th=math.cos(th)
        sin_th=math.sin(th)
        
        ret=Matrix()
        ret.set(0,0,cos_th+axis_x*axis_x*(1.0-cos_th))
        ret.set(0,1,axis_x*axis_y*(1.0-cos_th)-axis_z*sin_th)
        ret.set(0,2,axis_x*axis_z*(1.0-cos_th)+axis_y*sin_th)
        ret.set(0,3,0.0)
        ret.set(1,0,axis_y*axis_x*(1.0-cos_th)+axis_z*sin_th)
        ret.set(1,1,cos_th+axis_y*axis_y*(1.0-cos_th))
        ret.set(1,2,axis_y*axis_z*(1.0-cos_th)-axis_x*sin_th)
        ret.set(1,3,0.0)
        ret.set(2,0,axis_z*axis_x*(1.0-cos_th)-axis_y*sin_th)
        ret.set(2,1,axis_z*axis_y*(1.0-cos_th)+axis_x*sin_th)
        ret.set(2,2,cos_th+axis_z*axis_z*(1.0-cos_th))
        ret.set(2,3,0.0)
        ret.set(3,0,0.0)
        ret.set(3,1,0.0)
        ret.set(3,2,0.0)
        ret.set(3,3,1.0)

        return ret
