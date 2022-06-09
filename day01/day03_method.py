# _*_ coding:utf-8 _*_
# @Time : 2021/9/17 15:39
# @Author : wsl
# @File : day03_method
# @Project : python

print('---------------------------String---------------------------------')
s = '美好生活'
a = '我的世界'
c = 'abc'

print(len(c))
print(s.find('好'))  # 找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1
print(s.startswith('我'))  # 判断字符串是不是以谁谁谁开头/结尾
print(s.count('好'))  # 返回 str在start和end之间 里面出现的次数
print(s.count('好', 0, 15))
print(s.replace('好', '坏'))
print(s.split(" "))  # 切割字符串
print(s.lower())
print(len(c.strip()))  #去掉收尾空格
print(s.join(a))  #拼接   我 美好生活 的 美好生活 世 美好生活 界

print('---------------------------列表---------------------------------')

A = ['a', 'b', 'c']
B = ['aa', 'bb', 'cc']

A.append('e')  #在末尾添加元素

A.insert(3, 'F')  #在指定位置插入元素

A.extend(B)  #合并两个列表

# 修改元素
A[0] = 'A'
print('A=%s' % A)

# 查找元素，在 in，不在 not in
if 'A' in A:
    print('找到了')

# 通过下标删除
del A[0]

# 删除最后一个
A.pop()

# 根据元素的值删除
A.remove('aa')

print('---------------------------元祖---------------------------------')
a = ('我的', 77.0)
print(a[0])  # 访问元祖，不能修改元祖
print(a[1])

b = (11,)
print(type(b))

# 切片
print(s[3:7:1])  # 起始 结束 步长

print('---------------------------字典  类似json---------------------------------')
info = {'name': '班长', 'age': 18}
print(info['age'])  # 获取元素
print(info.get('name'))
print(info.get('sex'), '男')  # 获取不存在的元素，给个默认值

print('修改之前的字典为:%s' % info)
info['age'] = 200

del info['name']  # 删除
del info  # 删除整个字典
# info.clear()

info = {'name': '班长', 'age': 18}
# key
for key in info.keys():
    print(key)

# value
for value in info.values():
    print(value)

# 项
for item in info.items():
    print(item)

for key, value in info, item:
    print('key = %s' % key, 'value = %s' % value)
