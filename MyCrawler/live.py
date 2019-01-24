#coding:utf-8
# 引入必要的包
import requests
import json
import time
# Url拼接模块
import UrlHandler
# 引入支持循环执行的模块
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# 引入作图模块
import Painter
# 引入文件写入模块
import WriteInXls

# 定义目标Url的参数：
# http://data.live.126.net/partake/usercount/198476.json?callback=liveUsercount
# 200056, 95689
param = {
    'roomid': '200056',
    'callback': 'liveUsercount'
}
filename = "163live"

param['roomid'] = input("请输入直播间的房间号：")

# 拼接请求的目标url
url = UrlHandler.spliceUrl('163live', param)

# 用于存储格式化的数据
data = []
x = []
y = []


def request(url):
    print('\n')

    # 输出期望的请求信息
    print('希望请求的url为：%s \n' % url)

    # 记录抓取时间点
    time_request = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('于【 %s 】开始抓取：\n' % time_request)

    # 执行请求
    _request = requests.get(url)
    print('实际请求的url为：%s' % _request.url)

    # 拿到响应结果
    response = _request.text
    print('响应结果为：%s \n' % response)
    # 截取前缀 'liveUsercount(' 及后缀 ');'
    json_str = response[14:-3]
    # json_str解码为对象
    json_obj = json.loads(json_str)
    print('处理后结果为：%s \n' % json_obj)

    # 存储格式化的数据
    _data = {
        'time': time_request,
        'user_count': json_obj['msg']['user_count'],
        'raw': json_str
    }
    data.append(_data)
    x.append(time_request)
    y.append(json_obj['msg']['user_count'])
    print('当前已存储数据【 %s 】条' % len(data))

    # 将数据写入文件中
    write_res = WriteInXls.writeInXls({
        'filename': filename,
        'id': param['roomid'],
        'data': _data
    })
    print(write_res)

def doit():
    request(url)

# 定义 BlockingScheduler BackgroundScheduler
scheduler = BackgroundScheduler()
job = scheduler.add_job(doit, 'interval', seconds=3)

# 启动后台抓取任务
scheduler.start()
# 启动作图
drawer = Painter.Draw(data, x, y).start().show()
