from models.instructor import Instructor
from repositories.instructor_repository import InstructorRepository


class InstructorController:
    """
    Controller for Instructor operations.
    Uses Repository Pattern for data access.
    """
    
    def __init__(self):
        self.repository = InstructorRepository()
    
    def get_all(self):
        """Get all instructors"""
        return self.repository.get_all()
    
    def add(self, name: str, specialty: str):
        """Add a new instructor"""
        instructor = Instructor(name, specialty)
        self.repository.save(instructor.to_dict())
        print(f"✅ Instructor added: {name}")
        return instructor
    
    def find_by_id(self, instructor_id: str):
        """Find instructor by ID"""
        return self.repository.find_by_id(instructor_id)
    
    def find_by_specialty(self, specialty: str):
        """Find instructors by specialty"""
        return self.repository.find_by_specialty(specialty)
    
    def update(self, instructor_id: str, **kwargs):
        """Update instructor information"""
        return self.repository.update(instructor_id, kwargs)
    
    def delete(self, instructor_id: str):
        """Delete an instructor"""
        success = self.repository.delete(instructor_id)
        if success:
            print(f"✅ Instructor deleted: {instructor_id}")
        return success
    def update(self, instructor_id: str, **kwargs):
        """
        Update instructor information
        Repository Pattern: Delegates to InstructorRepository
        """
        success = self.repository.update(instructor_id, kwargs)
        if success:
            print(f"✅ Instructor updated: {instructor_id}")
        return success
