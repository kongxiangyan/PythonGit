# 自定义类，用来封装两个按钮的单击事件处理函数
class ButtonHandler:
    def __init__(self):
        self.flag = True
        print("初始化制图数据长度为：%s" % len(data))
        self.lastcount = len(data)

    def redraw(self):
        while self.flag:
            sleep(2)
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
                drawEchartsLine("太空", x, y)
                figure.draw("网易直播在线人数", "Time(s)", "People(Billion)", x, y)

    # 线程函数，用来更新数据并重新绘制图形
    def threadStart(self):
        # ani = animation.FuncAnimation(fig, self.redraw, interval=2000)
        self.redraw()

    def Start(self):
        self.flag = True
        # 创建并启动新线程
        t = Thread(target=self.threadStart)
        t.start()

    def Stop(self, event):
        self.flag = False


callback = ButtonHandler()
callback.Start()

# axprev = plt.axes([0.81, 0.05, 0.1, 0.075])
# bprev = Button(axprev, 'Stop')
# bprev.on_clicked(callback.Stop)
# axnext = plt.axes([0.7, 0.05, 0.1, 0.075])
# bnext = Button(axnext, 'Start')
# bnext.on_clicked(callback.Start)