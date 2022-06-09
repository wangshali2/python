# _*_ coding:utf-8 _*_
# @Time : 2021/9/17 17:49
# @Author : wsl
# @File : Urllib
# @Project : python

import urllib.request

# https://www.baidu.com/s?/wd=周杰伦  #
# http/https  www.baidu.com  80/443     s    wd=周杰伦  #
# 协议             主机         端口号   路径  参数     锚点


# UA反扒，爬取结果内容很少
url = 'https://www.baidu.com'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
# print(content)

# UA：f12（右键检查）-network-第一个位置访问的网址-headers-最下面UA

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36"
}

# 解决：请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
response2 = urllib.request.urlopen(request)
content2 = response2.read().decode('utf-8')
print(content2)

