#!/usr/bin/python3.8
import sys
import logging


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/app")

from main import app as application