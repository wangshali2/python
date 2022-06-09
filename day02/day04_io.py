from io import StringIO
from io import BytesIO

# 打开或创建一个文件
f = open('../out/1.txt', 'w+')
f.write('我的天空哈哈哈')


# print(f.read(4))
#
# print(f.readlines())

for line in f.readlines():
    print(line.split())  # 去掉换行符


# StringIO读写内存字符串
f = StringIO()
f.write("hello")
f.write("    ")
f.write('world')
# 获取写入后的str
print(f.getvalue())


# BytesIO读写内存二进制
f = BytesIO()
f.write("中文".encode('utf-8'))
print(f.getvalue())


f.close()
