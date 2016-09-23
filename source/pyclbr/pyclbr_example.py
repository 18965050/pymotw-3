"""Example source for pyclbr.
"""


class Base:
    """This is the base class.
    """

    def method1(self):
        return


class Sub1(Base):
    """This is the first subclass.
    """


class Sub2(Base):
    """This is the second subclass.
    """


class Mixin:
    """A mixin class.
    """

    def method2(self):
        return


class MixinUser(Sub2, Mixin):
    """Overrides method1 and method2
    """

    def method1(self):
        return

    def method2(self):
        return

    def method3(self):
        return


def my_function():
    """Stand-alone function.
    """
    return