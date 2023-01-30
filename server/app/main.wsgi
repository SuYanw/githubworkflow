#!/usr/bin/python3.8
import os
import sys
import logging


file = open("/app/.env", "r")
lines = file.readlines()
for line in lines:
    key = line.strip().split("=")[0]
    val = line.strip().split("=")[1]

    os.environ[key] = val



logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/app")

from main import app as application