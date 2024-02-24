from __future__ import annotations

from typing import Optional

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet
from core.impl.BaseSingleton import BaseSingleton


# from core.orm.entity.BaseEntity import BaseEntity


class EntityResolver(BaseSingleton):

    ENTITY_MAPPING: Optional[KeySet] = None

    @staticmethod
    def resolve_entity(entity):

        """ Resolve entity
            - from file name -> return a BaseEntity
            - from BaseEntity -> return entity schema
        """

        if not fs.file_exist(fs.from_root(fs.join("storage", "cache", "entities.py"))): KernelException(
            "UnavailableCacheFileException",
            "Some cache files are missing, please run 'python console entity:generate' to generate them"
        )

        entity_mapping = EntityResolver.load_from_cache()

        if not entity_mapping.has_key(entity): KernelException(
            "EntityNotFoundException",
            f"Entity {entity} does not exist, please run 'python console entity:generate' if this is an error"
        )

        try: return entity_mapping.get(entity)
        except KeyError: KernelException(
            "EntityResolverException",
            f"Invalid entity type provided, exepected 'string' or 'BaseEntity', got {str(type(entity))}"
        )

    @classmethod
    def resolve_schema(cls, entity):
        from core.orm.entity.BaseEntity import BaseEntity

        if issubclass(entity, BaseEntity): return entity.schema()
        elif isinstance(entity, str): return cls.resolve_entity(entity).schema
        else: KernelException(
            "EntityResolverException",
            f"Invalid entity type provided, exepected 'string' or 'BaseEntity', got {str(entity.__class__)}"
        )


    @staticmethod
    def load_from_cache():
        if EntityResolver.ENTITY_MAPPING is None:
            from storage.cache.entities import ENTITY_CACHE_MAPPING
            EntityResolver.ENTITY_MAPPING = KeySet(ENTITY_CACHE_MAPPING)
        return EntityResolver.ENTITY_MAPPING
