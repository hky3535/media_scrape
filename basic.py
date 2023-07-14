import re
import os


class Basic:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.generate_dir()

    def generate_dir(self):
        if not os.path.exists(f"{self.base_dir}/download_temp"):
            os.mkdir(f"{self.base_dir}/download_temp")

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
        return False, f"无法获取有效url: {raw}"

    def save(self, source, title, content):
        title = self.sanitize(title)
        try:
            save_dir = f"{self.base_dir}/download_temp/[{source}]{title}.mp4"
            open(save_dir, "wb").write(content)
            return True, save_dir
        except Exception as e:
            return False, "文件写入失败"
