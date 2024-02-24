from core.orm.entity.BaseEntity import BaseEntity
from core.exceptions.KernelException import KernelException
from core.kernel.Base import Base

class EntityPersister(Base):

    def __init__(self): super().__init__(orm=False)

    def persist_many(self, entities: list[BaseEntity]):

        from core.orm.ORM import ORM
        orm = self.kernel.app("orm")

        entity_type = entities[0].__class__
        for entity in entities:
            if not isinstance(entity, entity_type): KernelException(
                "InvalidEntityTypesException",
                f"Unable to persist many entities that are not of the same type "
                f"- expected {entity_type} got {type(entity)}"
            )

        schema = self.kernel.app("orm").resolve_schema(entity_type)
        table = schema.table

        # INSERT STATEMENT

        sql = f"INSERT INTO {table} ("
        for index, field in enumerate(schema.fields): sql += f"{field}" + (", " if index < len(schema.fields) - 1 else ") VALUES (")
        for index, field in enumerate(schema.fields): sql += "?" + (", " if index < len(schema.fields) - 1 else ")")

        # DATA TREATMENT

        data = [entity.serialize_to_tuple() for entity in entities]

        if self.kernel.verbose(2):
            self.console.info(f" -- Executing SQL Statement")
            self.console.info(f" - SQL Statement: {sql}")
            self.console.info(f" - Data: {data}")

        return orm.driver.execute_many(sql, data)


