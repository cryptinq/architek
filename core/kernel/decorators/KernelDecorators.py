from core.kernel.console.KernelConsole import KernelConsole


class KernelDecorator:

    @staticmethod
    def boot(func):
        def wrapper(*args, **kwargs):
            if args[0].verbose(0): KernelConsole.info(f" -- Initializing {func.__module__}")
            return_value = func(*args, **kwargs)
            if args[0].verbose(0): KernelConsole.success(f"{func.__module__} initialized successfully")
            return return_value
        return wrapper