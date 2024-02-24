from core.impl.BaseSingleton import BaseSingleton
from core.kernel.services.classes.BaseService import BaseService


class SingletonService(BaseSingleton, BaseService):

    def __str__(self): return self.__class__.__name__
