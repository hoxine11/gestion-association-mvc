from abc import ABC
from typing import List, Dict, Optional
from utils.csv_loader import read_csv, write_csv


class BaseRepository(ABC):
    """
    Abstract repository implementing common CRUD operations.
    
    Design Pattern: Repository Pattern
    Justification: 
    - Abstracts data access logic from business logic
    - Provides centralized data access
    - Easy to switch between CSV, JSON, MySQL without changing controllers
    - Follows Single Responsibility Principle (SOLID)
    """
    
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def get_all(self) -> List[Dict]:
        """Retrieve all records from data source"""
        return read_csv(self.filepath)
    
    def find_by_id(self, entity_id: str) -> Optional[Dict]:
        """Find a single record by ID"""
        for record in self.get_all():
            if record["id"] == entity_id:
                return record
        return None
    
    def save(self, entity_dict: Dict) -> Dict:
        """Add a new record to data source"""
        data = self.get_all()
        data.append(entity_dict)
        write_csv(self.filepath, data)
        return entity_dict
    
    def update(self, entity_id: str, updated_data: Dict) -> bool:
        """Update an existing record"""
        data = self.get_all()
        for i, record in enumerate(data):
            if record["id"] == entity_id:
                data[i].update(updated_data)
                write_csv(self.filepath, data)
                return True
        return False
    
    def delete(self, entity_id: str) -> bool:
        """Delete a record by ID"""
        data = self.get_all()
        new_data = [record for record in data if record["id"] != entity_id]
        if len(data) != len(new_data):
            write_csv(self.filepath, new_data)
            return True
        return False
    
    def find_by(self, **criteria) -> List[Dict]:
        """
        Find records matching criteria
        Example: find_by(name="Ahmed", age="25")
        """
        results = []
        for record in self.get_all():
            match = all(str(record.get(key)) == str(value) for key, value in criteria.items())
            if match:
                results.append(record)
        return results
