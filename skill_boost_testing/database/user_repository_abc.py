from abc import ABC, abstractmethod
from typing import List

from skill_boost_testing.database.user import User


class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def find_all_users(self) -> List[User]:
        pass
