#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header

import tarfile
import time

with tarfile.open('example.tar', 'r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print('\tModified:\t', time.ctime(member_info.mtime))
        print('\tMode    :\t', oct(member_info.mode))
        print('\tType    :\t', member_info.type)
        print('\tSize    :\t', member_info.size, 'bytes')
        print()
