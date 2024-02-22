from typing import Optional

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet


class EntityResolver:

    ENTITY_MAPPING: Optional[KeySet] = None

    @staticmethod
    def resolve_entity(entity):

        if not fs.file_exist(fs.from_root(fs.join("storage", "cache", "entities.py"))): KernelException(
            "UnavailableCacheFileException",
            "Some cache files are missing, please run 'python console entity:generate' to generate them"
        )

        entity_mapping = EntityResolver.load_from_cache()

        if not entity_mapping.has_key(entity): KernelException(
            "EntityNotFoundException",
            f"Entity {entity} does not exist, please run 'python console entity:generate' if this is an error"
        )

        return entity_mapping.get(entity)

    @staticmethod
    def load_from_cache():
        if EntityResolver.ENTITY_MAPPING is None:
            from storage.cache.entities import ENTITY_CACHE_MAPPING
            EntityResolver.ENTITY_MAPPING = KeySet(ENTITY_CACHE_MAPPING)
        return EntityResolver.ENTITY_MAPPING
