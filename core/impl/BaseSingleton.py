from core.kernel.Base import Base
from core.exceptions.KernelException import KernelException


class BaseSingleton(Base):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs, orm=False)

        if hasattr(self.__class__, '_instance'): KernelException(
            "SingletonInitializationException",
            f"Unable to initialize a new instance of {self.__class__} - class is a singleton"
        )

        self.__class__._instance = self
        if self.kernel.verbose(2): self.console.info(f"Initialized {self.__module__}(BaseSingleton)")

    @classmethod
    def __new__(cls, *args, **kwargs):

        if isinstance(cls, BaseSingleton) and cls == BaseSingleton: KernelException(
            "SingletonCreationException",
            f"Unable to instantiate BaseSingleton - this is an abstract class"
        )

        if not hasattr(cls, '_instance'): return super().__new__(*args, **kwargs)
        else: return cls._instance
