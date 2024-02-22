import sys
from time import time
from typing import Optional

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.orm.ORM import ORM
from core.orm.schema.utils.EntitySchemaResolver import EntitySchemaResolver
from core.orm.schema.utils.EntitySchemaParser import EntitySchemaParser
from core.orm.schema.utils.EntitySchemaValidator import EntitySchemaValidator
from core.orm.schema.generator.EntityGenerator import EntityGenerator
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.orm.schema.generator.EntityORMMappingGenerator import EntityORMMappingGenerator
from core.orm.schema.Schema import Schema
from core.exceptions.KernelException import KernelException


class EntityGenerateCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)
        self.orm: ORM = self.kernel.app("orm")
        self.schemas: Optional[dict] = None

    def invoke(self):

        start_time = time()
        force = "-f" in sys.argv or "--force" in sys.argv

        # resolve & parse schemas from yaml files
        self.schemas = EntitySchemaResolver.resolve_entities(self.orm)
        self.schemas = EntitySchemaParser.parse_schemas(self.schemas)

        # ensure that schemas are valid
        schemas_objects: dict[str, Schema] = (EntitySchemaValidator(self.schemas)).validate()

        generated_classes: dict[str, dict] = (
            EntityGenerator()
        ).generate_from_schemas(schemas_objects)

        for entity_key in generated_classes.keys():

            entity = generated_classes[entity_key]

            if not force:
                if fs.file_exist(entity["path"]): KernelException(
                    "EntityAlreadyExistsException",
                    f"Entity '{entity_key.capitalize()}' already exist at {entity['path']} - use --force to overwrite existing"
                )

            fs.write(entity["path"], entity["stub"])
            self.console.info(f"Created entity {entity['name']} at {entity['path']}")

        (EntityORMMappingGenerator(schemas_objects)).generate_cache()

        print("")
        self.console.success(f"Successfully generated {len(generated_classes.keys())} entities in {((time() - start_time) * 1000):.2f}ms")

    def generate(self):
        pass