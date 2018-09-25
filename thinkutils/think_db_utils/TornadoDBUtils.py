#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from tornado import ioloop, gen
from tornado_mysql import pools
import tornado.web
from thinkutils.common_utils.object2json import *
from thinkutils.log.log import *
from thinkutils.config.Config import *
import tornado_mysql.cursors
import copy
import threading

class TornadoDBUtils(object):

    MYSQL_POOL = pools.Pool(dict(host=g_config.get("mysql", "host")
                                 , port=int(g_config.get("mysql", "port"))
                                 , user=g_config.get("mysql", "user")
                                 , passwd=g_config.get("mysql", "password")
                                 , db=g_config.get("mysql", "db"), charset="utf8")
                            , max_idle_connections=16,
                            max_open_connections=int(g_config.get("mysql", "maxconnections")))

    @gen.coroutine
    def query_db(self, query, args=None):
        conn = yield TornadoDBUtils.MYSQL_POOL._get_conn()
        try:
            cur = conn.cursor(tornado_mysql.cursors.DictCursor)
            yield cur.execute(query, args)
        except:
            TornadoDBUtils.MYSQL_POOL._close_conn(conn)
            raise gen.Return(None)
        else:
            TornadoDBUtils.MYSQL_POOL._put_conn(conn)

        raise gen.Return(cur)

g_tornado_db_util = TornadoDBUtils()