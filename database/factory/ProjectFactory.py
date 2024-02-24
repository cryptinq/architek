from app.common.entity.Project import Project
from core.kernel.factory.BaseFactory import BaseFactory


class ProjectFactory(BaseFactory):

    entity = Project

    def __init__(self):
        super().__init__({
            "primary_key": "id",
            "fields": ["name", "user"]
        })

    def create(self, attrs: dict, ammount: int = 1):
        for _ in range(0, ammount):
            entity = Project(attrs["name"], attrs["user"])