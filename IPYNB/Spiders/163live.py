#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'IPYNB\Spiders'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## 引入必要的包

#%%
# 请求包
import requests
# json
import json
# 解析包
# from bs4 import BeautifulSoup
# 引入时间相关模块
from datetime import datetime


#%%
# # 要抓取的页面地址
# url= 'http://data.live.126.net/partake/usercount/198455.json?callback=liveUsercount'

# # 获取内容
# response = requests.get(url)

# # 拿到bytes型页面代码
# # html = response.content # or use response.text

# # 解析为utf-8格式文本
# # html = str(html,'utf-8') # html_doc = html.decode("utf-8","ignore")

# print(response.text)

#%% [markdown]
# ## 定义抓取主函数

#%%
def getViewersCount():
    # 直播房间号
    roomid = '198476'

    # 要抓取的页面地址
    url= 'http://data.live.126.net/partake/usercount/' + roomid + '.json?callback=liveUsercount'

    # 获取内容
    response = requests.get(url)

    # 拿到bytes型页面代码
    html = response.content # or use response.text

    # 解析为utf-8格式文本
    html = str(html,'utf-8') # html_doc = html.decode("utf-8","ignore")

    # 截取前缀 'liveUsercount(' 及后缀 ');'
    json_str = html[14:-3]

    # json_str解码
    json_obj = json.loads(json_str)

    # 输出
    res = {
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'value': json_obj['msg']['user_count']
    }
    print(res)
    return res

#%% [markdown]
# ## 定义文件写入函数

#%%
from xlrd import open_workbook
from xlutils.copy import copy

def writeInXls(config):
    filename = config['filename']
    time = config['time']
    value = config['value']

    # 用wlrd提供的方法读取一个excel文件
    rexcel = open_workbook(filename) 

    # 用wlrd提供的方法获得现在已有的行数
    rows = rexcel.sheets()[0].nrows 

    # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    excel = copy(rexcel)

    # 用xlwt对象的方法获得要操作的sheet
    table = excel.get_sheet(0) 
    
    # 标记行数
    row = rows
   
    # xlwt对象的写方法，参数分别是行、列、值
    table.write(row, 0, time)
    table.write(row, 1, value)

    # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    excel.save(filename) 
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#%% [markdown]
# ## 定义运行函数

#%%
def execute():
    res = getViewersCount()
    time = res['time']
    value = res['value']
    
    end = writeInXls({
        'filename': 'data.xls',
        'time': time,
        'value': value
    })
    
    print(end)


#%%
# 引入支持循环执行的模块
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler


#%%
# 定义BlockingScheduler
scheduler = BackgroundScheduler()
# scheduler = BlockingScheduler()
job = scheduler.add_job(execute, 'interval', seconds=3)
scheduler.start()


#%%
job.remove()


#%%



