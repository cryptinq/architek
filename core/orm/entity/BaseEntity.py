import inspect

from core.kernel.Base import Base
from core.orm.schema.Schema import Schema
from core.orm.schema.utils.EntityResolver import EntityResolver
from core.kernel.interface.KernelInterface import KernelInterface
from core.exceptions.KernelException import KernelException


class BaseEntity(Base):

    PRIMARY_KEY = ""

    def __init__(self, primary_key: str):
        super().__init__()
        self.primary_key: str = primary_key
        setattr(self, self.primary_key, -1)
        self.__schema: Schema = self.schema()
        self.table = self.__schema.table

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

    def serialize_to_tuple(self, remove_primary=True):
        tuple_obj: tuple = ()
        for index, field in enumerate(self.schema().fields):
            if remove_primary and field == self.primary_key: continue
            else: tuple_obj += (getattr(self, field),)
        return tuple_obj

    def serialize_to_dict(self, remove_primary=True):
        dict_obj: dict = {}
        for index, field in enumerate(self.schema().fields):
            if remove_primary and field == self.primary_key: continue
            else: dict_obj[field] = getattr(self, field)
        return dict_obj

    @classmethod
    def from_tuple(cls, tuple_obj: tuple):

        param_names = ["id"] + [param for param in inspect.signature(cls).parameters if param != 'self']
        resolved_params = []

        # Check if every required values
        for name, value in zip(param_names, tuple_obj): resolved_params.append(name)

        if len(resolved_params) != len(param_names): KernelException(
            "InvalidEntityFromTupleException",
            f"Invalid entity creation from tuple \n Tuple: {tuple_obj}, \n Expected : {param_names} \n Got : {resolved_params}"
        )

        # Create an instance of the class and set attributes dynamically
        instance = cls.__new__(cls)
        for name, value in zip(param_names, tuple_obj): setattr(instance, name, value)

        return instance
