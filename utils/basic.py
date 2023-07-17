"""
何恺悦 hekaiyue 2021-03-14
"""
import re
import os
import requests
import random


class Basic:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.storage_dir = f"{self.base_dir}/storage"
        self.generate_dir(self.storage_dir)

    def generate_dir(self, dir):                # 确保文件下载目录存在
        if not os.path.exists(dir):
            os.mkdir(dir)

    def sanitize(self, file_name):              # 将提取出的带有特殊字符的标题转为文件名
        illegal_chars = r'[\/:*?"<>|]'
        emoticons = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]'
        
        pattern = '|'.join((illegal_chars, emoticons))
        return re.sub(pattern, '', file_name)

    def extract_url(self, input_url):           # 从杂乱的原始分享链接url中提取出实际页面的url
        pattern = r'https?://\S+'

        matches = re.findall(pattern, input_url)
        if len(matches) == 1:
            return True, matches[0]
        return False, f"无法获取有效url：{input_url}"

    def save(self, source, title, media_url):   # 通过媒体的实际url下载文件并保存到本地
        identification_code = ''.join(random.choices('0123456789', k=7))    # 生成七位随机码

        content = requests.get(media_url).content       # 下载文件
        title = self.sanitize(title)                    # 格式化文件名
        try:
            save_dir = f"{self.storage_dir}/[{source}]{title}[{identification_code}].mp4"
            open(save_dir, "wb").write(content)         # 写入本地
            return True, [f"{identification_code}", f"{title}.mp4"]
        except Exception as e:
            return False, f"文件写入失败：{e}"
