import numpy as np
import matplotlib.pyplot as plt

# plt.axis([0, 100, 0, 1])
# plt.ion()

# for i in range(100):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.1)


# fig,ax=plt.subplots()
# y1=[]
# for i in range(50):
#     y1.append(i)
#     ax.cla()
#     ax.bar(y1,label='test',height=y1,width=0.3)
#     ax.legend()
#     plt.pause(0.3)

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y1=[30,31,31,32,33,35,35,40,47,62,99,186,480]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y2=[32,32,32,33,34,34,34,34,38,43,54,69,116,271]

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3=[30,31,31,32,33,35,35,40,47,62]

x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y4=[32,32,32,33,34,34,34,34,38,43]
group_labels = ['64k', '128k','256k','512k','1024k','2048k','4096k','8M','16M','32M','64M','128M','256M','512M']
plt.title('broadcast(b) vs join(r)')
plt.xlabel('data size')
plt.ylabel('time(s)')

#plt.plot(x1, y1,'r', label='broadcast')
#plt.plot(x2, y2,'b',label='join')
#plt.xticks(x1, group_labels, rotation=0)

# plt.plot(x3, y3,'r', label='broadcast')
# plt.plot(x4, y4,'b',label='join')
# plt.xticks(x3, group_labels, rotation=0)
plt.plot([[1,2,3],[2,3,4],[3,4,5],[5,100,50],[4,34,23]])
for label in ax1.get_xticklabels():
    label.set_visible(False)
for label in ax1.get_xticklabels()[::(5%5)]:
    label.set_visible(True)
# plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()
x = range(100)
print(x[::2])
print(x[::3])
print(x[10:40:6])


# 时间格式转换
# time = data[i]['time']
# _timestamp = time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
# timeTuple = time.localtime(_timestamp)
# otherTime = time.strftime("%H:%M:%S", timeTuple)

