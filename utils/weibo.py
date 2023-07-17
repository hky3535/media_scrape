"""
何恺悦 hekaiyue 2021-03-14
"""
import requests
import re


class Weibo:
    def __init__(self):
        pass

    def scrape_url(self, url):
        try:
            page = requests.get(url=url).content.decode('utf8')
        except Exception as e:
            return False, f"微博页面爬取失败：{e}"

        try:
            # 获取到标题和链接
            title = re.search(r'"content2":\s*"([^"]+)",', page).group(1)
            url = re.findall(r'"mp4_.+?_mp4":\s*"(.+?)"', page)[0]
            return True, (title, url)
        except Exception as e:
            return False, f"微博视频爬取失败：{e}"
