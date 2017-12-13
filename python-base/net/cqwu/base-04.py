#-*- coding: utf-8 -*-
"""
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量：定义在方法中的变量，只作用于当前实例的类。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

    python对象销毁(垃圾回收)
    Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
    在 Python 内部记录着所有使用中的对象各有多少引用。
    一个内部跟踪变量，称为一个引用计数器。
    当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

    类属性与方法
    类的私有属性
    __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
    类的方法
    在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
    类的私有方法
    __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用

"""
class Employee:
    #mpCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。
    empCount = 0
    #第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self,name,salary):
        #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        #self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def dispayCount(self):
        print "Total Employee %s" % Employee.empCount
    def displayEmployee(self):
        print "Name: " ,self.name, "salary",self.salary
class JustCounter:
    __secretCount = 0 #私有变量
    publicCount = 0 #公开变量
    def count(self):
        self.__secretCount = 10
        self.publicCount = 20
if __name__ == '__main__':
    emp1 = Employee('zp',3200)
    emp2 = Employee('zp',3200)
    emp1.dispayCount()
    #你可以添加，删除，修改类的属：
    emp1.age = 23
    print emp1.age