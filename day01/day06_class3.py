# 实例变量和类变量
# 实例变量是每一个实例自己的变量，是自己独有的
# 类变量是类的变量，是类的所有实例共享的属性和方法

class Person:
    age = 3
    def __init__(self, name):
        self.name = name

tom  = Person('Tom')
jerry = Person('Jerry')
print(tom.name, jerry.name)
print(tom.age, jerry.age)
print(Person.age)
Person.age = 30
print(Person.age,  tom.age, jerry.age)
