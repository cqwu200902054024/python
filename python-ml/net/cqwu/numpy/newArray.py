#-*-coding:utf-8 -*-
import numpy as np
"""
数组的创建
"""
if __name__ == "__main__":
    #创建一个空数组
    #numpy.empty(shape, dtype = float, order = 'C')
    em = np.empty((2,3),dtype=float)
    print em
    #创建一个以0填充的数组
    #numpy.zeros(shape, dtype = float, order = 'C')
    zero = np.zeros((3,4))
    print zero
    #创建一个以1填充的数组
    one = np.ones((3,4),dtype=[('x','int8'),('y','int8'),('z','int8'),('s','int8')])
    print one
    print one['y']
    one = np.ones((3,4),dtype='int8')
    print "===="
    print one