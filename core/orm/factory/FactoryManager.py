import sys

from faker import Faker

from core.impl.BaseSingleton import BaseSingleton
from core.kernel.static.module.KernelModuleResolver import KernelModuleResolver
from core.kernel.factory.BaseFactory import BaseFactory
from core.orm.entity.BaseEntity import BaseEntity
from core.kernel.file.helpers.KeySet import KeySet
from core.exceptions.KernelException import KernelException
from core.exceptions.FatalKernelException import FatalKernelException


class FactoryManager(BaseSingleton):

    def __init__(self):
        super().__init__()

        self.__faker = self.faker()
        self.factories: dict[BaseEntity, BaseFactory] = self.resolve_factories()

    @classmethod
    def resolve_factories(cls) -> dict[BaseEntity, BaseFactory]:
        try:
            return {
                factory.entity: factory
                for factory
                in KernelModuleResolver.resolve_modules("database.factory")
            }
        except FatalKernelException as e:
            if "database:seed" in sys.argv: KernelException(e.name, e.error)
            else: KernelException(e.name, e.error, False)


    def get_factory(self, entity: BaseEntity) -> BaseFactory:

        factories = KeySet(self.factories)
        if not factories.has_key(entity): KernelException(
            "UnimplementedFactoryException",
            f"Unable to resolve entity for factory {entity.schema().name}"
        )

        return factories.get(entity)

    def faker(self):
        if not hasattr(self, "__faker"): self.__faker = Faker()
        return self.__faker
