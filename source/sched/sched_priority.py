#!/usr/bin/env python3
"""Basic sched example
"""
#end_pymotw_header

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print('EVENT:', time.ctime(time.time()), name)

now = time.time()
print('START:', time.ctime(now))
scheduler.enterabs(now + 2, 2, print_event, ('first',))     # 优先级为2
scheduler.enterabs(now + 2, 1, print_event, ('second',))    # 优先级为1,高于优先级2

scheduler.run()
