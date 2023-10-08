import os

import config
from pathlib import Path

def main():
    print("开始了")
    conf = config.getInstance()
    faileds = conf.failed_folder()
    # print(faileds,"faileds-----------")
    if not isinstance(faileds, str) or faileds == '':
        faileds = os.path.abspath(".")

    source = Path(faileds).resolve()
    # print(source,"faileds-------")
    deletelist = []

    for full_name in source.glob(r'**/*'):
        is_sym = full_name.is_symlink()
        movie_size = 0 if is_sym else full_name.stat().st_size

        if 0 < movie_size < 125829120:
            deletelist.append(full_name)

    delete_cont = len(deletelist)
    if delete_cont > 0:
        print("一共发现"+str()+"条需要删除的数据")
    else:
        print("没有需要删除的数据")
        return


    for _ in deletelist:
        movie_path = str(os.path.join(_))
        try:
            os.remove(movie_path)
        except:
            print("删除失败了奥", movie_path)

    print("删除结束")

main()