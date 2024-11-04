import os
import shutil
import configparser
import subprocess
from pathlib import Path

from tqdm import tqdm


def get_video_encoding_info(file_path):
    try:
        ffprobe_cmd = ['/var/packages/ffmpeg5/target/bin/ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of',
                       'json', file_path]
        result = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        if result.returncode == 0 and not result.stderr:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        return False
        print(e)


def find_and_move_video_files():
    try:

        source_folder = "/volume2/medie/medies/downloads"
        target_folder = "/volume2/medie/medies/japan/ok_"
        min_size_bytes = 52000
        file_list = []
        del_dir_list = []
        total_files = sum(len(files) for _, _, files in os.walk(source_folder))
        with tqdm(total=total_files, desc="Sizer", unit="file") as pbar:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    if file.endswith(
                            (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpg", ".mpeg", ".m4v", "iso")):
                        file_path = os.path.join(root, file)
                        if os.path.getsize(file_path) >= min_size_bytes:
                            target_path = os.path.join(target_folder, file)
                            if get_video_encoding_info(file_path):
                                file_list.append([file_path, target_path])
                    pbar.update(1)

        with tqdm(total=len(file_list), desc="moveFile", unit="file") as pbar:
            for movie in file_list:
                shutil.move(movie[0], movie[1])
                current_dir = Path(movie[0]).resolve().parent
                del_dir_list.append(str(current_dir))
                pbar.update(1)

        with tqdm(total=len(del_dir_list), desc="delectFile", unit="file") as pbar:
            exclude = ['downloads','japan','tv']
            for directory in del_dir_list:
                decoded_directory = os.path.abspath(directory)
                path = Path(decoded_directory)
                if str(path).split("/")[-1] in exclude:
                    print(f"Skipping directory: {decoded_directory}")
                    continue
                # 检查目录是否存在
                if path.exists():
                    try:
                        shutil.rmtree(path)
                        pbar.update(1)
                        # print(f"Deleted directory: {path}")
                    except Exception as e:
                        print(f"Error deleting directory {path}: {e}")


    except Exception as e:
        print(f"Error: {e}")
find_and_move_video_files()
