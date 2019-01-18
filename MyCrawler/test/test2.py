import os,xlwt
from xlrd import open_workbook
from xlutils.copy import copy

filename = "filename.xls"
if (os.path.exists(filename)==False):
    _file = xlwt.Workbook()
    sheet = _file.add_sheet("111")
    _file.save(filename)

excel = open_workbook(filename)
wexcel = copy(excel)
# wexcel.add_sheet("222")
wexcel.save(filename)

print(dir(excel.sheets()[0]))
print(excel.sheet_names())
rows = excel.sheet_by_name("111").nrows
print(rows)