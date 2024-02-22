from core.orm.schema.Schema import Schema
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.kernel.interface.KernelInterface import KernelInterface


class EntityORMMappingGenerator:

    def __init__(self, schemas: dict[str, Schema]):
        self.kernel = KernelInterface.instance()
        self.console = self.kernel.app("console")
        self.schemas = schemas

    def generate_cache(self):

        imports = []
        orm_cache_mapping = "ENTITY_CACHE_MAPPING = {"

        for index, key in enumerate(self.schemas.keys()):
            schema = self.schemas[key]
            orm_cache_mapping += f"'{key}': {schema.name}"
            orm_cache_mapping += ", " if index != len(self.schemas) - 1 else ""
            imports.append(f"from common.entities.{schema.name} import {schema.name}")

        content = '\n'.join(imports) + "\n" * 2 + orm_cache_mapping + "}\n"

        cache_file_path = fs.from_root(fs.join("storage", "cache", "entities.py"))
        fs.write(cache_file_path, content)

        if self.kernel.verbose(1):
            self.console.info(f"Generated entity cache at {cache_file_path}")