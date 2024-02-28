import sys
from time import time
from typing import Optional

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
from core.orm.schema.generator.RepositoryGenerator import RepositoryGenerator


class EntityGenerateCommand(BaseCommand):

    def __init__(self):
        super().__init__()

        self.orm: ORM = self.kernel.app("orm")
        self.schemas: Optional[dict] = None

        self.force = False

    def invoke(self):

        start_time = time()
        self.force = "-f" in sys.argv or "--force" in sys.argv

        # resolve & parse schemas from yaml files
        self.schemas = EntitySchemaResolver.resolve_entities(self.orm)
        self.schemas = EntitySchemaParser.parse_schemas(self.schemas)

        # ensure that schemas are valid
        schemas_objects: dict[str, Schema] = (EntitySchemaValidator(self.schemas)).validate()

        # generate entities & repositories
        self.generate_entities(schemas_objects)
        print("")
        self.generate_repositories(schemas_objects)

        # generate cache - used by orm to resolve entities, schemas, and repositories
        (EntityORMMappingGenerator(schemas_objects)).generate_cache()

        print("")
        self.console.success(f"Successfully generated {len(schemas_objects.keys())} entities in {((time() - start_time) * 1000):.2f}ms")

    def generate_entities(self, schemas_objects: dict[str, Schema]):

        generated_classes: dict[str, dict] = (
            EntityGenerator()
        ).generate_from_schemas(schemas_objects)

        for entity_key in generated_classes.keys():

            entity = generated_classes[entity_key]

            if not self.force:
                if fs.file_exist(entity["path"]): KernelException(
                    "EntityAlreadyExistsException",
                    f"Entity '{entity_key.capitalize()}' already exist at {entity['path']} "
                    f"- use --force to overwrite existing"
                )

            fs.write(entity["path"], entity["stub"])
            self.console.info(f"Created entity ∑9{entity['name']}∑f at {entity['path']}")

    def generate_repositories(self, schemas_objects: dict[str, Schema]):

        generated_classes: dict[str, dict] = (
            RepositoryGenerator()
        ).generate_from_schemas(schemas_objects)

        for repository_key in generated_classes.keys():

            repository = generated_classes[repository_key]

            if not self.force:
                if fs.file_exist(repository["path"]): KernelException(
                    "RepositoryAlreadyExistsException",
                    f"Repository '{repository['name']}' already exist at {repository['path']} "
                    f"- use --force to overwrite existing"
                )

            fs.write(repository["path"], repository["stub"])
            self.console.info(f"Created repository ∑9{repository['name']}∑f at {repository['path']}")
