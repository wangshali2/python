# _*_ coding:utf-8 _*_
# @Time : 2021/9/17 15:17
# @Author : wsl
# @File : day02_if
# @Project : python


# if
age = 30
if age > 18:
    print('成年了')

if age > 18:
    print('成年了')
else:
    print('未成年')

#elif:当条件A满足时做事情1；当条件A不满足、条件B满足时做事情2；当条件B不满足、条件C满足时做事情3
if age > 5:
    print('A')
elif age > 10:
    print('B')
elif age > 40:
    print('C')

#  for
for s in 'hello':
    print(s)

for i in range(5):  # 0-4
    print(i)

for x in range(10,20,2):#start,end,step
    print(x)