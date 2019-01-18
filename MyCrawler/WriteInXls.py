#coding:utf-8
import os
from xlutils.copy import copy
from xlrd import open_workbook
import xlwt
# 引入时间相关模块
from datetime import datetime

def writeInXls(config):
    filename = config['filename'] + ".xls"
    id = config['id']
    time = config['data']['time']
    user_count = config['data']['user_count']
    raw = config['data']['raw']


    if (os.path.exists(filename)==False):
        print("目标文件【 %s 】不存在，尝试进行创建……" % filename)
        _file = xlwt.Workbook()
        sheet = _file.add_sheet(id)
        _file.save(filename)
        print("创建目标文件【 %s 】成功！" % filename)

    # 用wlrd提供的方法读取一个excel文件
    rexcel = open_workbook(filename)

    # 读取目标excel文件的Sheets列表
    rexcel_names = rexcel.sheet_names()

    # 检测目标Sheet是否存在
    if ( id not in rexcel_names):
        print("目标Sheet【 %s 】不存在，尝试进行创建……" % id)
        _excel = copy(rexcel)
        _excel.add_sheet(id)
        _excel.save(filename)
        print("目标Sheet【 %s 】创建成功！" % id)

    rexcel2 = open_workbook(filename)
    # 用wlrd提供的方法获得现在已有的行数
    rows = rexcel2.sheet_by_name(id).nrows

    rexcel_names = rexcel2.sheet_names()

    # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    wexcel = copy(rexcel2)
    print("当前操作的目标Sheet索引为【 %s 】" % rexcel_names.index(id))
    # 用xlwt对象的方法获得要操作的sheet
    table = wexcel.get_sheet(rexcel_names.index(id))

    # 标记行数
    row = rows

    if ( row==0 ):
        table.write(row, 0, "time")
        table.write(row, 1, "user_count")
        table.write(row, 2, "raw")
        row+=1

    # xlwt对象的写方法，参数分别是行、列、值s
    table.write(row, 0, time)
    table.write(row, 1, user_count)
    table.write(row, 2, raw)

    # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    wexcel.save(filename)
    return ("数据写入【 %s 】文件Sheet【 %s 】成功：" % (filename, id)) + datetime.now().strftime("%Y-%m-%d %H:%M:%S")