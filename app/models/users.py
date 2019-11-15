from pydantic.dataclasses import dataclass


@dataclass
class User:
    email: str
    username: str
    password: str
    is_cool: bool


users_db = [
    {
        'email': 'test@example.com',
        'username': 'username',
        'password': 'password',
        'is_cool': True
    },
    {
        'email': 'user2@example.com',
        'username': 'username',
        'password': 'password',
        'is_cool': False
    }
]
