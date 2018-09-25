# -*- coding: UTF-8 -*-

import asyncio
import tornado
import tornado.platform.asyncio

from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient
from tornado.tcpserver import TCPServer

from thinkutils.log.log import g_logger
from Constants import *

@gen.coroutine
def echo(stream, text):
    """Send the text to the server and print the reply."""
    if text[-1] != EOF:
        text = text + EOF
    yield stream.write(text.encode(ENCODING))
    reply = yield stream.read_until(EOF.encode(ENCODING))
    print(reply.strip())

@gen.coroutine
def run_client():
    """Setup the connection to the echo server and wait for user
    input.
    """
    stream = yield TCPClient().connect('127.0.0.1', 9000)
    try:
        while True:
            data = input('(echo) ')
            yield echo(stream, data)
    except KeyboardInterrupt:
        stream.close()

if __name__ == '__main__':
    IOLoop.instance().run_sync(run_client)