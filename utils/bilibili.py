import requests
import re
import urllib
import json


class Bilibili:
    def __init__(self, parent):
        self.parent = parent

    def download(self, url):
        try:
            page = requests.get(url=url).content.decode('utf8')                                                 # 获取到播放页面
        except Exception as e:
            print(e)
            return False, "微博页面爬取失败"

        try:
            # 获取到标题和链接
            title = self.parent.basic.sanitize(re.search(r'"content2":\s*"([^"]+)",', page).group(1))
            url = re.findall(r'"mp4_.+?_mp4":\s*"(.+?)"', page)[0]
            content = requests.get(url).content
            return True, (title, content)
        except Exception as e:
            print(e)
            return False, "微博视频爬取失败"
