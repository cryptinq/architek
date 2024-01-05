from core.kernel.file.helpers.FileSystem import FileSystem as fs


class ORM:

    SCHEMAS_PATH = fs.from_root("database/schema")

    def __init__(self):
        pass