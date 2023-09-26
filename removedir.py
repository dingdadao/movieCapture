import os

import config

def remove_empty_files(folder_path,fil):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) < 51200:
                file_path_str = file_path.split(".")
                if file_path_str[-1] not in ["torrent","aria2","test","xltd"]:
                    try:
                        os.remove(file_path)
                        # fil.write(str(file_path)+'\n')
                    except:
                        fil.write(str(file_path)+'\n')


        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if os.path.isdir(dir_path):
                dir_path_str = dir_path.split("/")
                if dir_path_str[-1] not in ["download","JAV_output","failed","film","tvplay"]:
                    try:
                        os.rmdir(dir_path)
                        # fil.write(str(dir_path) + '\n')
                    except:
                        fil.write(str(dir_path) + '\n')



if __name__ == '__main__':
    conf = config.getInstance()
    folder_path = conf.source_folder()

    if not os.path.isfile(folder_path + '/test.txt'):
        file = open(folder_path + '/test.txt', 'w')
    else:
        file = open(folder_path + '/test.txt', 'a')

    remove_empty_files(folder_path,file)
    file.close()