# 引入必要的包
import requests
import json



param1 = {
    'roomid': '198476',
    'callback': 'liveUsercount'
}

# 内置各平台请求url
urls = {
    '163live': {
        'url': ['http://data.live.126.net/partake/usercount/', '_roomid', '.json?callback=', '_callback'] # roomid, callback
    }
}


def spliceUrl(platform, param):
    url_list = urls[platform]['url']
    if not url_list:
        print('检测到目标平台Url数组为空，请正确提供Url模板！')
        return

    len_url_list = len(url_list)
    charat = []

    for i in range(0, len_url_list):
        if url_list[i] == '':
            charat.append(i)

    if not charat:
        print('Url无需填充参数！')
        return
    else:
        for i in range(0, len(charat)):
            url_list[charat[i]] = param[i]
        print(''.join(url_list))

spliceUrl('163live', param1)