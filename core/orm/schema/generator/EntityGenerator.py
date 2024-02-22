from typing import Optional

from core.orm.schema.Schema import Schema
from core.kernel.file.helpers.FileSystem import FileSystem as fs


class EntityGenerator:

    def __init__(self): self.schema: Optional[Schema] = None

    def generate_from_schemas(self, schemas: dict[str, Schema]):
        generated_code = {}
        for schema_name in schemas.keys():
            generated_code[schema_name] = {
                "name": schemas[schema_name].name,
                "path": fs.from_root(fs.join("app", "common", "entities", f"{schemas[schema_name].name}.py")),
                "stub": self.generate_from_schema(schemas[schema_name])
            }
        return generated_code

    def generate_from_schema(self, schema: Schema):

        self.schema = schema

        entity_stub_file = fs.from_root(fs.join("core", "kernel", "stub", "entity", "entity.stub"))
        content = fs.content(entity_stub_file)

        replacements = {
            "%ENTITY%": schema.name,
            "%FIELDS_DEFINITION%": self.field_definition(),
            "%FIELDS_INITIALIZATION%": self.field_initialization(),
            "%FIELDS_DOCSTRING%": self.field_docstring(),
            "%PRIMARY_KEY%": self.primary_key(),
            "%IMPORTS%": self.imports(),
        }

        for replacement in replacements.keys(): content = content.replace(replacement, replacements[replacement])

        return content

    def field_definition(self):
        definition_str = ""

        for index, field in enumerate(self.schema.fields):
            if self.schema.fields[field].is_primary(): continue
            definition_str += self.schema.fields[field].definition()
            definition_str += ', ' if index != len(self.schema.fields) - 1 else ''

        return definition_str

    def field_initialization(self):
        initialization_str = ""

        for index, field in enumerate(self.schema.fields):
            if self.schema.fields[field].is_primary(): continue
            initialization_str += f"{(' ' * 8) if index != 0 else ''}"
            initialization_str += f"self.{self.schema.fields[field].name} = {self.schema.fields[field].name}"
            initialization_str += '\n' if index != len(self.schema.fields) - 1 else ''

        return initialization_str

    def field_docstring(self):
        docstring_str = ""

        for index, field in enumerate(self.schema.fields):
            docstring_str += f"{(' ' * 11)} - {self.schema.fields[field].definition()}"
            docstring_str += '\n' if index != len(self.schema.fields) - 1 else ''

        return docstring_str

    def primary_key(self): return f'"{self.schema.key.name}"'

    def imports(self):
        imports_str = ""

        for index, field in enumerate(self.schema.fields):
            field_obj = self.schema.fields[field]
            imports_str += field_obj.imports() + "\n" if field_obj.imports() else ""

        return imports_str
