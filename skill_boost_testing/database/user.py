from dataclasses import dataclass
from typing import List


@dataclass
class User:
    """Class representing a user with name, age and surname."""
    name: str = ""
    age: int = 18
    surname: str = ""

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name and self.surname == other.surname

    def __hash__(self):
        return hash((self.name, self.surname))
