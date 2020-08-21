"""
Vector
"""

import numpy as np
import math
from typing import Tuple

from matrix import Matrix

class Vector(object):
    """
    Vector
    """
    def __init__(self,init_values:Tuple[float,float,float]=None):
        super().__init__()

        if init_values is None:
            self.v=np.zeros((4,1))
        else:
            self.v=np.empty((4,1))
            self.v[0,0]=init_values[0]
            self.v[1,0]=init_values[1]
            self.v[2,0]=init_values[2]

        self.v[3,0]=1.0

    @classmethod
    def from_angles(cls,angle_v:float,angle_h:float)->"Vector":
        x=math.cos(angle_h)
        y=math.sin(angle_v)
        z=-math.sin(angle_h)
        size=math.sqrt(x*x+y*y+z*z)

        return Vector((x/size,y/size,z/size))
    @classmethod
    def from_vector(cls,v:"Vector")->"Vector":
        return Vector((v.get_x(),v.get_y(),v.get_z()))
    @classmethod
    def from_ndarray(cls,arr:np.ndarray)->"Vector":
        if arr.shape!=(3,1) and arr.shape!=(4,1):
            message="Expected shape (3, 1) or (4, 1) but got {}.".format(arr.shape)
            raise ValueError(message)

        return Vector((arr[0,0],arr[1,0],arr[2,0]))

    def __str__(self):
        return "({},{},{})".format(self.v[0,0],self.v[1,0],self.v[2,0])

    def get_ndarray(self):
        """
        Returns the underlying ndarray instance.
        """
        return self.v

    def get(self)->Tuple[float,float,float]:
        return (self.v[0,0],self.v[1,0],self.v[2,0])
    def get_x(self)->float:
        return self.v[0,0]
    def get_y(self)->float:
        return self.v[1,0]
    def get_z(self)->float:
        return self.v[2,0]

    def set(self,x:float,y:float,z:float):
        self.v[0,0]=x
        self.v[1,0]=y
        self.v[2,0]=z
    def set_x(self,value):
        self.v[0,0]=value
    def set_y(self,value):
        self.v[1,0]=value
    def set_z(self,value):
        self.v[2,0]=value

    def get_square_size(self)->float:
        x=self.v[0,0]
        y=self.v[1,0]
        z=self.v[2,0]

        return x*x+y*y+z*z
    def get_size(self)->float:
        x=self.v[0,0]
        y=self.v[1,0]
        z=self.v[2,0]

        return math.sqrt(x*x+y*y+z*z)

    def normalize(self)->"Vector":
        size=self.get_size()

        x=self.v[0,0]/size
        y=self.v[1,0]/size
        z=self.v[2,0]/size

        return Vector((x,y,z))

    def add(self,v:"Vector")->"Vector":
        x=self.get_x()+v.get_x()
        y=self.get_y()+v.get_y()
        z=self.get_z()+v.get_z()

        return Vector((x,y,z))
    def sub(self,v:"Vector")->"Vector":
        x=self.get_x()-v.get_x()
        y=self.get_y()-v.get_y()
        z=self.get_z()-v.get_z()

        return Vector((x,y,z))
    def scale(self,scale:float)->"Vector":
        x=self.get_x()*scale
        y=self.get_y()*scale
        z=self.get_z()*scale

        return Vector((x,y,z))
    def cross(self,v:"Vector")->"Vector":
        a1=self.get_x()
        a2=self.get_y()
        a3=self.get_z()
        b1=v.get_x()
        b2=v.get_y()
        b3=v.get_z()

        x=a2*b3-b2*a3
        y=a3*b1-b3*a1
        z=a1*b2-b1*a2

        return Vector((x,y,z))
    def dot(self,v:"Vector")->float:
        x1=self.get_x()
        y1=self.get_y()
        z1=self.get_z()
        x2=v.get_x()
        y2=v.get_y()
        z2=v.get_z()

        return x1*x2+y1*y2+z1*z2

    def get_angle_v(self)->float:
        xz_vec=Vector(self.get_x(),0.0,self.get_z())

        cos_th=self.dot(xz_vec)/(self.get_size()*xz_vec.get_size())
        th=math.acos(cos_th)

        return th
    def get_angle_h(self)->float:
        x_axis=Vector(init_values=(1.0,0.0,0.0))
        xz_vec=Vector(init_values=(self.get_x(),0.0,self.get_z()))

        cos_th=xz_vec.dot(x_axis)/xz_vec.get_size()
        th=math.acos(cos_th)

        if self.get_z()>=0.0:
            th*=(-1.0)

        return th
    
    def transform(self,matrix:Matrix)->"Vector":
        transformed_arr=np.matmul(matrix.get_ndarray(),self.v)
        return Vector.from_ndarray(transformed_arr)
    def transform_sr(self,matrix:Matrix)->"Vector":
        mat_temp=np.empty((4,1))
        mat_temp[0,0]=self.v[0,0]
        mat_temp[1,0]=self.v[1,0]
        mat_temp[2,0]=self.v[2,0]
        mat_temp[3,0]=0.0

        transformed_arr=np.matmul(matrix,mat_temp)

        return Vector(transformed_arr)

    def rot_x(self,th:float)->"Vector":
        rot_mat=Matrix.rotation_x(th)
        return self.transform(rot_mat)
    def rot_y(self,th:float)->"Vector":
        rot_mat=Matrix.rotation_y(th)
        return self.transform(rot_mat)
    def rot_z(self,th:float)->"Vector":
        rot_mat=Matrix.rotation_z(th)
        return self.transform(rot_mat)
    def rot(self,axis_x:float,axis_y:float,axis_z:float,th:float)->"Vector":
        rot_mat=Matrix.rotation(axis_x,axis_y,axis_z,th)
        return self.transform(rot_mat)
