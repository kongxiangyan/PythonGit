
# 引入必要的包
import requests
import json
import time
import UrlHandler

# 定义目标Url的参数：
# http://data.live.126.net/partake/usercount/198476.json?callback=liveUsercount
param = {
    'roomid': '198476',
    'callback': 'liveUsercount'
}

# 拼接请求的目标url
url = UrlHandler.spliceUrl('163live', param)


def request(url):
    # 输出期望的请求信息
    print('希望请求的url为：%s' % url)

    # 记录抓取时间点
    time_request = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('于【 %s 】开始抓取：' % time_request)

    # 执行请求
    _request = requests.get(url)
    print('实际请求的url为：%s' % _request.url)

    # 拿到响应结果
    response = _request.text
    print('响应结果为：%s' % response)
    # 截取前缀 'liveUsercount(' 及后缀 ');'
    json_str = response[14:-3]
    # json_str解码为对象
    json_obj = json.loads(json_str)
    print('处理后结果为：%s' % json_obj)

    # 存储格式化的数据
    data = []
    data.append({
        'time': time_request,
        'user_count': json_obj['msg']['user_count'],
        'raw': json_str
    })
    print('当前已存储数据【 %s 】条，详细情况如下：' % len(data))
    print(data)

request(url)