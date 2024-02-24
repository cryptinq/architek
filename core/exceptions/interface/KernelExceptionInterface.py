from core.kernel.decorators.ArchitekDecorator import architek


class KernelExceptionInterface:

    _CONSOLE = None

    @staticmethod
    @architek.boot
    def boot(kernel): KernelExceptionInterface._CONSOLE = kernel.app("console")

    @staticmethod
    def get_console(): return KernelExceptionInterface._CONSOLE
