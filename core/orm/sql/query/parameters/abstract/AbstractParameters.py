from core.exceptions.KernelException import KernelException


class AbstractParameters:

    def __init__(self):
        self._params = []  # use this if many values
        self._param = None  # use this if single value

    def add(self, param: str): KernelException(
        "UnimplementedMethodException",
        f"Method {self.__class__}.add() is an abstract method, you should implement it in child class."
    )

    @property
    def params(self): return self._params

    @property
    def param(self): return self.param
    @param.setter
    def param(self, param): self._param = param
