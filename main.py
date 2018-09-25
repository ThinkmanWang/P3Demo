# -*- coding: UTF-8 -*-

from thinkutils.log.log import g_logger
from thinkutils.datetime.datetime_utils import *
from MyTorEchoServer import MyTorEchoServer

if __name__ == '__main__':
    MyTorEchoServer.start_server()