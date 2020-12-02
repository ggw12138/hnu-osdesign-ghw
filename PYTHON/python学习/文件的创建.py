#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import xlwt
#新建一个Excel文件
wb=xlwt.Workbook()
#新建一个Sheet
ws=wb.add_sheet('Python',cell_overwrite_ok=True)
#定义字体对齐方式对象
alignment=xlwt.Alignment()
#设置水平方向
alignment.horz=xlwt.Alignment.HORZ_CENTER
#设置垂直方向
alignment.vert=xlwt.Alignment.VERT_CENTER
#定义格式对象
style=xlwt.XFStyle()
style.alignment=alignment
#合并单元格ws.write_merge(开始行,结束行,开始列,结束列,内容,格式)
ws.write_merge(0,0,0,5,'Python暑期训练营',style)
#写入数据
for i in range(2,7):
    for k in range(5):
        ws.write(i,k,i+k)#行，列，内容

#保存文件
wb.save('file.xls')
"""创建Excel的思路是:1.xlwt创建生成临时Excel对象;
2.添加Worksheets对象；3.单元格的位置由行列索引决定，索引从0开始
4.数据写入主要由write_merge()和write()实现，两个分别是合并单元格再写入和单元格写入
5.设置数据格式是在写入(write_merge()和write()实现)的数据中传入参数style,运行程序
"""
