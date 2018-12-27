
# 内置各平台请求url
urls = {
    '163live': {
        'url': ['http://data.live.126.net/partake/usercount/', '_roomid_', '.json?callback=', '_callback_'] # roomid, callback
    }
}

def spliceUrl(platform, parameters):
    if not (platform in urls.keys()):
        print('未检测到内置【 %s 】的Url模板！' % platform)
        return

    # 暂存Url模板
    url_frags = urls[platform]['url']

    if not url_frags:
        print('检测到【 %s 】的Url模板为空，请修正！' % platform)
        return

    # Url模板包含的片段数量
    len_url_frags = len(url_frags)

    # 初始化Url模板的参数信息字典
    _parameters = {
        'index': [],
        'parameter_name': [],
        'len': 0
    }

    # 写入目标Url模板的参数信息
    for i in range(0, len_url_frags):
        item = url_frags[i]
        if item.startswith('_') and item.endswith('_'):
            _parameters['index'].append(i)
            _parameters['parameter_name'].append(item[1:-1])
            _parameters['len'] += 1

    # 填充模板
    if not _parameters['len']:
        print('该Url模板无需填充参数！')
    else:
        for i in range(0, _parameters['len']):
            url_frags[_parameters['index'][i]] = parameters[_parameters['parameter_name'][i]]

    # 返回拼接完成的Url
    return ''.join(url_frags)
