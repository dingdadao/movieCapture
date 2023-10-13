import os
import re
import shutil
from pathlib import Path

import config


def mov_Movie():
    conf = config.getInstance()
    source_folder = conf.source_folder()
    check_folder = conf.check_folder()
    file_type = conf.media_type().lower().split(",")

    if not Path(source_folder).is_dir():
        print('[-]Source folder not found!')
        return ""

    source = Path(source_folder).resolve()
    for full_name in source.glob(r'**/*'):
        is_sym = full_name.is_symlink()
        # 调试用0字节样本允许通过，去除小于120MB的广告'苍老师强力推荐.mp4'(102.2MB)'黑道总裁.mp4'(98.4MB)'有趣的妹子激情表演.MP4'(95MB)'有趣的臺灣妹妹直播.mp4'(15.1MB)
        movie_size = 0 if is_sym else full_name.stat().st_size  # 同上 符号链接不取stat()及st_size，直接赋0跳过小视频检测
        if 0 < movie_size < 82428800:  # 1024*1024*120=125829120
            try:
                os.remove(full_name)
                print("删除了小于80m的文件，节约空间")
            except:
                print("删除失败了{0}".format(full_name))

        if not full_name.suffix.lower() in file_type:
            continue
        else:
            print(full_name)
            shutil.move(full_name, check_folder)


if __name__ == '__main__':
    mov_Movie()