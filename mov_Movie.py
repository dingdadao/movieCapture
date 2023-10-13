import os
import re
import shutil
import threading
from pathlib import Path

import config


def mov_Movie():

    movie_list = []
    conf = config.getInstance()
    source_folder = conf.source_folder()
    check_folder = conf.check_folder()
    file_type = conf.media_type().lower().split(",")

    if not Path(source_folder).is_dir():
        print('[-]Source folder not found!')
        return ""

    source = Path(source_folder).resolve()
    for full_name in source.glob(r'**/*'):

        if full_name.is_dir():
            continue
        # 要移动的目的地是否有，有就删除
        failed_name = os.path.join(check_folder, os.path.basename(full_name))
        if not full_name.suffix.lower() in file_type:
            continue
        else:
            print(full_name)
            is_sym = full_name.is_symlink()
            # 调试用0字节样本允许通过，去除小于120MB的广告'苍老师强力推荐.mp4'(102.2MB)'黑道总裁.mp4'(98.4MB)'有趣的妹子激情表演.MP4'(95MB)'有趣的臺灣妹妹直播.mp4'(15.1MB)
            movie_size = 0 if is_sym else full_name.stat().st_size  # 同上 符号链接不取stat()及st_size，直接赋0跳过小视频检测
            if 0 < movie_size < 82428800:  # 1024*1024*120=125829120
                try:
                    os.remove(full_name)
                    print("删除了小于80m的文件，节约空间")
                    continue
                except:
                    print("删除失败了{0}".format(full_name))
            if os.path.exists(failed_name):
                print('[-]移动到未识别文件夹，已经存在')
                try:
                    os.remove(full_name)
                    print('[-] 删除掉重复文件，优化空间 ')
                    continue
                except Exception as e:
                    print("删除重复文件报错了{0}".format(e))
            else:
                movie_list.append(str(full_name))

    return movie_list







# print(movielist)
# semaphore = threading.Semaphore(4)

import asyncio
import aiofiles
import shutil

async def move_file(source_path, destination_path):
    async with aiofiles.open(source_path, 'rb') as source_file:
        async with aiofiles.open(destination_path, 'wb') as destination_file:
            while True:
                chunk = await source_file.read(1024)
                if not chunk:
                    break
                await destination_file.write(chunk)

    print(f"Moved file from {source_path} to {destination_path}")

async def main():
    file_paths = mov_Movie()
    conf = config.getInstance()
    check_folder = conf.check_folder()

    tasks = []
    for file_path in file_paths:
        destination_path = check_folder + file_path.split("/")[-1]
        task = asyncio.create_task(move_file(file_path, destination_path))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print("All files have been moved")

asyncio.run(main())