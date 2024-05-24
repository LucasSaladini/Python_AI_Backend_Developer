import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent 

os.mkdir(ROOT_PATH / 'new_dir')

file = open(ROOT_PATH / 'new_file.txt', 'w')
file.close()

os.rename(ROOT_PATH / 'new_file.txt', ROOT_PATH / 'modified_file.txt')

os.remove(ROOT_PATH / 'modified_file.txt')

file = open(ROOT_PATH / 'new.txt', 'w')
file.close()

shutil.move(ROOT_PATH / 'new.txt', ROOT_PATH / "new_dir" /"new.txt")