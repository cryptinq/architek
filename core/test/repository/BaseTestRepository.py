from core.exceptions.KernelException import KernelException


class BaseTestRepository:

    def __init__(self): pass

    @classmethod
    def run(cls): KernelException(
        "UnimplementedTestRepositoryRunMethodException",
        f"Method run() not implemented for test repository '{cls.__class__.__name__}'"
    )
