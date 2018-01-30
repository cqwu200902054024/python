#-*-coding: utf-8 -*-
"""
    数组属性:
    ndarray.shape
    这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
"""
import numpy as np
if __name__ == "__main__":
    #2行3列(2L, 3L)
    a = np.array([[1,2,3],[4,5,6]])
    print a.shape
    #调整数组大小
    a.shape = (3,2)
    print a

    b = a.reshape(2,3)
    print b
    print "========="
    print a

    a = np.arange(24)
    print a
    #返回数组的维数
    print a.ndim
    a.shape = (3,8)
    print a.ndim
    a.shape = (2,3,4)
    print a.ndim
    #数组中每个元素的字节单位长度
    print a.itemsize
    #numpy.flags 对象的每个属性值