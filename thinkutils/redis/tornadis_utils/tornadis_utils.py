
from tornadis.client import *
from tornadis.pool import *
from thinkutils.config.Config import *

g_tornadis_pool = ClientPool(max_size=1024, host=g_config.get("redis", "host"), port=int(g_config.get("redis", "port")), password=g_config.get("redis", "password"), db=int(g_config.get("redis", "db")), autoconnect=True)
