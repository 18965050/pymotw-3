#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header

import tempfile

with tempfile.TemporaryFile(mode='w+t') as f:
    # f.writelines(['first\n', 'second\n'])
    f.write('Some data')

    f.seek(0)
    print(f.read())
    # for line in f:
        #print(line.rstrip())

