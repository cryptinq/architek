from core.orm.schema.fields.String import StringField
from core.orm.schema.fields.Integer import IntegerField
from core.orm.schema.fields.Relation import RelationField


class FieldType:

    TYPES = {
        'string': StringField,
        'integer': IntegerField,
        'relation': RelationField
    }

    @staticmethod
    def members(): return FieldType.TYPES

    @staticmethod
    def keys(): return FieldType.TYPES.keys()

    @staticmethod
    def resolve(field_type: str): return FieldType.TYPES[field_type]
