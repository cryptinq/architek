from typing import Optional

import yaml

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.orm.ORM import ORM


class DatabaseCreateCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)
        self.orm: ORM = self.kernel.app("orm")
        self.schemas: Optional[dict] = None

    def invoke(self):

        self.schemas = self.resolve_entities()

        self.parse_schemas()
        self.validate_schemas()

        print(self.schemas)

    def resolve_entities(self):
        schemas = {}

        for schema_file_name in fs.list_files(self.orm.SCHEMAS_PATH, ".yaml"):

            schema_file_path = fs.join(self.orm.SCHEMAS_PATH, schema_file_name)
            schema_file_name_raw = schema_file_name.replace(".yaml", "")

            with open(schema_file_path, "r") as schema_file:
                schemas[schema_file_name_raw] = {
                    "__data": {
                        "file": schema_file_name,
                        "raw_yaml": schema_file.read()
                    }
                }
                schema_file.close()

        return schemas

    def parse_schemas(self):
        for schema in self.schemas.keys():
            self.schemas[schema]["__data"]["parsed_yaml"] = yaml.safe_load(
                self.schemas[schema]["__data"]["raw_yaml"]
            )
        return self.schemas

    def validate_schemas(self):
        pass
