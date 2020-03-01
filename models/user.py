from sqlalchemy import (
    Column,
    Integer,
    String
)
from models import Base


class User(Base):
    """Model of a user."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    token = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
