"""
何恺悦 hekaiyue 2021-03-14
"""
import requests
import re

import basic


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


if __name__ == "__main__":
    url = "随便什么干扰中文或者英文http://m.weibo.cn/status/xxxxx?"

    basic = basic.Basic()
    weibo = Weibo()

    ret, url = basic.extract_url(url)               # 从输入中抽取到真实页面地址
    assert ret, url; print(f"获取到输入url：{url}")
    
    ret, res = weibo.scrape_url(url)                # 根据页面地址定位到视频真实链接并进行下载
    assert ret, res; print(f"微博视频爬取成功：{res[0]}")
    
    ret, res = basic.save("weibo", *res)            # 将下载视频保存到本地
    assert ret, res; print(f"微博视频保存成功：{res}")
