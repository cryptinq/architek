from typing import Optional

from core.orm.schema.Schema import Schema
from core.kernel.file.helpers.FileSystem import FileSystem as fs


class RepositoryGenerator:

    def __init__(self): self.schema: Optional[Schema] = None

    def generate_from_schemas(self, schemas: dict[str, Schema]):
        generated_code = {}
        for schema_name in schemas.keys():
            generated_code[schema_name] = {
                "name": f"{schemas[schema_name].name}Repository",
                "path": fs.from_root(
                    fs.join("app", "common", "repository", f"{schemas[schema_name].name}Repository.py")
                ),
                "stub": self.generate_from_schema(schemas[schema_name])
            }
        return generated_code

    def generate_from_schema(self, schema: Schema):

        self.schema = schema

        repository_stub_file = fs.from_root(fs.join("core", "kernel", "stub", "entity", "repository.stub"))
        content = fs.content(repository_stub_file)

        replacements = {
            "%ENTITY%": schema.name,
        }

        for replacement in replacements.keys(): content = content.replace(replacement, replacements[replacement])

        return content
