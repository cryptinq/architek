from core.orm.entity.BaseEntity import BaseEntity


class ORMQueryBuilderInterface:

    MODE_SELECT = "SELECT"
    MODE_INSERT = "INSERT"

    def __init__(self, entity: BaseEntity):
        self.entity = entity
        self.schema = self.entity.schema()
        self.table_name = self.schema.table
        self._mode = ORMQueryBuilderInterface.MODE_SELECT

    @property
    def mode(self) -> str: return self._mode

    @mode.setter
    def mode(self, mode: str) -> None: self._mode = mode
