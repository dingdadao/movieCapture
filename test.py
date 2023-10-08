import os

import config
from pathlib import Path

def main():
    print("开始了")
    conf = config.getInstance()
    faileds = conf.failed_folder()
    if not isinstance(faileds, str) or faileds == '':
        faileds = os.path.abspath(".")

    source = Path(faileds).resolve()

    for full_name in source.glob(r'**/*'):
        print(full_name)



main()