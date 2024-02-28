from __future__ import annotations

from typing import List, Optional, Any

from sql_smith import QueryFactory as SmithQueryFactory
from sql_smith.engine import CommonEngine as SmithCommonEngin
from sql_smith.query import InsertQuery, DeleteQuery, SelectQuery, UpdateQuery

from core.orm.entity.BaseEntity import BaseEntity
from core.orm.sql.query.ORMQuery import ORMQuery


class QueryFactory(SmithQueryFactory):

    def __init__(self, entity: BaseEntity):
        super().__init__(SmithCommonEngin())
        self.entity = entity

    def build(self, query: SelectQuery | InsertQuery | UpdateQuery | DeleteQuery):
        if isinstance(query, SelectQuery):
            return ORMQuery(self.entity, query.from_(self.entity.schema().table).compile())
        if isinstance(query, InsertQuery):
            return ORMQuery(self.entity, query.compile())

    def insert(self, column_values: Optional[dict[str, Any]]):
        return super().insert(self.entity.schema().table, column_values)


