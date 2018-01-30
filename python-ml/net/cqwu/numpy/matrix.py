#-*-coding:utf-8-*-
"""
    NumPy - 矩阵库
    NumPy 包包含一个 Matrix库numpy.matlib。此模块的函数返回矩阵而不是返回ndarray对象。
"""
import numpy.matlib as mt
import numpy as np

if __name__ == '__main__':
    #numpy.matlib.empty(shape, dtype, order)函数返回一个新的矩阵，而不初始化元素
    print mt.empty((2,2))
    #numpy.matlib.zeros()返回以零填充的矩阵。
    print mt.zeros((3,3))
    #numpy.matlib.ones()返回以一填充的矩阵。
    print mt.ones((4,4))
    #numpy.matlib.eye(n, M,k, dtype)返回一个矩阵，对角线元素为 1，其他位置为零。
    print mt.eye(n = 5,M = 5,k = 0,dtype=float)
    #numpy.matlib.identity()函数返回给定大小的单位矩阵。单位矩阵是主对角线元素都为 1 的方阵。
    print mt.identity(5)
    #numpy.matlib.rand()函数返回给定大小的填充随机值的矩阵。
    print mt.rand(3,3)
    #矩阵总是二维的，而ndarray是一个 n 维数组。 两个对象都是可互换的。
    m = np.matrix('1,2;3,4')
    print m
    print type(m)
    print np.asarray(m)

