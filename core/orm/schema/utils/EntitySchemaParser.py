import yaml


class EntitySchemaParser:

    @staticmethod
    def parse_schemas(schemas):
        for schema in schemas.keys():
            schemas[schema]["__data"]["parsed_yaml"] = yaml.safe_load(
                schemas[schema]["__data"]["raw_yaml"]
            )
        return schemas