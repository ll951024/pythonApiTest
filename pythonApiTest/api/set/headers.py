import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)
from api.set.logininit import Init
import unittest


class Headers():
    def headers(self):
        return {
            "Authorization": Init.test_userlogin(self),
            "Content-Type":"application/json"
        }







