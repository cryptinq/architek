class KernelInterface:

    def app(self, name):
        module = getattr(self, name, None)
        if module is None:
            raise Exception(f"Unable to find module {name}.")
        return module if module is not None else None

    def bootstrap(self, interface):
        return interface.boot(self)


