import os

import config


def remove_empty_files():
    conf = config.getInstance()
    folder_path = conf.source_folder()
    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            if os.path.getsize(file_path) == 0:

                pass

                # os.remove(file_path)

            print(os.path.getsize(file_path))





if __name__ == '__main__':
    remove_empty_files()