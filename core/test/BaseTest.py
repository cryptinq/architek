from unittest import TestCase

from core.kernel.Base import Base


class BaseTest(Base, TestCase):

    def __init__(self, test):
        Base.__init__(self)
        TestCase.__init__(self, test)
