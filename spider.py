# %% [markdown]
# # 样例1 1- 爬取中国传媒大学百度贴吧帖子信息

# %%
# 例子1
# 爬取中国传媒大学百度贴吧帖子信息嗯

from pyecharts import Line
import pandas as pd
import time
import random
import requests
from bs4 import BeautifulSoup

count = 1

for page in range(0, 401, 50):
    response = requests.get(
        'http://tieba.baidu.com/f?kw=%E4%BC%A0%E5%AA%92%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='+str(page))
    html = response.text

    bs = BeautifulSoup(html)
    posts = bs.select('div.t_con')

    post_url_prefix = 'http://tieba.baidu.com'

    for post in posts:
        print(count)
        count += 1

        reply_num = post.select('.threadlist_rep_num')
        reply_num = reply_num[0].text.strip()
        print('帖子回复数：' + reply_num)

        threadlist_title = post.select('.threadlist_title')
        threadlist_title = threadlist_title[0].text.strip()
        print('帖子标题：' + threadlist_title)

        url = post.select('a.j_th_tit')
        url = post_url_prefix + url[0].get('href').strip()
        print('帖子链接：' + url)

        author_name = post.select('.frs-author-name')
        author_name = author_name[0].text.strip()
        print('帖子发布者：' + author_name)

        with open('2.1_tieba.txt', mode='a', encoding='utf-8') as fin:
            fin.write(threadlist_title+','+url+',' +
                      reply_num+','+author_name+'\n')
        print('=======================================================================================================================================')

# %% [markdown]
# ---
# %% [markdown]
# # 样例2 - 爬取新发地菜市场发布的每日价格行情

# %%
# coding: utf-8
# @Author  : P.C.
# @Email   : panchengbj@126.com
# @File    : main.py
# @Software: PyCharm
# @Intro   : 本程序是爬取新发地菜市场发布的每日价格行情


TYPE = 2  # 商品类型
PAGE = 200  # 爬取的网页数量

if __name__ == '__main__':
    for page_num in range(1, PAGE + 1):
        print('['+str(page_num)+'/'+str(PAGE)+']')

        # 获取网页内容
        url = 'http://www.xinfadi.com.cn/marketanalysis/' + \
            str(TYPE) + '/list/' + str(page_num) + '.shtml'
        html = ''
        try:
            html = requests.get(url=url).content
            time.sleep(random.random())
        except Exception as e:
            print(e)

        # 分析爬取的网页源代码，获取数据
        bs = BeautifulSoup(html)
        infos = bs.find(name='table', class_='hq_table').find_all('tr')
        for i in range(1, len(infos)):
            info = infos[i].find_all('td')
            name = info[0].text
            price_avg = info[2].text
            date = info[6].text
            with open('2.1_xfd.txt', mode='a', encoding='utf-8') as fin:
                fin.write(name + ',' + date + ',' + price_avg + '\n')
                print(name, price_avg, date)
    print('done.')


# %%
# coding: utf-8
# @Author  : P.C.
# @Email   : panchengbj@126.com
# @File    : show.py
# @Software: PyCharm
# @Intro   : 展示爬取的数据 http://pyecharts.org


NAME_LIST = ['木瓜', '板栗', '火龙果', '冬枣']  # 展示的商品名

if __name__ == '__main__':
    info_list = []
    chart = Line(title="水果价格折线图", subtitle='单位 斤/元')
    for i in range(len(NAME_LIST)):
        info_df = pd.read_csv('2.1_xfd.txt', names=[
                              'name', 'date', 'price_avg'], index_col='name')
        sub_info_df = info_df.loc[NAME_LIST[i]]
        info_list.append(sub_info_df)
        chart.add(name=NAME_LIST[i], x_axis=sub_info_df.date,
                  y_axis=sub_info_df.price_avg)
    chart.render('2.1_xfd_result.html')
    print('done.')
