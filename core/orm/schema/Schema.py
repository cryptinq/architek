from typing import Optional

from core.orm.schema.configuration.Key import Key


class Schema:

    def __init__(self, name: str, table: str, timestamp: bool):
        self.name = name
        self.table = table
        self.timestamp = timestamp
        self.fields = []
        self.key: Optional[Key] = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Schema(name={self.name}, table={self.table})"
