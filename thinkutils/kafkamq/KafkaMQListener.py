#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from abc import *
from threading import Thread

import ssl
import socket
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from kafka import KafkaProducer
from thinkutils.config.Config import g_config
from thinkutils.common_utils.StringUtils import *

import os

class KafkaMQListener(Thread):
    __metaclass__ = ABCMeta

    def __init__(self, szServer, szTopics, szGID = "", szCID = ""):
        super(KafkaMQListener, self).__init__()

        self.m_szTopics = szTopics

        if is_empty_string(szGID) or is_empty_string(szCID):
            self.m_consumer = KafkaConsumer(
                bootstrap_servers=szServer
            )
        else:
            self.m_consumer = KafkaConsumer(
                bootstrap_servers=szServer
                , group_id=szGID
                , client_id=szCID
            )

    @abstractmethod
    def on_message(self, szChannel, data):
        # 修改成你的代码逻辑
        # print item["channel"], item["data"]
        pass

    def run(self):
        while True:
            try:
                self.m_consumer.subscribe(tuple(self.m_szTopics))
                for message in self.m_consumer:
                    self.on_message(message.topic, message.value)
            except Exception as e:
                continue
            finally:
                pass
