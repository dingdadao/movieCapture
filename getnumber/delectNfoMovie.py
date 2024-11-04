# -*- coding: utf-8 -*-
import os
import shutil
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def selectMovie(path: str, year: str):
    file_list = []
    year_pattern = re.compile(r"^\d{4}(-\d{1,2}){0,2}$")
    numid_pattern = re.compile(r"mmgh", re.IGNORECASE)  # 正则匹配 mmgh，不论大小写

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".nfo"):
                file_path = os.path.join(root, file)
                try:
                    tree = ET.parse(file_path)
                    root_element = tree.getroot()

                    # 查找 'numid' 元素
                    numid_element = root_element.find('numid')
                    if numid_element is not None and numid_pattern.search(numid_element.text or ''):
                        print(f"Skipping file {file_path} because 'numid' contains 'mmgh'.")
                        continue

                    # 优先查找 'year' 元素
                    element = root_element.find('year')
                    if element is None:
                        # 如果没有找到 'year' 元素，则查找 'genre' 元素
                        continue

                    if element is not None and element.text and year_pattern.match(element.text):
                        if year <= element.text:
                            current_dir = Path(file_path).resolve().parent
                            file_list.append(str(current_dir))
                            break

                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
                    continue
    return file_list


def deleteDirectories(directories):
    for directory in directories:
        decoded_directory = os.path.abspath(directory)
        print(f"Trying to delete directory: {decoded_directory}")
        path = Path(decoded_directory)

        # 检查目录是否存在
        if path.exists():
            try:
                shutil.rmtree(path)
                print(f"Deleted directory: {path}")
            except Exception as e:
                print(f"Error deleting directory {path}: {e}")
        else:
            print(f"Directory does not exist: {path}")


# 测试路径和年份
movie_directories = selectMovie("/volume2/medie/medies/japan/perfect", "2020-01")
print(f"Directories to be deleted: {movie_directories}")
deleteDirectories(movie_directories)
