from core.orm.sql.query.ORMQueryBuilderInterface import ORMQueryBuilderInterface
from core.orm.entity.BaseEntity import BaseEntity
from core.orm.sql.query.mode.SQLSelectQuery import SQLSelectQuery
from core.exceptions.KernelException import KernelException
from core.orm.sql.query.ORMQueryParameters import ORMQueryParameters


class ORMQueryBuilder(ORMQueryBuilderInterface):

    def __init__(self, entity: BaseEntity):
        super().__init__(entity)

        self.query_params = ORMQueryParameters()

    def build(self):

        if self.mode == self.MODE_SELECT: return SQLSelectQuery(
            table=self.table_name, entity=self.entity, schema=self.schema,
            where=self.query_params.where, limit=self.query_params.limit
        )

        # if self.mode == self.MODE_INSERT: return SQLInsertQuery()

        else: KernelException(
            "InvalidORMQueryBuilderMode",
            f"Invalid ORMQueryBuilder mode, expected: [{self.MODE_SELECT}, {self.MODE_INSERT}] got {self.mode}"
        )

