# 支持多线程
from time import sleep
from threading import Thread
# 引入支持画图的模块
import ChartsKit

class Draw():
    # 初始化实例
    def __init__(self, data, x, y):
        self.figure = ChartsKit.FigureHandler().getFigure("直播在线人数实时抓取呈现")
        self.data = data
        self.x = x
        self.y = y
        print("初始化制图数据长度为：%s" % len(data))
        self.lastcount = len(data)

    # 处理数据并调用绘图程序
    def __draw(self):
        while True:
            sleep(2)
            _len = len(self.data)
            print("当前数据长度为：【 %s 】, 上次数据长度(lastcount)为：【 %s 】" % (_len, self.lastcount))

            # if (_len > self.lastcount):
            #     for i in range(self.lastcount, _len):
            #         self.x.append(self.data[i]['time'])
            #         self.y.append(self.data[i]['user_count'])

            # 重新绘制图形
            ChartsKit.drawEchartsLine("网易直播某直播间在线人数", "太空", self.x, self.y) # Echarts
            self.figure.draw("网易直播在线人数", "Time(s)", "People(人)", self.x, self.y) # matplotlib

            print("重置lastcount为：【 %s 】" % _len)
            self.lastcount = _len

    # 实例启动方法
    def start(self):
        t = Thread(target=self.__draw)
        t.start()
        return self

    # 绘图后续，显示画图程序会阻塞进程，确保最后手动执行
    def show(self):
        self.figure.plt.show()
        return self