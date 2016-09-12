#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import functools


class MyClass:
    "Demonstration class for functools"

    def method1(self, a, b=2):
        "Docstring for method1()."
        print('  called method1 with:', (self, a, b))

    def method2(self, c, d=5):
        "Docstring for method2"
        print('  called method2 with:', (self, c, d))

    wrapped_method2 = functools.partial(method2, 'wrapped c')
    functools.update_wrapper(wrapped_method2, method2)

    def __call__(self, e, f=6):
        "Docstring for MyClass.__call__"
        print('  called object with:', (self, e, f))


def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    return


o = MyClass()

show_details('calling method1 directly', o.method1)
o.method1('no default for a', b=3)
print()

p1 = functools.partial(o.method1, b=4)
functools.update_wrapper(p1, o.method1)
show_details('calling method1 wrapped', p1)
p1('a goes here')
print()

show_details('calling method2 directly', o.method2)
o.method2('no default for c', d=6)
print()

show_details('calling method2 wrapped', o.wrapped_method2)
o.wrapped_method2('no default for c', d=7)
print()

show_details('instance', o)
o('no default for e')
print()

p2 = functools.partial(o, f=8)
functools.update_wrapper(p2, o)
show_details('instance wrapper', p2)
p2('e goes here')
