from core.exceptions.interface.KernelExceptionInterface import KernelExceptionInterface
from core.exceptions.FatalKernelException import FatalKernelException
from core.kernel.interface.KernelInterface import KernelInterface


class KernelException:
    def __init__(self, exception_name, error, fatal=True):

        # if fatal, print err + python err if verbose, else only err
        if fatal:
            if KernelInterface.instance().verbose() == 1: raise FatalKernelException(self, exception_name, error)
            else:
                self.print_error(exception_name, error, newline=False, kill=True)

        # if not fatal, print err if verbose, else nothing
        if not fatal:
            if KernelInterface.instance().verbose() == 1: self.print_error(exception_name, error)

    @classmethod
    def print_error(cls, exception_name, error, newline=True, kill=False):
        KernelExceptionInterface.get_console().error(
            exception_name + " : " + error + ('\n' if newline else '')
        )
        if kill: exit(1)
