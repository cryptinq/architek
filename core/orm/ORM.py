from typing import Optional

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.orm.driver.ORMDriver import ORMDriver
from core.orm.schema.utils.EntitySchemaParser import EntitySchemaParser
from core.orm.schema.utils.EntitySchemaResolver import EntitySchemaResolver
from core.orm.schema.utils.EntitySchemaValidator import EntitySchemaValidator
from core.orm.schema.utils.EntityResolver import EntityResolver
from core.exceptions.KernelException import KernelException


class ORM:

    SCHEMAS_PATH = fs.from_root("database/schema")

    def __init__(self, kernel):
        self.kernel = kernel
        self.driver: Optional[ORMDriver] = None
        self.schemas: Optional[dict] = None
        self.entity_resolver = EntityResolver()

    def initialize(self):

        # resolve & parse schemas from yaml files
        schemas = EntitySchemaResolver.resolve_entities(self)
        schemas = EntitySchemaParser.parse_schemas(schemas)

        # ensure that schemas are valid
        self.schemas = (EntitySchemaValidator(schemas)).validate()

        if self.kernel.verbose(1):
            self.kernel.console.info(f"Loaded schemas from configuration : {list(self.schemas.keys())}")

    def resolve_schema(self, key):
        if key not in self.schemas.keys(): KernelException(
            "InvalidSchemaException",
            f"Unable to resolve unknown schema {key}"
        )
        return self.schemas[key]
