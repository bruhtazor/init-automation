#!/bin/bash

function create () {
    cd ~/root/creating/programming;
    python3 automation_project/main.py $1 
    cd $1
    git init
    git remote add origin git@github.com:<your username>/$1.git
    touch README.md
    git add .
    git commit -m "inital commit"
    git push --set-upstream origin master
    code .
}