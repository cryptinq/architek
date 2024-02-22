from core.orm.schema.configuration.Field import Field
from core.exceptions.KernelException import KernelException
from core.orm.schema.enums.RelationType import RelationType
from core.kernel.interface.KernelInterface import KernelInterface


class RelationField(Field):

    # class defaults:
    #     length = 255

    def __init__(self, entity_name: str, field_name: str, field_data: dict):
        super().__init__(entity_name, field_name, field_data)

        self.orm = KernelInterface.instance().app("orm")

        self.related_entity = None
        self.related_field = None
        self.relation_type = None

        self.validate()

    def validate(self):

        # entity attribute
        if not self.has_attribute("entity"): KernelException(
            "InvalidRelationFieldValue",
            f"Invalid attribute 'entity' for 'entity.{self.entity_name}.{self.name}' - 'entity' attribute is not set"
        )
        else:
            # TODO: check if entity exist
            self.related_entity = self.get_attribute("entity")

        # field attribute
        if not self.has_attribute("field"): KernelException(
            "InvalidRelationFieldValue",
            f"Invalid attribute 'field' for 'entity.{self.entity_name}.{self.name}' - 'field' attribute is not set"
        )
        else:
            self.related_field = self.get_attribute("field")

        # relation attribute
        if not self.has_attribute("relation"): KernelException(
            "InvalidRelationFieldValue",
            f"Invalid attribute 'relation' for 'entity.{self.entity_name}.{self.name}' - 'relation' attribute is not set"
        )
        else:
            relation_type = self.get_attribute("relation")
            if relation_type not in [e.value for e in RelationType]: KernelException(
                "InvalidRelationFieldValue",
                f"Invalid attribute 'relation' for 'entity.{self.entity_name}.{self.name}' - "
                f"'relation' must be one of {[e.value for e in RelationType]}"
            )

    def sql(self): return f"INTEGER"

    def definition(self):
        entity_scheme = self.orm.resolve_schema(self.get_attribute("entity"))
        return f"{self.name}: {entity_scheme.name}"

    def imports(self):
        entity_scheme = self.orm.resolve_schema(self.get_attribute("entity"))
        return f"from common.entities.{entity_scheme.name} import {entity_scheme.name}"
