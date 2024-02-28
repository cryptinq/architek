from __future__ import annotations

from typing import Optional

# from app.common.repository.UserRepository import UserRepository
# from app.common.entity.User import User
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.orm.driver.ORMDriver import ORMDriver
from core.orm.schema.utils.EntitySchemaParser import EntitySchemaParser
from core.orm.schema.utils.EntitySchemaResolver import EntitySchemaResolver
from core.orm.schema.utils.EntitySchemaValidator import EntitySchemaValidator

from core.orm.entity.BaseEntity import BaseEntity
from core.orm.interface.ORMImplementationInterface import ORMImplementationInterface
from core.orm.sql.query.QueryFactory import QueryFactory


class ORM(ORMImplementationInterface):

    SCHEMAS_PATH = fs.from_root("database/schema")

    def __init__(self, kernel):
        super().__init__(kernel)

        self.driver: Optional[ORMDriver] = None
        self.schemas: Optional[dict] = None

    def initialize(self):

        # resolve & parse schemas from yaml files
        schemas = EntitySchemaResolver.resolve_entities(self)
        schemas = EntitySchemaParser.parse_schemas(schemas)

        # ensure that schemas are valid
        self.schemas = (EntitySchemaValidator(schemas)).validate()

        if self.kernel.verbose(1):
            self.kernel.console.info(
                f"Loaded schemas from configuration : {list(self.schemas.keys())}"
            )

    def resolve_schema(self, key: str | BaseEntity):
        if key in self.schemas.keys(): return self.schemas[key]
        return self.entity_resolver().resolve_schema(key)

    def get_repository(self, entity: BaseEntity):
        return self.repository_resolver().resolve_repository(entity)

    def query_factory(self, entity: BaseEntity): return QueryFactory(entity)
