import os
import string
import subprocess


def make_dir():
    for c in string.ascii_lowercase:
        os.makedirs('train_data/' + c.upper())
        subprocess.check_output('touch train_data/' + c.upper() + "/.gitkeep", shell=True)
    for i in range(10):
        os.makedirs('train_data/' + str(i))


def add_git_keep():
    for c in string.ascii_lowercase:
        subprocess.check_output('touch train_data/' + c.upper() + "/.gitkeep", shell=True)
    for i in range(10):
        subprocess.check_output('touch train_data/' + str(i) + "/.gitkeep", shell=True)


add_git_keep()
