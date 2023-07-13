"""
何恺悦 hekaiyue 2023-07-13
"""
from utils.basic import Basic
from utils.douyin import Douyin
from utils.weibo import Weibo
from utils.bilibili import Bilibili

class Main:
    def __init__(self):
        self.basic = Basic(self)
        self.douyin = Douyin(self)
        self.weibo = Weibo(self)
        self.Bilibili = Bilibili(self)

    def scrape_download(self, identification, source, url):

        res, content = self.basic.extract_url(url)   
        if not res: return JsonResponse({"res": res, "content": content})
        # res: False, content: f"无法获取有效url"
        # res: True, content: f"{url}"

        res, content = self.basic.download_to_server(identification, source, content)
        if not res: return JsonResponse({"res": res, "content": content})
        # res: False, content: f"{error_type}"
        # res: True, content: f"{文件名称}"

        return {"res": res, "content": content}

if __name__ == "__main__":
    identification = "0123456"      # 这个不重要，主要是为了对齐online_toolkit里的函数
    source = [
        "douyin", 
        "weibo", 
        "bilibili"
    ][0]                            # 选择要下载的源
    url = ""                        # 请填写url

    result = Main().scrape_download(identification, source, url)
    print(result)
