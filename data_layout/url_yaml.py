# 解析yaml文件
import os

import yaml

current_path = os.path.dirname(os.path.abspath(__file__))
single_yaml_path = os.path.join(current_path, "data_config.yaml")


class YamlMethods(object):

    def open_read_file(self, path=single_yaml_path):
        """打开文件"""
        with open(path, 'r', encoding='utf-8') as f:
            file_data = f.read()
            return file_data

    def open_write_file(self, path):
        """写入文件"""
        f = open(path, 'w', encoding='utf-8')
        return f

    def single_yaml_load(self):
        """解析单个yaml文档"""
        file_data = self.open_read_file(single_yaml_path)
        data = yaml.safe_load(file_data)
        return data