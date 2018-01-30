#-*-coding:utf-8 -*-
"""
NumPy - 线性代数
NumPy 包包含numpy.linalg模块，提供线性代数所需的所有功能。

    1. 	dot 两个数组的点积
    2. 	vdot 两个向量的点积
    3. 	inner 两个数组的内积
    4. 	matmul 两个数组的矩阵积
    5. 	determinant 数组的行列式
    6. 	solve 求解线性矩阵方程
    7. 	inv 寻找矩阵的乘法逆矩阵
"""
import numpy as np
import numpy.matlib as mat
if __name__ == '__main__':
    """
    numpy.dot()
    此函数返回两个数组的点积。 对于二维向量，其等效于矩阵乘法。 对于一维数组，它是向量的内积。 对于 N 维数组，它是a的最后一个轴上的和与b的倒数第二个轴的乘积。
    """
    a = np.array([1,2,3,4])
    b = np.array([4,5,6,7])
    print np.dot(a,b)
    a = np.array([[1,2],[3,4]])
    b = np.array([[11,12],[13,14]])
    print a
    print b
    #[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
    print np.dot(a,b)
    """
    numpy.vdot()
    此函数返回两个向量的点积。 如果第一个参数是复数，那么它的共轭复数会用于计算。 如果参数id是多维数组，它会被展开。
    """

    a = np.array([1,2,3,4])
    b = np.array([1,2,3,4])
    print np.vdot(a,b)

    a = np.array([[1,2],[3,4]])
    b = np.array([[1,2],[3,4]])
    print np.vdot(a,b)
    """
    numpy.inner()
    此函数返回一维数组的向量内积。 
    """
    a = np.array([1,2,3,4])
    b = np.array([1,2,3,4])
    print np.inner(a,b)
    a = np.array([[1,2],[3,4]])
    b = np.array([[1,2],[3,4]])
    print a
    print b
    #[[1 * 1 + 2 * 2,1 * 3 + 2 * 4],[3 * 1 + 4 * 2, 3 * 3 + 4 * 4]]
    print np.inner(a,b)
    """
    numpy.matmul()
    函数返回两个数组的矩阵乘积。 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播。
    另一方面，如果任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除。
    """
    a = np.array([[1,2],[3,4]])
    b = np.array([[1,2],[3,4]])
    print np.matmul(a,b)
    a = np.array([1,2])
    print "-----"
    print np.matmul(a,b)
    #如果任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除
    a = np.array([[1,2],[1,1]])
    print np.matmul(a,b)
    a = np.arange(8).reshape(2,4)
    print a
    b = np.arange(8).reshape(4,2)
    print b
    print np.matmul(a,b)
    print '===='
    a = np.arange(8).reshape(2,2,2)
    print a
    b = np.arange(8).reshape(2,4)
    print b
    print np.matmul(a,b)
    #numpy.linalg.det()函数计算输入矩阵的行列式。
    a = np.arange(9).reshape(3,3)
    print a
    print np.linalg.det(a)
    a = np.arange(4).reshape(2,2)
    print a
    print np.linalg.det(a)
    b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
    print b
    print -2 * 6 * 7 + 1 * 5 * 2 + 1 * 4 * 8 + 2 * 2 * 1 - 1 * 4 * 7 - 6 * 8 * 5
    print np.linalg.det(b)
    #numpy.linalg.solve()函数给出了矩阵形式的线性方程的解。
    a = np.array([[4,2,-1],[3,-1,2],[11,3,0]])
    b = np.array([2,10,8])
    #print np.linalg.solve(a,b)
    a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
    b = np.array([6,-4,27])
    print np.linalg.solve(a,b)
    #numpy.linalg.inv()函数来计算矩阵的逆。
    a = np.array([[1,2],[3,4]])
    print np.linalg.inv(a)
    a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
    print np.linalg.inv(a)
    b = np.array([[6],[-4],[27]])
    print np.linalg.solve(a,b)
    print np.dot(np.linalg.inv(a),b)






