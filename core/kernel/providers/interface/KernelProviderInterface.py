import os

from core.kernel.providers.KernelProvider import KernelProvider
from core.providers.EnvironmentProvider import EnvironmentProvider


class KernelProviderInterface:

    @staticmethod
    def boot(kernel):
        kernel_interface = KernelProviderInterface(kernel)
        return kernel_interface.kernel_provider

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_provider = KernelProvider(kernel)
        self.initialize()

    def initialize(self):

        providers = [EnvironmentProvider]

        for provider in providers:
            self.kernel_provider.boot(provider)
