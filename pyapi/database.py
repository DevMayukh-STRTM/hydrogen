import re
import os
import pickle
import sys

import http

from . import exeption

class HydrogenDB:
    def __init__(self, attr):
        if type(attr) == type([]) and len(attr) == 2:
            self.data = attr
        else:
            raise exeption.HydrogenDataError

    