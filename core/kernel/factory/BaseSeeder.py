import os

from faker import Faker

from core.kernel.Base import Base
from core.kernel.factory.BaseFactory import BaseFactory
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.orm.entity.BaseEntity import BaseEntity


class BaseSeeder(Base):

    def __init__(self, entity: BaseEntity):
        super().__init__()
        self.entity: BaseEntity = entity
        self.factory: BaseFactory = self.orm.factory_manager().get_factory(entity)()
        self.path: str = fs.from_root(fs.join("database", "factory", f"{self.__class__.__name__}.py"))
        self.name: str = self.path.split(os.sep)[-1].replace(".py", "")

    def faker(self) -> Faker: return self.orm.factory_manager().faker()
