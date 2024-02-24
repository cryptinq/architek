from core.kernel.Base import Base


class BaseService(Base):

    def __str__(self): return self.__class__.__name__
