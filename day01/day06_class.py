# 1.必须使用 class 关键字
# 2.类名必须是用 大驼峰 命名
# 3.类定义完成后，就产生了一个类对象，绑定到了标识符 ClassName 上
# 4.在类对象名称后面加上一个括号，就是调用类的实例化方法,实际上就是调用的 __init__(self) 方法
# 5.类定义中的变量和类中定义的方法都是类的属性

class MyClass:
    """My first class"""
    print('in class')
    xx = 'abc'  # 类的属性

    def __init__(self, x, y):
        print('in init')
        self.x = x
        self.y = y

    def foo(self):
        print('in foo')
        return "My class"

#print(MyClass.xx, MyClass.foo, MyClass.__doc__)
#in class
# abc <function MyClass.foo at 0x000001F015D65378> My first class

myc1 = MyClass(1, 2)
print(myc1.foo())
# in class
# in init
# in foo
# My class

print(MyClass.foo(myc1))
# in foo
# My class