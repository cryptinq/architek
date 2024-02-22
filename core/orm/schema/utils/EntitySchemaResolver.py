from core.kernel.file.helpers.FileSystem import FileSystem as fs


class EntitySchemaResolver:



    @staticmethod
    def resolve_entities(orm):
        schemas = {}

        for schema_file_name in fs.list_files(orm.SCHEMAS_PATH, ".yaml"):
            schema_file_path = fs.join(orm.SCHEMAS_PATH, schema_file_name)
            schema_file_name_raw = schema_file_name.replace(".yaml", "")

            with open(schema_file_path, "r") as schema_file:
                schemas[schema_file_name_raw] = {
                    "__data": {
                        "file": schema_file_name,
                        "raw_yaml": schema_file.read()
                    }
                }
                schema_file.close()

        return schemas

    # @staticmethod
    # def resolve_class_from_schema(schema_name):
