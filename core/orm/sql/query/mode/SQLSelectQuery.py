from typing import Optional

from core.orm.entity.BaseEntity import BaseEntity
from core.orm.schema.Schema import Schema
# from core.orm.sql.query.mode.ORMQuery import ORMQuery
from core.orm.sql.query.parameters.LimitParameter import LimitParameter
from core.orm.sql.query.parameters.WhereParameter import WhereParameters
from core.orm.sql.query.ORMQuery import ORMQuery


class SQLSelectQuery(ORMQuery):

    def __init__(self, table: str, entity: BaseEntity, schema: Schema, columns: Optional[list] = None,
                 where: WhereParameters = None, limit: LimitParameter = None):

        super().__init__()
        self.table: str = table
        self.entity: BaseEntity = entity
        self.schema: Schema = schema
        self.columns: list = [] if columns is None else columns
        self.where: WhereParameters = where
        self.limit: LimitParameter = limit

    def execute(self):
        pass

    def build_query(self) -> str:

        columns = "*" if len(self.columns) == 0 else "(" + (", ".join(self.columns)[-2:-2]) + ")"

        sql_query = f"SELECT {columns} FROM {self.table}"

        # if len(self.where.params) != 0:
            # sql_query += f" WHERE {self.where.}"

