from __future__ import annotations

from typing import Optional

from sql_smith.query import Query

from core.kernel.Base import Base
from core.orm.driver.ORMDriver import ORMDriver
from core.orm.entity.BaseEntity import BaseEntity


class ORMQuery(Base, Query):
    
    def __init__(self, entity: BaseEntity, query: Query):
        super().__init__()
        Query.__init__(self, query.sql, query.params)
        self.entity = entity

    def execute(self, fetch="one") -> bool | list[BaseEntity] | BaseEntity:

        result: Optional[BaseEntity] | Optional[list[BaseEntity]] = None

        orm_driver: ORMDriver = self.orm.driver
        query_result = orm_driver.execute(self.sql, params=self.params, fetch=fetch)

        if fetch == "one":
            result: BaseEntity = self.entity.from_tuple(query_result) \
                if query_result not in [None, False] else None

        if fetch == "all":
            result: list[BaseEntity] = [
                self.entity.from_tuple(entity) for entity in query_result
            ] if query_result is not None else []

        return result if result not in [None, False] else None


