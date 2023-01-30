#!/usr/bin/python3.8
import os
import sys
import logging

os.environ['SQL_HOST'] = "asdasd"

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/app")

from main import app as application