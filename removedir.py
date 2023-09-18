import os

import config

def remove_empty_files(folder_path,fil):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) < 51200:
                try:
                    # os.remove(file_path)
                    fil.write(str(file_path))
                    fil.write('/n')
                except:
                    fil.write(str(file_path))
                    fil.write('/n')



if __name__ == '__main__':
    conf = config.getInstance()
    folder_path = conf.source_folder()

    if not os.path.isfile(folder_path + '/test.txt'):
        file = open(folder_path + '/test.txt', 'w')
    else:
        file = open(folder_path + '/test.txt', 'a')

    remove_empty_files(folder_path,file)
    file.close()