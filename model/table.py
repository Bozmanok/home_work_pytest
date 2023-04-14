from dataclasses import dataclass


@dataclass
class Table:
    websites: str
    popularity: int
    frontend: list
    backend: list
    database: list
    notes: str
