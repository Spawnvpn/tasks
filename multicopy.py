import json
import os
import shutil
from multiprocessing import Pool
import time


def copy_files(file):
    try:
        shutil.copy(file, to_dir)
        print("profit")
        time.sleep(3)
    except IsADirectoryError:
        return


if __name__ == '__main__':
    if input("Load quantity of processes? Y / N ") == "Y":
        f = open("number_of_processes.txt", 'r')
        n_processes = json.load(f)
    elif input("Enter quantity of processes? Y / N ") == "Y":
        n_processes = input(int("Input quantity of processes: "))
    else:
        n_processes = 3

    from_dir = input("Enter the directory from to copy: ")
    to_dir = input("Enter the directory in which to copy: ")

    pool = Pool(n_processes)
    pool.map(copy_files, os.listdir(path=from_dir))
    pool.close()
    pool.join()

    if input("Save quantity of processes? Y / N ") == "Y":
        f = open("number_of_processes.txt", 'w')
        json.dump(n_processes, f)
        f.close()
