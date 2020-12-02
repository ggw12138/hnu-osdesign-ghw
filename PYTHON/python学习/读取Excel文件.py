#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import xlrd
wb=xlrd.open_workbook('file.xls')
#获取sheets总数
ws_count=wb.nsheets
print('Sheets总数:',ws_count)
#通过索引顺序获取Sheets
# ws=wb.sheets()[0]
ws=wb.sheet_by_name('Python')
#获取整行内容
row_value=ws.row_values(3)
print('第4行数据:',row_value)
#获取整列的值
row_col=ws.col_values(3)
print('第4列数据',row_col)
#获取总行数和总列数
nrows=ws.nrows
ncols=ws.ncols
print('总行数:',nrows,'总列数:',ncols)
cells=ws.cell(2, 3).value
print(cells)