import csv

# 读csv文件
def readCsv(path):
    #列表
    infoList = []
    #以只读的形式打开文件
    with open(path, 'r')  as f:
        #读取文件的内容
        allFileInfo = csv.reader(f)
        #将获取到的内容逐行追加到列表中
        for row in allFileInfo:
            infoList.append(row)
    return infoList

# 加r ：不需要进行转义了
path = r"../out/read.csv"
print(readCsv(path))


# 写入
def writeCsv(path,data):
    with open(path,'w',newline='')  as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData =", rowData)
            #按行写入
            writer.writerow(rowData)

path = r"../out/write.csv"
writeCsv(path,[[1,2,3],[4,5,6],[7,8,9]])