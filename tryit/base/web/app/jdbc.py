# -*- coding: utf-8 -*-
import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time,aiomysql
from datetime import datetime


@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info("create database connect  poll")
    global _pool
    _pool = yield from aiomysql.create_pool(
        host=kw.get('host', '192.168.229.129'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop

    )
