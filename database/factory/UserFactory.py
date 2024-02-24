from app.common.entity.User import User
from core.kernel.factory.BaseFactory import BaseFactory


class UserFactory(BaseFactory):

    entity = User

    def __init__(self):
        super().__init__({
            "primary_key": "id",
            "fields": ["name", "email", "password"]
        })

