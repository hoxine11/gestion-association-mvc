from models.base_model import BaseModel

class Member(BaseModel):
    """
    Represents a registered member in the association.
    """

    def __init__(self, name: str, age: int, phone: str):
        super().__init__(name)
        self.age = age
        self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "created_at": self.created_at
        }
