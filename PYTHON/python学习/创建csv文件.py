#-*- encoding:UTF-8 -*-
#誉天暑期训练营
# lst1=["name","age","school","address"]
# filew=open('asheet.csv','w')
# filew.write(",".join(lst1))
# filew.close()
#读取文件里面的内容
filer=open('asheet.csv','r')
line=filer.read()
print(line)
filer.close()
#读取二维数据
datas=[['Name','DEP','Eng','Math','Chinese'],
       ['Rose','法学',89,78,65],['Mike','历史',56,'',44],['John','数学',45,65,67]]
import csv
filename='bsheet.csv'
# with open(filename,'w',newline="") as f:
#     writer=csv.writer(f)
#     for row in datas:
#         writer.writerow(row)

ls=[]
with open(filename,'r')as f:
    reader=csv.reader(f)
    for row in reader:
        print(reader.line_num,row) #行号从1开始
        ls.append(row)
    print(ls)
"""合并两个.txt内容，两个文件的多行内容交替写入文件，如果一个文件内容比较少，则把另一个文件的剩余内容写入结果文件的尾部"""
#定义一个函数
def test(txtFiles):
    with open('result.txt','w',encoding='utf-8')as fp:#创建合并的新文件
        with open(txtFiles[0],encoding='utf-8')as fp1,open(txtFiles[1],encoding='utf-8')as fp2:#读已经存在的两个txt文件
            while True:
                #交替读取文件1和文件2中的行,写入结果文件
                line1=fp1.readline()
                if line1:
                    fp.write(line1)#如果读取到的文件里面有内容，那么就需要把内容写到新创建的文件
                else:
                    #如果文件1结束，结束循环
                    flag=False
                    break
                line2=fp2.readline()
                if line2:
                    fp.write(line2)
                else:
                    #如果文件2结束，结束循环
                    flag=True
                    break
                #获取没有结束的文件对象
            fp3=fp1 if flag else fp2
            #把剩余内容写入结果文件
            for line in fp3:
                fp.write(line)


txtFiles=['test.txt','test1.txt']
test(txtFiles)


