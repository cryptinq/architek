from dataclasses import dataclass
from typing import Callable


@dataclass
class Route:
    rule: str
    method: Callable
    endpoint: str
    methods: list[str]
