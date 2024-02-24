from typing import Optional

from core.orm.entity.common.EntityPersister import EntityPersister
from core.orm.factory.FactoryManager import FactoryManager
from core.orm.schema.utils.EntityResolver import EntityResolver


class ORMImplementationInterface:

    def __init__(self, kernel):

        self.kernel = kernel

        self._entity_resolver: Optional[EntityResolver] = self.entity_resolver()
        self._factory_manager: Optional[FactoryManager] = self.factory_manager()
        self._entity_persister: Optional[EntityPersister] = self.entity_persister()

        self.register_methods()

    def register_methods(self):

        # Register here method that can be used with self.orm.your_method()

        methods = {
            "persist_many": self.entity_persister().persist_many
        }

        for method in methods.keys(): setattr(self, method, methods[method])

    def entity_persister(self):
        if not hasattr(self, "_entity_persister"): self._entity_persister = EntityPersister()
        return self._entity_persister

    def entity_resolver(self):
        if not hasattr(self, "_entity_resolver"): self._entity_resolver = EntityResolver()
        return self._entity_resolver

    def factory_manager(self):
        if not hasattr(self, "_factory_manager"): self._factory_manager = FactoryManager()
        return self._factory_manager
