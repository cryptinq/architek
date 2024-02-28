from core.orm.sql.query.parameters.abstract.AbstractParameters import AbstractParameters


class LimitParameter(AbstractParameters):
    def __init__(self): super().__init__()

    def set(self, limit: int): self.param = limit
