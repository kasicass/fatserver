#!/bin/bash

SERVER_ROOT=$(pwd)
PROJECT_NAME=alogger

export FAT_SERVER_PATH=$SERVER_ROOT/fatserver
export PROJECT_PATH=$SERVER_ROOT/examples/$PROJECT_NAME
export PYTHONPATH=$FAT_SERVER_PATH/Lib:$FAT_SERVER_PATH:$PROJECT_PATH

python2.7 $PROJECT_PATH/main.py
