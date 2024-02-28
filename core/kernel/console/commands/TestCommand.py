import os
import sys
import unittest
from unittest import TestSuite

from core.kernel.console.base.BaseCommand import BaseCommand
from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.test.repository.BaseTestRepository import BaseTestRepository
from core.test.BaseTest import BaseTest
from core.test.TestLoader import TestLoader
from core.test.TestResult import TestResult


class TestCommand(BaseCommand):

    def __init__(self):
        super().__init__()
        self.test_loader = TestLoader()

    def invoke(self):

        if len(sys.argv) < 3: KernelException(
            "MissingRequiredArgumentException",
            f"Argument 'test' is missing, use \"python console test 'test_name'\""
        )

        test_name = sys.argv[2]
        test_path = fs.from_root(
            fs.join("test", *tuple(path for path in test_name.split('/')))
        ) + ".py"

        if not fs.file_exist(test_path): KernelException(
            "InvalidTestException",
            f"Invalid test provided, 'test/{test_name}.py' does not exist"
        )

        test_class = self.kernel.resolve_class(
            "test." + test_name.replace(os.sep, "."),
            test_name.split("/")[-1].replace(".py", "")
        )

        if issubclass(test_class, BaseTestRepository): tests = [test_cls for test_cls in test_class.run()]
        else: tests = [test_class]

        result = self.run_tests(tests)

        if result.wasSuccessful(): print(); self.console.success("All tests passed !")
        else:
            failed, passed = len(result.errors), len(tests)
            self.console.error(f"Some test failed (∑c{failed} ∑f/ ∑a{passed}∑f)")

    def run_tests(self, tests: list[BaseTest]):

        test_suites_list: list[TestSuite] = []
        test_runner = unittest.TextTestRunner(resultclass=TestResult)

        test_runner.resultclass.console = self.console

        for test_cls in tests:
            test_suites_list.append(
                self.test_loader.from_test_case(test_cls)
            )

        test_suites = unittest.TestSuite(test_suites_list)

        test_runner.resultclass.nb_tests = test_suites.countTestCases()
        self.console.info(f"Running {test_suites.countTestCases()} tests from ∑9test/{sys.argv[2]}"); print()

        return test_runner.run(test_suites)
