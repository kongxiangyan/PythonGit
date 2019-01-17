
# 引入必要的包
import requests
import json
import time
import UrlHandler
# 引入支持循环执行的模块
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# 支持多线程
from time import sleep
from threading import Thread
# 引入支持画图的包
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import Button

# 定义目标Url的参数：
# http://data.live.126.net/partake/usercount/198476.json?callback=liveUsercount
param = {
    'roomid': '95689',
    'callback': 'liveUsercount'
}

# 拼接请求的目标url
url = UrlHandler.spliceUrl('163live', param)

# 用于存储格式化的数据
data = []
x = []
y = []

# 设置样式
style.use('fivethirtyeight')
# 设置画布
fig, ax = plt.subplots()
# 设置图形显示位置
plt.subplots_adjust(bottom=0.2)
plt.xlabel('Time(s)')
plt.ylabel('Viewers')
plt.title('网易直播某直播间在线人数')

# 自定义类，用来封装两个按钮的单击事件处理函数
class ButtonHandler:
    def __init__(self):
        self.flag = True
        print("初始化制图数据长度为：%s" % len(data))
        self.lastcount = len(data)

    # 线程函数，用来更新数据并重新绘制图形
    def threadStart(self):
        while self.flag:
            sleep(1)
            _len = len(data)
            print("当前数据长度为：【 %s 】, 上次数据长度(lastcount)为：【 %s 】" % (_len, self.lastcount))

            if (self.lastcount > 1):
                x[self.lastcount-1] = ''

            if (_len > self.lastcount):

                for i in range(self.lastcount, _len):
                    # 时间格式转换
                    a = data[i]['time']
                    _timestamp = time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
                    timeTuple = time.localtime(_timestamp)
                    otherTime = time.strftime("%H:%M:%S", timeTuple)

                    x.append(otherTime)
                    y.append(data[i]['user_count'])
                    print(x)
                    print(y)
                print("重置lastcount为：【 %s 】" % _len)
                self.lastcount = _len
                # 重新绘制图形
                ax.clear()
                ax.plot(x, y)

    def Start(self, event):
        self.flag = True
        # 创建并启动新线程
        t = Thread(target=self.threadStart)
        t.start()

    def Stop(self, event):
        self.flag = False


callback = ButtonHandler()

axprev = plt.axes([0.81, 0.05, 0.1, 0.075])
bprev = Button(axprev, 'Stop')
bprev.on_clicked(callback.Stop)
axnext = plt.axes([0.7, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Start')
bnext.on_clicked(callback.Start)


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
    data.append({
        'time': time_request,
        'user_count': json_obj['msg']['user_count'],
        'raw': json_str
    })
    print('当前已存储数据【 %s 】条，详细情况如下：' % len(data))


def doit():
    request(url)

# 定义BlockingScheduler
scheduler = BackgroundScheduler()
job = scheduler.add_job(doit, 'interval', seconds=3)
scheduler.start()
plt.show()