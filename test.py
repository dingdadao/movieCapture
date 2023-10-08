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
    for full_name in source.glob(r'**/*'):
        is_sym = full_name.is_symlink()
        movie_size = 0 if is_sym else full_name.stat().st_size

        if 0 < movie_size < 125829120:
            movie_path = str(os.path.join(full_name))
            try:
                os.remove(movie_path)
            except:
                print("删除失败了奥",movie_path)


main()