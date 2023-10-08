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

    sources = Path(sources).resolve()
    for _ in sources.glob(r'**/*'):
        patha = str(os.path.join(_))
        if os.path.isdir(patha):
            print(patha)
            is_sym = _.is_symlink()
            movie_size = 0 if is_sym else _.stat().st_size
            if movie_size <= 0:
                print(patha,"小于0")


main()