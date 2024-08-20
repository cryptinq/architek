from core.kernel.decorators.ArchitekDecorator import architek
from core.kernel.http.KernelServer import KernelServer


class KernelServerInterface:

    @staticmethod
    @architek.boot
    def boot(kernel):
        kernel_interface = KernelServerInterface(kernel)
        return kernel_interface.kernel_server

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_server = KernelServer(kernel)
        self.initialize()

    def initialize(self):
        self.kernel_server.initialize_server()
        self.kernel_server.register_routes()
