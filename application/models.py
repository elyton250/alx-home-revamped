"""this module interacts with the database collection"""

from application import *
from uuid import uuid4
from bson.binary import Binary, UUID_SUBTYPE

class User(UserMixin):
    def __init__(self, email, username):
        self.email = email
        self.username = username
        self.id = Binary(uuid4().bytes, UUID_SUBTYPE)

    def get_id(self):
        return str(self.id)
