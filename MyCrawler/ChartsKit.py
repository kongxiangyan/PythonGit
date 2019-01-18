#coding:utf-8

import math
# 引入支持画图的包 matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import Button
# 引入支持画图的包 pyechartss
from pyecharts import Line

def drawEchartsLine(title, series_name, xs, ys):
    line = Line(title)
    line.add(series_name, xs, ys)
    line.render()

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

class FigureHandler():
    def __init__(self):
        self.plt = plt

    def getFigure(self, suptitle):
        # 生成画布
        fig, [ax_lst] = plt.subplots(1, 1, squeeze=False)  # a figure with a 1x1 grid of Axes
        # 设置画布的标题
        fig.suptitle(suptitle)
        # 调整绘图区域的位置
        plt.subplots_adjust(bottom=0.2)

        self.fig = fig
        self.ax_lst = ax_lst

        return self

    def draw(self, axes_title, axes_xlabel, axes_ylabel, x_data, y_data):
        # 绘制图形
        ax1 = self.ax_lst[0] # 拿到坐标系
        ax1.cla() # 清空画布
        ax1.set_title(axes_title) # 设置坐标系的标题
        ax1.set_xlabel(axes_xlabel) # 设置坐标系的横轴标签
        ax1.set_ylabel(axes_ylabel) # 设置坐标系的纵轴标签
        ax1.plot(x_data, y_data, "o-") # 传入数据进行绘图

        # 隐藏一部分x轴标签，保持在5个左右
        labels = ax1.get_xticklabels()
        for label in labels:
            label.set_visible(False)
        for label in labels[::(math.floor(len(y_data)/5)+1)]:
            label.set_visible(True)
        labels[-1].set_visible(True)

        # plt.gcf().autofmt_xdate() # x轴标签自动旋转

        # 显示图形
        plt.draw()

        return self

# figure = FigureHandler().getFigure("直播在线人数实时抓取呈现").draw("网易直播在线人数", "Time(s)", "People(Billion)", [1,2,3,4], [4,5,3,6])