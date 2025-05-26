import pytest
from unittest.mock import Mock

from skill_boost_testing.database.user import User
from skill_boost_testing.database.user_service import UserService


@pytest.fixture
def user_repository():
    repo = Mock()
    repo.find_all_users.return_value = [
        User(name="John", age=20, surname="Doe"),
        User(name="Jonny", age=20, surname="Doe"),
        User(name="Jan", age=20, surname="Doe"),
        User(name="Dirk", age=20, surname="Johanson"),
        User(name="Mark", age=20, surname="Doe")
    ]
    return repo


@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)


def test_given_a_database_with_five_users_when_searching_for_name_containing_jo_expect_three_users(user_repository,
                                                                                                   user_service):
    # Act
    users_with_jo = user_service.find_all_with_name_containing("Jo")

    # Assert
    user_repository.find_all_users.assert_called_once()
    assert len(users_with_jo) == 3
