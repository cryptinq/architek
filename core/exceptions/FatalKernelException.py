class FatalKernelException(Exception):
    """Base Exception"""

    def __init__(self, kernel_exception, exception_name, error):
        kernel_exception.print_error(exception_name, error)
