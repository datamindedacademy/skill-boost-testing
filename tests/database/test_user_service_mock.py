import pytest
from unittest.mock import Mock

from skill_boost_testing.database.user import User
from skill_boost_testing.database.user_service import UserService


@pytest.fixture
def user_repository():
    return Mock()


@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)


def test_given_user_with_non_empty_name_and_age_not_zero_when_saving_expect_user_saved_in_database(user_repository,
                                                                                                   user_service):
    # Arrange
    user = User(name="John", age=20, surname="Doe")

    # Act
    is_success = user_service.save(user)

    # Assert
    assert is_success is True
    user_repository.save_user.assert_called_once_with(user)
