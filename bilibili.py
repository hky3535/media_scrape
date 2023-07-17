"""
何恺悦 hekaiyue 2021-03-14
"""
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

    def scrape_url(self, url):
        try:
            page = requests.get(url=url, headers=self.headers, cookies=self.cookies).content.decode('utf8')
        except Exception as e:
            return False, f"B站页面爬取失败：{e}"

        try:
            # 获取到标题和链接
            title = re.search(r'<title.*?>(.*?)</title>', page).group(1)
            url = re.findall(r'"baseUrl":"(.*?)"', page)[0]
            return True, (title, url)
        except Exception as e:
            return False, f"B站视频爬取失败：{e}"
