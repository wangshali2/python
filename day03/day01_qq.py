def checkQQ(str):
    #不管传入的str是否合法，我们假设合法
    result = True

    #寻找条件推翻最初的假设
    try:
        #判断是否是全数字
        num = int(str)

        #判断位数
        if len(str) >= 4 and len(str) <= 11:
            #判断是否以数字0开头
            if str[0] == '0':
                result = False
        else:
            result = False

    except BaseException:
        result = False

    return result

print(checkQQ("1490980"))