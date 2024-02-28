from __future__ import annotations

from typing import Optional

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet
from core.impl.BaseSingleton import BaseSingleton
from core.orm.entity.BaseEntity import BaseEntity
from core.orm.entity.repository.BaseRepository import BaseRepository


class RepositoryResolver(BaseSingleton):

    REPOSITORY_MAPPING: Optional[KeySet] = None

    @staticmethod
    def resolve_repository(entity: BaseEntity):

        """ Resolve repository from entity"""

        if not fs.file_exist(fs.from_root(fs.join("storage", "cache", "repositories.py"))): KernelException(
            "UnavailableCacheFileException",
            "Some cache files are missing, please run 'python console entity:generate' to generate them"
        )

        repository_mapping = RepositoryResolver.load_from_cache()

        if not repository_mapping.has_key(entity): KernelException(
            "RepositoryNotFoundException",
            f"Unable to find repository corresponding to entity {entity.__class__.__name__} "
            f", please run 'python console entity:generate' to regenerate files if this is an error"
        )

        try:
            repository: BaseRepository = repository_mapping.get(entity)
            if repository not in RepositoryResolver.REPOSITORY_MAPPING.keys():
                RepositoryResolver.REPOSITORY_MAPPING.set(repository, repository(entity))
            return RepositoryResolver.REPOSITORY_MAPPING.get(repository)

        except KeyError: KernelException(
            "RepositoryResolverException",
            f"Invalid entity type provided, exepected 'BaseEntity', got {str(type(entity))}"
        )
        except Exception as e: KernelException(
            "RepositoryResolverException",
            f"There was an error while trying to resolve repository '{repository_mapping.get(entity).__name__}'"
            f"\n Error : {str(e)}"
        )


    @staticmethod
    def load_from_cache():
        if RepositoryResolver.REPOSITORY_MAPPING is None:
            from storage.cache.repositories import REPOSITORY_CACHE_MAPPING
            RepositoryResolver.REPOSITORY_MAPPING = KeySet(REPOSITORY_CACHE_MAPPING)
        return RepositoryResolver.REPOSITORY_MAPPING
