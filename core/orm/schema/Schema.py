class Schema:

    def __init__(self, name: str, table: str, timestamp: bool):
        self.name = name
        self.table = table
        self.timestamp = timestamp
        self.fields = []
        self.key = ""

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Schema(name={self.name}, table={self.table})"
