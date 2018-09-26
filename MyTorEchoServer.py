# -*- coding: UTF-8 -*-

import asyncio
import tornado
import tornado.platform.asyncio
import aiohttp

from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient
from tornado.tcpserver import TCPServer
from tornado.platform.asyncio import to_tornado_future
from tornado.gen import convert_yielded

from thinkutils.log.log import g_logger
from Constants import *

class TCPConnection(object):

    def __init__(self, stream, address):
        self.__stream = stream
        self.__address = address

        self.__stream.set_close_callback(self.on_close)
        self.on_connect()

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def get_ip(self):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, 'http://ip.cn')
            return html

    async def sleep(self, nTime):
        await asyncio.sleep(3)
        return "123"

    @gen.coroutine
    def test(self):
        raise gen.Return(1)

    @asyncio.coroutine
    def test1(self):
        return 1

    async def test2(self):
        return 3

    @gen.coroutine
    def on_close(self):
        if self.__stream is not None and False == self.__stream.closed():
            self.__stream.close()
            self.__stream = None

    @gen.coroutine
    def on_connect(self):
        print(self.test())
        print(self.test1())
        print(self.test2())

        try:
            szData = yield self.__stream.read_until(EOF.encode(ENCODING))
            yield self.__stream.write(szData.replace(EOF.encode(ENCODING), "".encode(ENCODING)))
            szIP = yield self.get_ip()
            yield self.__stream.write(szIP.encode(ENCODING))
            yield self.__stream.write(EOF.encode(ENCODING))
        except Exception as e:
            pass

        if self.__stream is not None and False == self.__stream.closed():
            self.on_connect()

class MyTorEchoServer(TCPServer):

    @gen.coroutine
    def handle_stream(self, stream, address):
        g_logger.info("Client from: %s" % (address, ))
        TCPConnection(stream, address)

    @classmethod
    def start_server(cls):
        tornado.platform.asyncio.AsyncIOMainLoop().install()
        ioloop = asyncio.get_event_loop()

        server = MyTorEchoServer()
        server.listen(9000)

        print("Starting server on tcp://localhost:9000")
        ioloop.run_forever()

        # IOLoop.instance().start()