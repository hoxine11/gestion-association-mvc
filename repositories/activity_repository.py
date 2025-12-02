from repositories.base_repository import BaseRepository


class ActivityRepository(BaseRepository):
    """
    Repository for Activity data access.
    """
    
    def __init__(self):
        super().__init__("data/activities.csv")
    
    def find_by_instructor(self, instructor_id: str):
        """Find all activities taught by an instructor"""
        return self.find_by(instructor_id=instructor_id)
    
    def find_by_category(self, category: str):
        """Find activities by category"""
        return self.find_by(category=category)
