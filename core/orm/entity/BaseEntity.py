from core.kernel.Base import Base
from core.orm.schema.Schema import Schema
from core.orm.schema.utils.EntityResolver import EntityResolver
from core.kernel.interface.KernelInterface import KernelInterface


class BaseEntity(Base):

    def __init__(self, primary_key: str):
        super().__init__()
        self.primary_key: str = primary_key
        setattr(self, self.primary_key, -1)
        self.__schema: Schema = self.schema()
        self.table = self.schema().table

    def __repr__(self):
        str_repr = f"{self.__class__.__name__}("
        for index, field in enumerate(self.schema().fields):
            str_repr += f"'{field}': {getattr(self, field)}"
            str_repr += ", " if index != len(self.schema().fields) - 1 else ""
        return str_repr + ")"

    @classmethod
    def schema(cls) -> Schema:

        if not hasattr(cls, 'primary_key'):  # == if class and not instance
            return KernelInterface.instance().app("orm").resolve_schema(
                EntityResolver.resolve_entity(cls)
            )

        else:
            if not hasattr(cls, '__schema'): return cls.orm.resolve_schema(
                EntityResolver.resolve_entity(cls)
            )
            return cls.__schema

    def serialize_to_tuple(self):
        tuple_obj: tuple = ()
        for index, field in enumerate(self.schema().fields): tuple_obj += (getattr(self, field),)
        return tuple_obj
