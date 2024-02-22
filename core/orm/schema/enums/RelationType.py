from enum import Enum


class RelationType(Enum):
    MANY_TO_MANY = "many_to_many"
    MANY_TO_ONE = "many_to_one"
    ONE_TO_MANY = "one_to_many"
    ONE_TO_ONE = "one_to_one"
