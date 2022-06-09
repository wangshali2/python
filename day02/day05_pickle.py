import pickle

d = dict({"name":"lili","age":18})

# 序列化
#任意对象序列化成一个bytes
print(pickle.dumps(d))

#把序列化后的对象写入文件
f = open("../out/pickle.txt",'wb')
#参数一：要写入的对象， 参数二：写入文件的对象
pickle.dump(d,f)
f.close()


# 反序列化
f2 = open("../out/pickle.txt","rb")
d = pickle.load(f2)
f2.close()
print(d)
print(type(d))


