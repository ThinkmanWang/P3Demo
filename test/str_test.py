# -*- coding: UTF-8 -*-

import sys
import os

if __name__ == '__main__':
    print(type("测试"))
    print(bytes("测试", encoding="utf-8"))
    print(type(b"123"))
    print(str(b"123", encoding="utf-8"))