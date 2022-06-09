import json

dict1 = {"name":"lili","age":18}
ji = json.dumps(dict1)
print(type(ji))

with open("../out/json","w") as f:
    json.dump(dict1,f)

with open("../out/json","r",encoding="utf-8") as f:
    du = json.load(f)
    print(du)
    print(type(du))

print('---------------------------------------------------')

# 将一个class对象序列化为json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 将student对象转换为dict
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
# 参数一：要传入的对象  参数二：将对象转为dict的函数
d = json.dumps(s, default=student2dict)

# 将dict转为对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

jsonStr = '{"age": 20, "score": 88, "name": "Bob"}'
# json反序列化为一个对象
# 参数一：json字符串，参数二：dict转为对象的函数
print(json.loads(jsonStr, object_hook=dict2student))

# 写入文件
with open("t1.txt","w") as f:
    f.write(d)

# 读取文件
with open("t1.txt","r",encoding="utf-8") as f:
    du = json.load(f,object_hook=dict2student)
print(du)