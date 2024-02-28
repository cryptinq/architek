from __future__ import annotations
from typing import List

from app.common.entity.Project import Project
from core.orm.entity.repository.BaseRepository import BaseRepository


class ProjectRepository(BaseRepository):

    def __init__(self, entity: Project): super().__init__(entity)

    def get_by_id(self, entity_id: int) -> Project | List[Project]: return super().get_by_id(entity_id)
