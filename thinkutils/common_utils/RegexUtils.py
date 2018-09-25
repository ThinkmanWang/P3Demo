#!/usr/bin/python
#coding=utf-8

import re

class RegexUtils(object):

    @classmethod
    def isMobile(cls, szPhone):
        m = re.findall("^((17[0-9])|(14[0-9])|(13[0-9])|(15[0-9])|(18[0-9]))\\d{8}$", szPhone)
        if m:
            return True

        return False

# print RegexUtils.isMobile("123456")