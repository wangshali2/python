# _*_ coding:utf-8 _*_
# @Time : 2021/9/17 16:28
# @Author : wsl
# @File : day04_def
# @Project : 函数


# 全变量
d = 100


# TODO 函数
def f1():
    print('欢迎光临')
    print('2位')
    print(d)


def addnum():
    a = 11  # 局部变量
    b = 22
    c = a + b
    print(c)


# 带参函数
def add2num(a, b):
    print(a,"+",b,"=",a + b)


f1()
addnum()
add2num(11, 22)




