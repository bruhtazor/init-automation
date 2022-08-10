import sys
import os
from github import Github
from configparser import ConfigParser

#elements from config.ini file
file = "config.ini"
config = ConfigParser()
config.read(file)

#variables used for the directory creation
dir_name = sys.argv[1]
parent_dir = os.getcwd()
path = os.path.join(parent_dir, dir_name)

#variables used for github access
ACCESS_TOKEN = config[Settings][access_token]
LOGIN = Github(ACCESS_TOKEN)
USER = LOGIN.get_user()

def create(dir_name):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % dir_name)
    else:
        print ("Successfully created the directory %s " % dir_name)
    USER.create_repo(dir_name)


if __name__ == "__main__":
    create(dir_name)