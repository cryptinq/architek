from __future__ import annotations
from typing import List

from app.common.entity.User import User
from core.orm.entity.repository.BaseRepository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, entity: User): super().__init__(entity)

    def get_by_id(self, entity_id: int) -> User | List[User]: return super().get_by_id(entity_id)
