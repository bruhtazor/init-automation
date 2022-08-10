#!/bin/bash

function create () {
    cd ~/root/creating/programming;
    python3 automation_project/main.py $1 
    cd $1
    touch README.md
    git init 
}