from typing import Optional

from core.orm.entity.BaseEntity import BaseEntity
from core.orm.schema.Schema import Schema


class SQLInsertQuery:

    def __init__(self, table: str, entity: BaseEntity, schema: Schema,
                 columns: Optional[list] = None,
                 where: Optional[list] = None,
                 limit: int = 0,
                 ):

        self.table: str = table
        self.entity: BaseEntity = entity
        self.schema: Schema = schema
        self.columns: list = [] if columns is None else columns
        self.where: list = [] if where is None else where
        self.limit: int = limit
