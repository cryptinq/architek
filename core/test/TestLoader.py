import unittest


class TestLoader:
    def __init__(self):
        self.loader = unittest.defaultTestLoader

    def from_test_case(self, test_case):
        return self.loader.loadTestsFromTestCase(test_case)