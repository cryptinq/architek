from core.exceptions.KernelException import KernelException


class Field:

    def __init__(self, entity_name: str, field_name: str, field_data: dict):

        self.entity_name: str = entity_name
        self.name: str = field_name
        self.data: dict = field_data

        self.primary: bool = self.is_primary()

    def has_attribute(self, attribute: str):
        return attribute in self.data.keys()

    def get_attribute(self, attribute):
        return self.data[attribute] if self.has_attribute(attribute) else KernelException(
            "InvalidFieldException",
            f"Attribute '{attribute}' does not exist for 'entity.{self.entity_name}.{self.name}'"
        )

    def is_primary(self):
        if not self.has_attribute("primary"): return False
        return self.get_attribute("primary")

    def imports(self): return False
