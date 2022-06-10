"""
分析：
1.全数字
2.位数：11位
3.开头只能是1
4.第二位可以为3，4，5，6，7，8
"""
def checkPhone(str):
    result = True

    try:
        #判断是否是全数字
        int(str)
        #判断位数
        if len(str) == 11:
            #判断开头是否为1
            if str[0] == '1':
                #判断第二位的数字
                if str[1] != '3' and str[1] != '4' and str[1] != '5' and str[1] != '6' and str[1] != '7' and str[1] != '8':
                    result = False
            else:
                result = False
        else:
            result = False

    except BaseException:
        result = False

    return  result

print(checkPhone("18501970795"))