
# 引入必要的包
import requests
import json
import UrlHandler



param = {
    'roomid': '198476',
    'callback': 'liveUsercount'
}

res = UrlHandler.spliceUrl('163live', param)

print(res)