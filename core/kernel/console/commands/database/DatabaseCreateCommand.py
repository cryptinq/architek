import sys
from datetime import datetime
from time import time
from typing import Optional

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.orm.ORM import ORM
from core.orm.schema.utils.EntitySchemaResolver import EntitySchemaResolver
from core.orm.schema.utils.EntitySchemaParser import EntitySchemaParser
from core.orm.schema.utils.EntitySchemaValidator import EntitySchemaValidator
from core.orm.sql.generator.SQLGenerator import SQLGenerator
from core.orm.schema.Schema import Schema


class DatabaseCreateCommand(BaseCommand):

    def __init__(self):
        super().__init__()
        self.schemas: Optional[dict] = None

    def invoke(self):

        seed = "-s" in sys.argv or "--seed" in sys.argv

        start_time = time()

        # resolve & parse schemas from yaml files
        self.schemas = EntitySchemaResolver.resolve_entities(self.orm)
        self.schemas = EntitySchemaParser.parse_schemas(self.schemas)

        # ensure that schemas are valid
        schemas_objects = (EntitySchemaValidator(self.schemas)).validate()

        sql_statement = (SQLGenerator()).generate_from_schemas(schemas_objects)

        if self.orm.driver.execute_script(sql_statement):
            for key in schemas_objects.keys():
                schema: Schema = schemas_objects[key]
                self.console.info(
                    f"Create table '{schema.table}' with columns: {[schema.fields[name].name for name in schema.fields.keys()]}"
                )

        print("")
        self.console.success(f"Database created successfully in {((time() - start_time) * 1000):.2f}ms")

        if seed:
            print("")
            self.kernel.invoke("database:seed")
