from __future__ import annotations

from core.kernel.file.helpers.KeySet import KeySet
from core.exceptions.KernelException import KernelException
from core.kernel.Base import Base
from core.orm.entity.BaseEntity import BaseEntity


class BaseFactory(Base):

    REQUIRED_ATTRIBUTES = ["primary_key", "fields"]

    def __init__(self, attrs: dict):
        super().__init__(orm=False)

        self.attrs = KeySet(attrs.copy())
        if not self.attrs.has_keys(BaseFactory.REQUIRED_ATTRIBUTES): KernelException(
            "InvalidFactoryInitializationException",
            f"Missing required attributes for {self.__class__} "
            f"- {self.attrs.missing_keys(BaseFactory.REQUIRED_ATTRIBUTES)}"
        )

        self.entity = self.__class__.entity
        self.primary_key = self.attrs.get("primary_key")
        self.fields = self.attrs.get("fields")  # ["name", "email", "password"]

        if self.kernel.verbose(2):
            self.console.info(
                f"Initialized Factory '{self.__class__.__name__}' for entity '{self.entity.schema().name}'"
            )

    def create(self, attrs: dict, amount: int = 1):
        entities = []
        for _ in range(0, amount):
            fields = {
                field: attrs.get(field)() if callable(attrs.get(field)) else attrs.get(field)
                for field in self.fields
            }
            entity = self.entity(**fields)
            entities.append(entity)
        return entities

    def persist(self, entity: list[BaseEntity] | BaseEntity) -> bool:
        if isinstance(entity, BaseEntity): return entity.save()
        return self.kernel.app("orm").persist_many(entity)

