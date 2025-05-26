import pytest
from typing import List

from skill_boost_testing.database.user import User
from skill_boost_testing.database.user_repository_abc import UserRepository
from skill_boost_testing.database.user_service import UserService


class FakeUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def save_user(self, user: User) -> None:
        self.users.append(user)

    def find_all_users(self) -> List[User]:
        return self.users


@pytest.fixture
def fake_database():
    return FakeUserRepository()


@pytest.fixture
def user_service(fake_database):
    return UserService(fake_database)


def test_given_user_with_non_empty_name_and_age_not_zero_when_saving_expect_user_saved_in_database(fake_database,
                                                                                                   user_service):
    # Arrange
    assert len(fake_database.find_all_users()) == 0
    user = User(name="John", age=20, surname="Doe")

    # Act
    is_success = user_service.save(user)

    # Assert
    assert is_success is True
    assert len(fake_database.find_all_users()) == 1


def test_given_a_database_with_five_users_when_searching_for_name_containing_jo_expect_three_users(fake_database,
                                                                                                   user_service):
    # Arrange
    assert len(fake_database.find_all_users()) == 0
    user1 = User(name="John", age=20, surname="Doe")
    user2 = User(name="Jonny", age=20, surname="Doe")
    user3 = User(name="Jan", age=20, surname="Doe")
    user4 = User(name="Dirk", age=20, surname="Johanson")
    user5 = User(name="Mark", age=20, surname="Doe")

    user_service.save(user1)
    user_service.save(user2)
    user_service.save(user3)
    user_service.save(user4)
    user_service.save(user5)

    # Act
    users_with_jo = user_service.find_all_with_name_containing("Jo")

    # Assert
    assert len(users_with_jo) == 3
