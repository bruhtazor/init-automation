import sys
import os

dir_name = sys.argv[1]
parent_dir = os.getcwd()
path = os.path.join(parent_dir, dir_name)

def mkdir(dir_name):
    print("{}".format(dir_name))
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % dir_name)
    else:
        print ("Successfully created the directory %s " % dir_name)


if __name__ == "__main__":
    mkdir(dir_name)