from core.orm.sql.query.parameters.abstract.AbstractParameters import AbstractParameters


class WhereParameters(AbstractParameters):

    def __init__(self): super().__init__()

    def add(self, where: str): self.params.append(where)
