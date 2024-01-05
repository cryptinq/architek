from core.exceptions.interface.KernelExceptionInterface import KernelExceptionInterface


class KernelException(Exception):
    """Base Exception"""

    def __init__(self, exception_name, error):
        KernelExceptionInterface.get_console().error(
            exception_name + " : " + error + "\n"
        )
