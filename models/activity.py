from models.base_model import BaseModel

class Activity(BaseModel):
    """
    Represents an activity in the association.
    """

    def __init__(self, name: str, category: str, instructor_id: str):
        super().__init__(name)
        self.category = category
        self.instructor_id = instructor_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "instructor_id": self.instructor_id,
            "created_at": self.created_at
        }
