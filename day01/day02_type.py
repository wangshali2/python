
# 定义变量,不需要指定类型；数据才有类型；变量没有类型
weather = '下雨了'
print(weather)

# 数据的类型
# 1.numbers
# int
money = 500
# long
# float
money1 = 1.2
# complex

# 2.boolean
sex = True

# 3.string
s = '天黑黑'

# 4.list
name_list = ['天使', '魔鬼']
print(name_list)

# 5.元祖
tuple = (1, 2, 3)
print(tuple)
print(max(tuple))
print(len(tuple))

# 6.字典
info = {'name': '班长', 'age': 18}
print(info.get("name"))
print(info.pop("name"))

# 查看类型
print(type(money))

#查看对象的id
print(id(tuple))

print('----------------------类型转换-------------------------')
# 将()内数据转换为int
print(int(123))
print(int(123.1))
print(int("123"))
print(int(True))
print(int(False))

# 转换成为浮点数
print(float(12))

# 转换成为字符串
str1 = str(123)
print(type(str1))

# 转换成为bool
print(bool(''))
print(bool(0))
print(bool([]))

print('-------------------------运算符-------------------------')
# 逻辑运算符  true and true->true
a = 20
a < 10 or print('python ')  #输出
a > 10 or print('good ')
a > 10 and print('hello ')  #输出
a < 10 and print('world')



