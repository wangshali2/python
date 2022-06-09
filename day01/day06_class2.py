# self
class MyClass:
    def __init__(self):
        print(1, 'self in init = {}'.format(id(self)))

    def showself(self):
        print(2, 'self in showself() = {}'.format(id(self)))

c = MyClass()
print(3, 'c = {}'.format(id(c)))
print('=' * 30)

c.showself()
print(MyClass.showself)
print(c.showself)

# 类实例化后，得到一个实例对象，调用类方法时，采用 instance.class_method() 的方式,实例对象就会绑定到方法
# self 就是调用者，self 这个名字只是一个惯例，可以修改，但最好不要修改
# 查看打印结果，思考一下代码的执行顺序
