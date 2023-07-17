"""
何恺悦 hekaiyue 2021-03-14
"""
from utils import basic

from utils import douyin
from utils import weibo
from utils import bilibili


class Main:
    def __init__(self):
        self.basic = basic.Basic()
        self.douyin = douyin.Douyin()
        self.weibo = weibo.Weibo()
        self.bilibili = bilibili.Bilibili()
        
        self.source = {
            "douyin": self.douyin,
            "weibo": self.weibo,
            "bilibili": self.bilibili
        }

    def main(self):
        # 输入下载源和原始分享链接
        source = "douyin"
        input_url = ""

        ret, page_url = self.basic.extract_url(input_url)
        if not ret:
            return {"ret": ret, "res": page_url}
        
        ret, media_info = self.source[source].scrape_url(page_url)
        if not ret:
            return {"ret": ret, "res": media_info}
        
        ret, download_info = self.basic.save(source, *media_info)
        if not ret:
            return {"ret": ret, "res": download_info}
        
        return {"ret": ret, "res": download_info}


if __name__ == "__main__":
    print(Main().main())