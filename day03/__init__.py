'''
.                匹配除换行符以外的任意字符
[0123456789]     []是字符集合，表示匹配方括号中所包含的任意一个字符
[good]           匹配good中任意一个字符
[a-z]            匹配任意小写字母
[A-Z]            匹配任意大写字母
[0-9]            匹配任意数字，类似[0123456789]
[0-9a-zA-Z]      匹配任意的数字和字母
[0-9a-zA-Z_]     匹配任意的数字、字母和下划线
[^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]           匹配所有的非数字字符
\d               匹配数字，效果同[0-9]
\D               匹配非数字字符，效果同[^0-9]
\w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
\W               匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
\s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
\S               匹配任意的非空白符，效果同[^ \f\n\r\t]

锚字符/边界字符
^     行首匹配，和在[]里的^不是一个意思,"^"要写到字符串的前面
$     行尾匹配,"$"要写到匹配的字符串后面

\A    匹配字符串的开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配其它行的行首
\Z    匹配字符串的结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾

\b    匹配一个单词的边界，也就是值单词和空格间的位置
      'er\b'可以匹配never,不能匹配nerve
\B    匹配非单词边界
'''
import re

print(re.findall("\d", "_sunck is 66a go8od man 3"))
print(re.findall("[A-Z]","_sunck is 66a go8oD man 3"))
print(re.findall("[a-z]","_sunck is 66a go8od man 3"))
print(re.findall("[\S]","_sunck is 66a go8od man 3"))
print(re.findall("[\W]","_sunck is 66a go8od man 3"))



print("*"*20)

print(re.findall("^sunck", "sunck is a good man\nsunck is a nice man", re.M))
print(re.findall("\Asunck", "sunck is a good man\nsunck is a nice man", re.M))
print(re.findall("man$", "sunck is a good man\nsunck is a nice man", re.M))
print(re.findall("man\Z", "sunck is a good man\nsunck is a nice man", re.M))

print(re.search(r"er\b", "never"))
print(re.search(r"er\b", "nerve"))
print(re.search(r"er\B", "never"))
print(re.search(r"er\B", "nerve"))

# 匹配qq邮箱，5~12位，第一位不为0
print(re.findall(r"^[1-9]\d{4,11}@qq\.com$","123456@qq.com"))
print(re.findall(r"^[1-9]\d{4,11}@qq\.com$","0123456@qq.com"))
print(re.findall(r"^[1-9]\d{4,11}@qq\.com$","123456@qq.co"))