from repositories.base_repository import BaseRepository


class InstructorRepository(BaseRepository):
    """
    Repository for Instructor data access.
    """
    
    def __init__(self):
        super().__init__("data/instructors.csv")
    
    def find_by_specialty(self, specialty: str):
        """Find instructors by specialty"""
        return self.find_by(specialty=specialty)
