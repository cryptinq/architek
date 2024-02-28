from test.core.orm.repository.RepositoryTest import RepositoryTest

from core.test.repository.BaseTestRepository import BaseTestRepository


class CoreTestRepository(BaseTestRepository):

    @classmethod
    def run(cls): return [
        RepositoryTest
    ]
