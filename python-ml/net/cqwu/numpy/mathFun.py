#-*-coding:utf-8-*-
"""
    NumPy - 算数函数
    很容易理解的是，NumPy 包含大量的各种数学运算功能。 NumPy 提供标准的三角函数，算术运算的函数，复数处理函数等。

    NumPy - 算数运算
    用于执行算术运算(如add()，subtract()，multiply()和divide())的输入数组必须具有相同的形状或符合数组广播规则。
"""
import numpy as np
if __name__ == '__main__':
    #NumPy 拥有标准的三角函数，它为弧度制单位的给定角度返回三角函数比值。
    a = np.array([0,30,60,90])
    print np.sin(a * np.pi / 180)
    print np.cos(a * np.pi / 180)
    print np.tan(a * np.pi / 180)
    #反三角函数arcsin，arccos，和arctan函数.degrees()函数通过将弧度制转换为角度制来验证。
    sin = np.arcsin(np.sin(a * np.pi / 180))
    print np.degrees(sin)
    """
    numpy.around()返回四舍五入到所需精度的值
    numpy.around(a,decimals)
    1. 	a 输入数组
    2. 	decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
    """
    print np.around([1.0,5.55,  123,  0.567,  25.532],decimals=1)
    #numpy.floor() 返回不大于输入参数的最大整数。
    print np.floor([-1.7,  1.5,  -0.2,  0.6,  10])
    #numpy.ceil()函数返回输入值的上限，即，标量x的上限是最小的整数i ，使得i> = x
    a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
    print np.ceil(a)
    a = np.arange(9,dtype='float_').reshape(3,3)
    b = np.array([10,20,30])
    print a
    print b
    print np.add(a,b)
    print np.subtract(a,b)
    print np.multiply(a,b)
    print np.divide(a,b)
    """
        numpy.reciprocal()
       此函数返回参数逐元素的倒数，。 由于 Python 处理整数除法的方式，对于绝对值大于 1 的整数元素，结果始终为 0， 对于整数 0，则发出溢出警告。
    """
    a = np.array([0.25,  1.33,  1,  0,  100])
    #print np.reciprocal(a)
    b = np.array([100])
    print np.reciprocal(b)
    #numpy.power()函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
    a = np.array([10,100,1000])
    print np.power(a,2)
    #numpy.mod()函数返回输入数组中相应元素的除法余数。 函数numpy.remainder()也产生相同的结果。
    a = np.array([10,20,30])
    b = np.array([3,5,7])
    print np.mod(a,b)
    print np.remainder(a,b)
    """
    以下函数用于对含有复数的数组执行操作。
    numpy.real() 返回复数类型参数的实部。
    numpy.imag() 返回复数类型参数的虚部。
    numpy.conj() 返回通过改变虚部的符号而获得的共轭复数。
    numpy.angle() 返回复数参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示。
    """

