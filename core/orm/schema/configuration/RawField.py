from core.exceptions.KernelException import KernelException
from core.orm.schema.enums.FieldType import FieldType
from core.orm.schema.Schema import Schema


class RawField:

    def __init__(self, entity_name: str, field_name: str, field_data: dict):
        self.entity_name: str = entity_name
        self.field_name: str = field_name
        self.field_data: dict = field_data

    def resolve(self):

        # check if field has type
        if not self.has_attribute("type"): KernelException(
            "InvalidFieldException",
            f"Field {self.field_name} has no attribute 'type' for entity '{self.entity_name.capitalize()}'"
        )

        # check if type is a valid field type
        field_type = self.get_attribute("type")
        if field_type not in FieldType.keys(): KernelException(
            "InvalidFieldException",
            f"Invalid attribute 'type' ({field_type}) for 'entity.{self.entity_name}.{self.field_name}'"
            f" - must be one of {list(FieldType.keys())}"
        )

        # resolve and return
        resolved_field = FieldType.resolve(field_type)
        return resolved_field(self.entity_name, self.field_name, self.field_data)

    def has_attribute(self, attribute: str): return attribute in self.field_data.keys()

    def get_attribute(self, attribute):
        return self.field_data[attribute] if self.has_attribute(attribute) else KernelException(
            "InvalidFieldException",
            f"Attribute '{attribute}' does not exist for 'entity.{self.entity_name}.{self.field_name}'"
        )