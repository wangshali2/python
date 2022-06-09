# _*_ coding:utf-8 _*_
# @Time : 2021/9/17 17:49
# @Author : wsl
# @File : Urllib
# @Project : python

import urllib.request

# 使用urllib 获取百度首页的源码,前提联网

# 要访问的地址
url = 'http://www.baidu.com'
url_page = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwx3.sinaimg.cn%2Fmw690%2F00266e0Ply1gtqdqyk3sgg60p00jyhdy02.gif&refer=http%3A%2F%2Fwx3.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1634465063&t=94f6adf425a6c7329091d2c492339f2d'
url_video = 'https://s.bdstatic.com/common/openjs/emoticon/box-emoticon.js?_v1631873924784'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 获取相应中的页面的源码,一个字节字节的读取，二进制->string：解码decode
content = response.read().decode('utf-8')

print(content)
print(response)  # HTTPResponse
print(response.getcode())  # 200 逻辑没错
print(response.geturl())
print(response.getheaders())

# 下载网页
urllib.request.urlretrieve(url, '../out/baidu.html')

# 下载图片
urllib.request.urlretrieve(url_page, '../out/lisa.jpg')

# 下载视频  f12 复制src,这个软件不支持打开
urllib.request.urlretrieve(url_video, '../out/lisa.mp4')

# https://www.baidu.com/s?/wd=周杰伦  #
# http/https  www.baidu.com  80/443     s    wd=周杰伦  #
# 协议             主机         端口号   路径  参数     锚点



