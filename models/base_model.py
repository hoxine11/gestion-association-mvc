from abc import ABC, abstractmethod
from datetime import datetime
import uuid

class BaseModel(ABC):
    """
    Abstract base model for all entities (Member, Instructor, Activity, etc.)
    """

    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  
        self.name = name
        self.created_at = datetime.now().isoformat()

    @abstractmethod
    def to_dict(self):
        """Return dictionary representation for CSV/JSON"""
        pass
