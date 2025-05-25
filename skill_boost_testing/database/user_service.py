from typing import List

from skill_boost_testing.database.exceptions import NameException, AgeException
from skill_boost_testing.database.user import User
from skill_boost_testing.database.user_repository_abc import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def save(self, user: User) -> bool:
        try:
            if not user.name:
                raise NameException("Name is not correct! This user cannot be saved!")
            elif user.age == 0:
                raise AgeException("Age is not correct! This user cannot be saved!")

            self.user_repository.save_user(user)
        except Exception as e:
            print(e)
            return False

        return True

    def find_all_with_name_containing(self, search: str) -> List[User]:
        all_users = self.user_repository.find_all_users()
        output = []

        for user in all_users:
            if search in user.name or search in user.surname:
                output.append(user)

        return output
