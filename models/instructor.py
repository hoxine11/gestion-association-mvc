from models.base_model import BaseModel

class Instructor(BaseModel):
    """
    Represents an instructor (teacher).
    """

    def __init__(self, name: str, specialty: str):
        super().__init__(name)
        self.specialty = specialty

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialty": self.specialty,
            "created_at": self.created_at
        }
