import os
import shutil
import configparser
import subprocess
from tqdm import tqdm


def get_video_encoding_info(file_path):
    try:
        ffprobe_cmd = ['/var/packages/ffmpeg6/target/bin/ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of',
                       'json', file_path]
        result = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        if result.returncode == 0 and not result.stderr:
            return result.stdout.decode('utf-8')
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(e)


def find_and_move_video_files(config_file):
    try:
        config = configparser.ConfigParser()
        config.read(config_file)

        source_folder = config.get('source', 'folder_path')
        target_folder = config.get('target', 'folder_path')
        min_size_bytes = config.getint('target', 'min_size_bytes')
        file_list = []
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
                pbar.update(1)

    except Exception as e:
        print(f"Error: {e}")

config_file = '/volume3/docker/mobile_media_file_config.ini'
find_and_move_video_files(config_file)
