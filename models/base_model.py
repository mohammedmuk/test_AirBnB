import uuid
import datetime


class BaseModel():
    """This is main class for this application"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat("T")
        self.updated_at = self.updated_at.isoformat("T")
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
