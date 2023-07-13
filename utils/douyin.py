import requests
import re
import urllib
import json


class Douyin:
    def __init__(self, parent):
        self.parent = parent
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'cookie': 'cookie: douyin.com; ttwid=1%7CItNlMCU7XA1dzJ9JAfTYqyN3USS6C6uA6qsKkTJIA6c%7C1657586709%7Ca79b507f07e9bcb5abfffb06464d0d52e27bbec7b9f5486adba85f422bb0807d; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=1657586711.076; s_v_web_id=verify_l5hgbw04_lpTAiRhv_vQC7_4AIj_96aY_8ZoIWVk23QTN; passport_csrf_token=7af7437a540d0d5cc283723636e4587d; passport_csrf_token_default=7af7437a540d0d5cc283723636e4587d; douyin.com; ttcid=31a9b5634fc345d5b4093ff39468684d19; THEME_STAY_TIME=%22299807%22; IS_HIDE_THEME_CHANGE=%221%22; pwa_guide_count=%223%22; tt_scid=OZe3.Wjx-I1ER.n9xIU9lv3n4nNHrMUKcBzQvXLhWI6Upp7AFiw8-.l0O8i6bs5Pd3b9; msToken=vbkXsGQvVg8LNHWnXJC_i7vLlFGAVaQGb-5SlXumYncK-p7sFf1iSRL2Rm794Xt8aHeh3U2VXnr3r8TawYbQQNJpon-zsapnDQYzVfRpPrE3OvKpTle4OCqHjDIHrB8=; msToken=5u6A2XAWnny4DUk5dAdPPbhJv_mlazQUkBKg6DbVQLp_7ZoKB9ff_gG1NRgHUWL34lR8cT5jABIAA3NsnkSg4vKBDN3NNRedxmuRL6RQyXkYETwsxSJsnSug4VtdaoQ=; __ac_nonce=062ccf5a5006526b92e98; __ac_signature=_02B4Z6wo00f01K9lC3wAAIDAL2fxPy86hmSvRQ.AAEka9Ue40fx5.YjdUUDYmtadVC-ST9OAPlpAZRGfIGzxYSfqE2Ow3YRHrCSjbTqGz6a5-He0pfl956i951KWXbb-USn2cO6zUlg074pufd; __ac_referer=https://www.douyin.com/video/7118292929868811527'
        }

    def download(self, url):
        try:
            page = requests.get(url=url, headers=self.headers, allow_redirects=False).content.decode('utf8')    # 获取页面重定向
            serial = re.search(r'video/(\d+)/', page).group(1)                                                  # 获取到真实的视频序列号
            url = f"https://www.douyin.com/video/{serial}"                                                      # page_type = video/note
            page = urllib.parse.unquote(requests.get(url=url, headers=self.headers).content.decode('utf8'))     # 获取到真实播放页面
        except Exception as e:
            return False, "抖音页面爬取失败"

        try:
            # 匹配页面内容抽出json部分
            title_url_json = json.loads(re.search(r'<script id="RENDER_DATA" type="application/json">(.*?)</script>', page, re.DOTALL).group(1))
            title_url_json = title_url_json[[s for s in list(title_url_json.keys()) if len(s) > 20 and all(c.isalnum() for c in s)][0]]
            # 获取到标题和链接
            title = self.parent.basic.sanitize(title_url_json["aweme"]["detail"]["desc"])
            url = "https:" + title_url_json["aweme"]["detail"]["video"]["playAddr"][0]["src"]
            content = requests.get(url).content
            return True, (title, content)
        except Exception as e:
            return False, "抖音视频爬取失败"
