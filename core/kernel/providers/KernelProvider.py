import os


class KernelProvider:

    def __init__(self, kernel):
        self.kernel = kernel
        self.providers = {}

    def boot(self, provider):
        provider_instance = provider(self.kernel)
        provider_id = provider_instance.id
        self.providers[provider_id] = provider_instance

        try:
            provider_instance.initialize()
        except AttributeError as e:
            self.kernel.throw("core function initialize() is missing from provider " + provider.__name__ + ".")

    def get(self, provider_id):
        if provider_id not in self.providers:
            self.kernel.throw("Provider " + provider_id + " not found.")
        return self.providers[provider_id]
