# -*- coding: utf-8 -*-
"""
NumPy 支持比 Python 更多种类的数值类型:
1. 	bool_存储为一个字节的布尔值(真或假)
2. 	int_默认整数，相当于 C 的long，通常为int32或int64
3. 	intc相当于 C 的int，通常为int32或int64
4. 	intp用于索引的整数，相当于 C 的size_t，通常为int32或int64
5. 	int8字节(-128 ~ 127)
6. 	int1616 位整数(-32768 ~ 32767)
7. 	int3232 位整数(-2147483648 ~ 2147483647)
8. 	int6464 位整数(-9223372036854775808 ~ 9223372036854775807)
9. 	uint88 位无符号整数(0 ~ 255)
10. 	uint1616 位无符号整数(0 ~ 65535)
11. 	uint3232 位无符号整数(0 ~ 4294967295)
12. 	uint6464 位无符号整数(0 ~ 18446744073709551615)
13. 	float_float64的简写
14. 	float16半精度浮点：符号位，5 位指数，10 位尾数
15. 	float32单精度浮点：符号位，8 位指数，23 位尾数
16. 	float64双精度浮点：符号位，11 位指数，52 位尾数
17. 	complex_complex128的简写
18. 	complex64复数，由两个 32 位浮点表示(实部和虚部)
19. 	complex128复数，由两个 64 位浮点表示(实部和虚部)
NumPy 数字类型是dtype(数据类型)对象的实例，每个对象具有唯一的特征。 这些类型可以是np.bool_，np.float32等。
数据类型对象 (dtype)
数据类型对象描述了对应于数组的固定内存块的解释，取决于以下方面：
    数据类型(整数、浮点或者 Python 对象)
    数据大小
    字节序(小端或大端)
    在结构化类型的情况下，字段的名称，每个字段的数据类型，和每个字段占用的内存块部分。
    如果数据类型是子序列，它的形状和数据类型。
字节顺序取决于数据类型的前缀<或>。<意味着编码是小端(最小有效字节存储在最小地址中)。>意味着编码是大端(最大有效字节存储在最小地址中)。
dtype可由一下语法构造：
numpy.dtype(object, align, copy)
参数为：
    Object：被转换为数据类型的对象。
    Align：如果为true，则向字段添加间隔，使其类似 C 的结构体。
    Copy:生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用。
"""
import numpy as np
if __name__ == "__main__":
    #创建结构化数据类型
    dt = np.dtype([('age',np.int8)])
    a = np.array([(10,),(20,),(30,)],dtype=dt)
   # a = np.array([[10],[20],[30]],dtype=dt)
    print a['age']
    stu = np.dtype([('name','S20'),('age','int8'),('marks','float16')])
    a = np.array([('abc',21,50),('xyz',22,54),('acd',25,58)],dtype=stu)
    print a
    print a['name']
    """
    numpy.asarray(a, dtype = None, order = None)
    1. 	a 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
    2. 	dtype 通常，输入数据的类型会应用到返回的ndarray
    3. 	order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
    """
    x = [1,2,3]
    a = np.asarray(x)
    print a
    x = (1,2,3)
    a = np.asarray(x,dtype=float)
    print a
    x = [(1,2,3),(4,5)]
    a = np.asarray(x)
    print a
    """
    numpy.frombuffer:
    此函数将缓冲区解释为一维数组。 暴露缓冲区接口的任何对象都用作参数来返回ndarray。
    numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
   1. 	buffer 任何暴露缓冲区借口的对象
   2. 	dtype 返回数组的数据类型，默认为float
   3. 	count 需要读取的数据数量，默认为-1，读取所有数据
   4. 	offset 需要读取的起始位置，默认为0
    """
    s = 'hello word'
    a = np.frombuffer(s,dtype='S1')
    print a
    """
    numpy.fromiter:
    此函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组。
    1. 	iterable 任何可迭代对象
    2. 	dtype 返回数组的数据类型
    3. 	count 需要读取的数据数量，默认为-1，读取所有数据
    """
    s = "123456"
    a = np.fromiter(s,dtype='S1')
    print a
    list = range(10)
    a = np.fromiter(list,dtype='int8')
    print a
