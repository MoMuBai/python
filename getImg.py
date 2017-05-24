# coding:utf-8

import urllib
import sys
import re
import os
from importlib import reload


def getHtml(url):
    reload(sys)
    return urllib.urlppen(url).read()
