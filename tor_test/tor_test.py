# -*- coding: UTF-8 -*-

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import asyncio
import tornado
import time
from tornado import gen
from thinkutils.log.log import g_logger

@gen.coroutine
def tor_sleep():
    yield gen.sleep(2)
    print("FXXK1")


async def asleep():
    await asyncio.sleep(2)
    print("FXXK2")


async def asleep2():
    print("FXXK2")
    await asyncio.sleep(2)

@asyncio.coroutine
def asleep3():
    yield from asyncio.sleep(2)

async def main(loop):
    asyncio.ensure_future(tor_sleep())
    await asyncio.gather(
        tor_sleep()
        , asleep()
        , loop=loop
    )


if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()