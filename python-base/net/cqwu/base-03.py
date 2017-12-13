#-*- coding: UTF-8 -*-
"""
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""
def printme(str):
    print str

def changeInt(a):
    a = 10

def changeList(list):
    list.append([1,2,3,4,4,5])
def testParam(a,b):
    print a,b
def printInfo(name,age = 32):
    print name,age
def printInfoAll(name,*info):
    print name
    for i in info:
        print i
Money = 2
def addMoney():
    """在函数中修改局部变量"""
    global Money
    Money = Money + 1
def  exception_param(param):
    try:
        return int(param)
    except ValueError:
        print "异常的参数"
    else:
        print "========"
if __name__ == '__main__':
    printme("ssss")
    a = [1,2,3]
    a = "runoob"
    """
    [1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，
    也可以指向 String 类型对象。
    """
    """
    可更改(mutable)与不可更改(immutable)对象
    在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
    python 函数的参数传递：
    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
    """
    b = 2
    changeInt(b)
    print b
    list = [10,20,30]
    changeList(list)
    print list
    """
    必备参数
    关键字参数
    默认参数
    不定长参数
    """
    """
    关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
    使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
    """
    testParam(b=5, a=4)
    #调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
    printInfo(name = 'zp',age = 34)
    printInfoAll('zp',1,32,323,"tet")
    """
    匿名函数
   python 使用 lambda 来创建匿名函数。
    lambda只是一个表达式，函数体比def简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
    """
    sum = lambda x,y: x + y
    print sum(10,20)
    """
    全局变量和局部变量
    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
    一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
    每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。
    Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
    因此，如果要给函数内的全局变量赋值，必须使用 global 语句。
    global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了。
    """
    """
    dir()函数
    dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
    返回的列表容纳了在一个模块里定义的所有模块，变量和函数。
    """
    import math
    print dir(math)
    """
    globals() 和 locals() 函数
    根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
    如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
    如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
    两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
    reload() 函数
    当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
    因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：
    reload(module_name)
    """
    f = open(r"D:\data\in\cdpi\test.txt","r")
    print f.name
    print f.read()
    f.close()

    """
    try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
使用except而带多种异常类型
你也可以使用相同的except语句来处理多个异常信息，如下所示：
try:
    正常的操作
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
try:
<语句>
finally:
<语句>    #退出try时总会执行
raise
    
    """
    try:
        fh = open("testfile","w")
    except IOError:
        print "Error,没有找到文件"
    else:
        print "写入成功"
        fh.flush()
        fh.close()

    exception_param("ss")
