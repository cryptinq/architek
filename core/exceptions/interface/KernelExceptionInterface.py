from core.kernel.decorators.KernelDecorators import KernelDecorator


class KernelExceptionInterface:

    _CONSOLE = None

    @staticmethod
    # @KernelDecorator.boot
    def boot(kernel): KernelExceptionInterface._CONSOLE = kernel.app("console")

    @staticmethod
    def get_console(): return KernelExceptionInterface._CONSOLE
