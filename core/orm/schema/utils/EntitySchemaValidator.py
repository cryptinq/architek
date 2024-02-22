from core.exceptions.KernelException import KernelException
from core.orm.schema.Schema import Schema
from core.orm.schema.configuration.Key import Key
from core.orm.schema.configuration.Field import Field
from core.orm.schema.configuration.RawField import RawField


class EntitySchemaValidator:

    def __init__(self, schemas: dict):
        self.schemas: dict = schemas
        self.schema_objects: dict[str, Schema] = {}

    def validate(self):

        # check if required attributes
        self.validate_attributes(["name", "table", "timestamp", "key", "fields"])

        for entity in self.schemas.keys():
            schema_data = self.schemas[entity]["__data"]["parsed_yaml"]["entity"]

            # create base schema class
            schema: Schema = Schema(
                name=schema_data["name"],
                table=schema_data["table"],
                timestamp=schema_data["timestamp"],
            )
            schema.fields = self.handle_fields(entity, schema_data)  # handle fields
            schema.key = Key(schema, schema_data["key"])  # handle key
            self.schema_objects[entity] = schema  # save schema

        return self.schema_objects

    @classmethod
    def handle_fields(cls, entity: str, schema_data: dict):

        # check if 'fields' is a dict
        if not isinstance(schema_data["fields"], list): KernelException(
            "InvalidSchemaException",
            f"Invalid 'fields' attributes for entity {entity.capitalize()} - must be a list of dictionaries"
        )

        # parse and validate all fields as Field objects
        fields: dict[str, Field] = {}

        for field_dict in schema_data["fields"]:

            field_key = list(field_dict.keys())[0]
            field_data = field_dict[field_key]

            # general field validation "type" etc
            raw_field: RawField = RawField(entity, field_key, field_data)

            # per field type validation, ex for string 'length' etc
            fields[field_key] = raw_field.resolve()

        # add fields object to our schema object & return it
        return fields

    def validate_attributes(self, attributes):

        for entity in self.schemas.keys():
            schema_data = self.schemas[entity]["__data"]["parsed_yaml"]["entity"]

            for attribute in attributes:
                if attribute not in schema_data.keys(): KernelException(
                    "InvalidSchemaException",
                    f"Invalid schema for entity '{entity.capitalize()}' - missing '{attribute}' attribute"
                )

