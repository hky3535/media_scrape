import re
import os


class Basic:
    def __init__(self, parent):
        self.parent = parent
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.generate_dir()

    def generate_dir(self):
        if not os.path.exists(f"{self.base_dir}/utils/download_temp"):
            os.mkdir(f"{self.base_dir}/utils/download_temp")

    def sanitize(self, file_name):
        illegal_chars = r'[\/:*?"<>|]'
        emoticons = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]'
        
        pattern = '|'.join((illegal_chars, emoticons))
        return re.sub(pattern, '', file_name)

    def extract_url(self, raw):
        pattern = r'https?://\S+'

        matches = re.findall(pattern, raw)
        if len(matches) == 1:
            return True, matches[0]
        return False, "无法获取有效url"

    def download_to_server(self, identification, source, url):
        if source == "douyin":
            res, content = self.parent.douyin.download(url)
        if source == "weibo":
            res, content = self.parent.weibo.download(url)
        if source == "bilibili":
            pass
        
        if res:
            try:
                save_dir = f"{self.base_dir}/utils/download_temp/[{source}]{content[0]}[{identification}].mp4"
                open(save_dir, "wb").write(content[1])
                return True, content[0]
            except Exception as e:
                return False, "文件写入失败"
        else:
            return False, content
