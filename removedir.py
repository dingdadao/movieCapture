import os

import config

def remove_empty_files(fil):
    conf = config.getInstance()
    folder_path = conf.source_folder()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            fil.write(file_path + '/n')
            if os.path.getsize(file_path) < 51200:
                try:
                    os.remove(file_path)
                except:
                    fil.write(os.path.getsize(file_path))



if __name__ == '__main__':

    if not os.path.isfile('./test.txt'):
        file = open('./test.txt', 'w')
    else:
        file = open('./test.txt', 'a')

    remove_empty_files(file)
    file.close()