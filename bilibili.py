import requests
import re
import urllib
import json

import basic


class Bilibili:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
        }
        self.cookies = {
            'SESSDATA': ''
        }

    def download(self, url):
        try:
            page = requests.get(url=url, headers=self.headers, cookies=self.cookies).content.decode('utf8')                                                 # 获取到播放页面
        except Exception as e:
            return False, "B站页面爬取失败"

        try:
            # 获取到标题和链接
            title = re.search(r'<title.*?>(.*?)</title>', page).group(1)
            url = re.findall(r'"baseUrl":"(.*?)"', page)[0]
            content = requests.get(url).content
            return True, (title, content)
        except Exception as e:
            return False, "B站视频爬取失败"


if __name__ == "__main__":
    url = "随便什么干扰中文或者英文https://www.bilibili.com/video/BVxxxxx/"

    basic = basic.Basic()
    bilibili = Bilibili()

    ret, url = basic.extract_url(url)               # 从输入中抽取到真实页面地址
    assert ret, url; print(f"获取到输入url: {url}")
    
    ret, res = bilibili.download(url)               # 根据页面地址定位到视频真实链接并进行下载
    assert ret, res; print(f"微博视频爬取成功: {res[0]}")
    
    ret, res = basic.save("bilibili", *res)         # 将下载视频保存到本地
    assert ret, res; print(f"微博视频保存成功: {res}")
