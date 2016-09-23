#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a coroutine
"""
#end_pymotw_header

import asyncio


async def coroutine():  #协程
    print('in coroutine')


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(
        coroutine()
    )
finally:
    print('closing event loop')
    event_loop.close()
