from core.orm.schema.configuration.Field import Field


class IntegerField(Field):

    # class defaults:
    #     length = 255

    def __init__(self, entity_name: str, field_name: str, field_data: dict):
        super().__init__(entity_name, field_name, field_data)
        #
        # self.length = 0

    # def validate(self):
    #
    #     if not self.has_attribute("length"): self.length = self.defaults.length
    #     else:
    #         if self.length > 65535: KernelException(
    #             "InvalidStringFieldValue",
    #             f"Invalid attribute 'length' for 'entity.{self.entity_name}.{self.name}' - must be between 0 and 65535"
    #         )
    #         self.length = self.get_attribute("length")

    def sql(self): return f"INTEGER"
