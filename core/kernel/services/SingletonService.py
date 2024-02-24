from impl.BaseSingleton import BaseSingleton
from kernel.services.BaseService import BaseService


class SingletonService(BaseSingleton, BaseService):

    def __str__(self): return self.__class__.__name__
