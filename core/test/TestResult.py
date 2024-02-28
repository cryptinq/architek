from typing import TextIO
from unittest import TextTestResult


class TestResult(TextTestResult):

    console = None
    index = 0
    nb_tests = 0

    def __init__(self, stream: TextIO, descriptions: bool, verbosity: int):
        super().__init__(stream, descriptions, 0)

    def name(self, test):
        components = test.id().split('.')[-2:]
        components[0] = f"∑9{components[0]}∑f"
        return ' -> '.join(components) + "()"

    def startTest(self, test):
        super().startTest(test)
        self.console.info(f"[{self.index}] {self.name(test)}")
        if self.index == self.nb_tests - 1: print()
        self.index += 1
