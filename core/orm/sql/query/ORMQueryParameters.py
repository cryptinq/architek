from typing import Optional

from core.orm.sql.query.parameters.WhereParameter import WhereParameters
from core.orm.sql.query.parameters.abstract.AbstractParameters import AbstractParameters
from core.orm.sql.query.parameters.LimitParameter import LimitParameter


class ORMQueryParameters:

    def __init__(self):

        self._limit: Optional[int] = None
        self._where: Optional[AbstractParameters] = None

    @property  # create class only if .where called
    def where(self):
        if self._where is None: self._where = WhereParameters()
        return self._where

    @property  # create class only if .limit called
    def limit(self):
        if self._limit is None: self._limit = LimitParameter()
        return self._limit
