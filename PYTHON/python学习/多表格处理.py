#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import xlrd
import xlsxwriter
import glob
biao_tou='NULL'
wei_zhi='NULL'
#定义一个获取表格的方法
def get_exce():
    global wei_zhi
    wei_zhi=input("请输入Excel文件所在的目录:")
    all_exce=glob.glob(wei_zhi+"*.xls")
    print("该目录下有"+str(len(all_exce))+"个xls文件")
    if(len(all_exce)==0):
        return 0
    else:
        for i in range(len(all_exce)):
            print(all_exce[i])
        return all_exce
#打开文件
def open_exce(name):
    fh=xlrd.open_workbook(name)
    return fh

#获取excel下面所有sheet
def get_sheet(fh):
    sheets=fh.sheets()
    return sheets

#获取sheet下有多少行的数据
def get_sheetrow_num(sheet):
    return sheet.nrows
#获取对应的行数下面的所有的数据
def get_sheet_data(sheet,row):
    for i in range(row):
        if(i==0):
            global biao_tou
            biao_tou=sheet.row_values(i)
            continue
        values=sheet.row_values(i)
        all_data1.append(values)
    return all_data1

if __name__ == '__main__':
    all_exce=get_exce() #调用get_exce的方法获取所有的表格数据
    if(all_exce==0):
        print('该目录下没有.xls文件!请检查您输入的目录是否正确')
        exit()
    #定义用来宝信合并的所有的行的数据
    all_data1=[]
    #开始文件数据的获取
    for exce in all_exce:
        fh=open_exce(exce)
        #获取文件下的sheet数量
        sheets=get_sheet(fh)
        for sheet in range(len(sheets)):
            row=get_sheetrow_num(sheets[sheet])#获取sheet下面所有数据的行数
            all_data2=get_sheet_data(sheets[sheet],row)

    all_data2.insert(0,biao_tou)
    #开始文件的数据写入
    new_exce=wei_zhi+"test.xls"
    #新建一个excel表
    fh1=xlsxwriter.Workbook(new_exce)
    #新建sheet
    new_sheet=fh1.add_worksheet()
    for i in range(len(all_data2)):
        for j in range(len(all_data2[i])):
            c=all_data2[i][j]
            new_sheet.write(i,j,c)
    fh1.close()
    print("文件合并成功，请查看"+wei_zhi+"目录下的test.xls文件")



