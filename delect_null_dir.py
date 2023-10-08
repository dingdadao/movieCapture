import os
from pathlib import Path

import config


def main():
    print("开始了")
    conf = config.getInstance()
    sources = conf.source_folder()
    # print(faileds,"faileds-----------")
    if not isinstance(sources, str) or sources == '':
        sources = os.path.abspath(".")
    delect_dir = []
    sources = Path(sources).resolve()
    for _ in sources.glob(r'**/*'):
        patha = str(os.path.join(_))
        if os.path.isdir(patha):
            is_sym = _.is_symlink()
            movie_size = 0 if is_sym else _.stat().st_size
            if movie_size <= 204800:
                delect_dir.append(patha)


    delete_cont = len(delect_dir)
    if delete_cont > 0:
        print("一共发现" + str(delete_cont) + "条需要删除的数据")
    else:
        print("没有需要删除的数据")
        return
    print(delect_dir)
    for _ in delect_dir:
        try:
            os.removedirs(_)
        except:
            print("删除失败",_)

    print("删除完成")


main()