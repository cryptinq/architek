class KernelInterface:

    def app(self, name):
        module = getattr(self, name, None)
        if module is None:
            raise Exception(f"Unable to find module {name}.")
        return module if module is not None else None

    def bootstrap(self, interface):
        return interface.boot(self)

    def throw(self, message):
        self.app("console").error("-" * 20 + " FATAL ERROR " + "-" * 20 + " \n\n" + message)
        exit(1)

    def kill(self):
        exit(1)
