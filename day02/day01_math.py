import math
import random
import os
import sys


num=12.345
print(math.ceil(num))
print(math.modf(num))

#随机选择元素
print(random.choice(['hello',True,[1,4,5]]))
#start end step
print(random.randrange(80,100,2))
#[0,1)
print(random.random())
#随机排序
list=[1,3,4,2,6,5]
print(random.shuffle(list))# 返回结果为None
print(list)


#pwd
print(os.getcwd())
#列出目录下所有文件  返回list
print(os.listdir("d:\logs"))
print(os.path.abspath("../day01"))



#实现从程序外部向程序传递参数,返回list
print(sys.argv)
sys.argv[0]

#获取当前执行环境的平台
print(sys.platform)
print(sys.path)


