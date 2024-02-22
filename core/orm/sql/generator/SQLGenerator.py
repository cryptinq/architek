from core.orm.schema.Schema import Schema
from core.orm.schema.configuration.Field import Field


class SQLGenerator:

    def __init__(self): pass

    def generate_from_schemas(self, schemas: dict[str, Schema]):
        sql_statement = ""
        for schema_name in schemas.keys(): sql_statement += self.generate_from_schema(schemas[schema_name]) + "\n"
        return sql_statement

    def generate_from_schema(self, schema: Schema):
        sql_statement = f"CREATE TABLE {schema.table} ("
        for index, field_key in enumerate(schema.fields.keys()):
            field: Field = schema.fields[field_key]
            sql_statement += f"{field.name} {field.sql()}{', ' if index != len(schema.fields) - 1 else ''}"
        return sql_statement + ");"