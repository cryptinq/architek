from core.orm.schema.configuration.Field import Field


class IntegerField(Field):

    def __init__(self, entity_name: str, field_name: str, field_data: dict):
        super().__init__(entity_name, field_name, field_data)

    def sql(self): return f"INTEGER"

    def definition(self): return f"{self.name}: int"
