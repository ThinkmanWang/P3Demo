import pymysql
from DBUtils.PooledDB import PooledDB

from thinkutils.config.Config import *

g_dbPool = PooledDB(pymysql
                    , mincached = int(g_config.get("mysql", "maxconnections")) / 2
                    , maxcached = int(g_config.get("mysql", "maxconnections"))
                    , host=g_config.get("mysql", "host")
                    , user=g_config.get("mysql", "user")
                    , passwd=g_config.get("mysql", "password")
                    , db=g_config.get("mysql", "db")
                    , port=int(g_config.get("mysql", "port"))
                    , maxconnections=int(g_config.get("mysql", "maxconnections"))
                    , charset = "utf8"
                    , use_unicode = True)
