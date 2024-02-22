from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet
# from core.orm.schema.Schema import Schema
from core.orm.schema.configuration.Field import Field


class Key:

    def __init__(self, schema, key_data: dict):

        self.schema = schema
        self.name = ""

        if not isinstance(key_data, dict): KernelException(
            "InvalidSchemaException",
            "Key is not a valid dictionary"
        )

        self.key_data = KeySet(key_data)

        self.validate_name()
        self.validate_generator()

    def validate_name(self):

        # check if key["name"] exist
        if not self.key_data.has_key("name"): KernelException(
            "InvalidSchemaException",
            f"Key 'name' is not defined for entity key '{self.schema.name}'"
        )

        # check if key["name"] is a valid field
        if self.key_data.get("name") not in self.schema.fields.keys(): KernelException(
            "InvalidSchemaException",
            f"Primary key '{self.key_data.get('name')}' is not a valid field for 'entity.{self.schema.name}'"
        )

        # check if field is defined as primary field
        field: Field = self.schema.fields[self.key_data.get("name")]
        if not field.is_primary: KernelException(
            "InvalidSchemaException",
            f"Field '{self.key_data.get('name')}' has not been defined as a primary key for entity "
            f"'{self.schema.name}' - add 'primary: true' to 'entity.{self.schema.name.lower()}.{self.key_data.get('name')}'"
        )

        self.name = self.key_data.get("name")

    def validate_generator(self):
        pass

