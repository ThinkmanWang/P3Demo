#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import ssl
import socket
from kafka import KafkaProducer
from kafka.errors import KafkaError
from thinkutils.config.Config import *
from thinkutils.log.log import g_logger
import os

class ThinkKafkaProducer(object):

    g_kafkaContext = None
    g_producer = None

    @classmethod
    def init(cls):
        cls.g_producer = KafkaProducer(bootstrap_servers=g_config.get("kafka_mq", "bootstrap_servers"))

    @classmethod
    def send(cls, szTopic, szKey, szMsg):
        g_logger.debug("FXXK")
        try:
            g_logger.debug("%s" % (szMsg, ))
            partitions = cls.g_producer.partitions_for(szTopic)
            g_logger.debug('Topic下分区: %s' % (partitions, ))
            future = cls.g_producer.send(szTopic, szMsg, key=szKey)
            future.get()
            # g_logger.debug('send message success.')
        except KafkaError as e:
            g_logger.error('send message failed. %s' % e.message)
