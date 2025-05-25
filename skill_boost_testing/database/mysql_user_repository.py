from typing import List
import mysql.connector

from skill_boost_testing.database.user import User
from skill_boost_testing.database.user_repository_abc import UserRepository


class MySqlUserRepository(UserRepository):
    USERNAME = "root"
    PASSWORD = "password"

    def save_user(self, user: User):
        sql = "INSERT INTO users VALUES(%s, %s, %s)"

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (user.name, user.surname, user.age))
            conn.commit()
        finally:
            conn.close()

    def find_all_users(self) -> List[User]:
        sql = "SELECT * FROM users"

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)

            users = []
            for (name, surname, age) in cursor:
                user = User()
                user.name = name
                user.surname = surname
                user.age = age
                users.append(user)

            return users
        finally:
            conn.close()

    def get_connection(self):
        return mysql.connector.connect(
            host="localhost:3306",
            user=self.USERNAME,
            password=self.PASSWORD,
            database=self.USERNAME
        )
