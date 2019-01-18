#coding:utf-8

# 引入支持画图的包
import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style

from matplotlib.widgets import Button

from pyecharts import Line

def drawEchartsLine(title, series_name, xs, ys):
    line = Line(title)
    line.add(series_name, xs, ys)
    line.render()

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 生成画布
fig, [ax_lst] = plt.subplots(1, 1, squeeze=False)  # a figure with a 1x1 grid of Axes
# 设置画布的标题
fig.suptitle('No axes on this figure')
# 调整绘图区域的位置
plt.subplots_adjust(bottom=0.2)

# 绘制图形
ax1 = ax_lst[0] # 拿到坐标系
ax1.set_title("网易直播在线人数") # 设置坐标系的标题
ax1.set_xlabel("Time(s)") # 设置坐标系的横轴标签
ax1.set_ylabel("People(Billion)") # 设置坐标系的纵轴标签
ax1.plot([1,2,3,4], [4,5,3,6]) # 传入数据进行绘图

# 显示图形
plt.show()

