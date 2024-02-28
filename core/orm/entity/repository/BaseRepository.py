from __future__ import annotations

from sql_smith.functions import field

from core.orm.entity.BaseEntity import BaseEntity
from core.orm.schema.Schema import Schema
from core.orm.sql.query.QueryFactory import QueryFactory
from core.orm.sql.query.ORMQuery import ORMQuery
from core.exceptions.KernelException import KernelException
from core.impl.BaseSingleton import BaseSingleton


# from core.orm.ORM import ORM


class BaseRepository(BaseSingleton):

    def __init__(self, entity: BaseEntity):
        super().__init__(orm=True)
        self.__entity: BaseEntity = entity
        self.__schema: Schema = entity.schema()
        self.__table: str = self.__schema.table

    @property
    def entity(self): return self.__entity
    @property
    def schema(self): return self.__schema
    @property
    def table(self): return self.__table

    def get_by_id(self, entity_id: int) -> list[BaseEntity] | BaseEntity:
        factory: QueryFactory = self.orm.query_factory(self.entity)
        query: ORMQuery = factory.build(
            factory.select("*").where(field("id").eq(entity_id))
        )
        return query.execute(fetch="one")

    def save(self, entity: BaseEntity | list[BaseEntity]) -> bool:

        if not isinstance(entity, self.entity): KernelException(
            "IncompatibleEntityTypeException",
            f"Incompatible entity type {entity.__class__.__name__} in repository {self.__class__.__name__} \n"
            f" Expected: {self.entity.__name__}, got {entity.__class__.__name__}"
        )

        factory: QueryFactory = self.orm.query_factory(self.entity)
        query: ORMQuery = factory.build(
            factory.insert(entity.serialize_to_dict())
        )
        return query.execute(fetch=None)
