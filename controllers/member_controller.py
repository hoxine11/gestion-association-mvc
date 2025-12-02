from models.member import Member
from repositories.member_repository import MemberRepository


class MemberController:
    """
    Controller for Member operations.
    Uses Repository Pattern for data access.
    """
    
    def __init__(self):
        self.repository = MemberRepository()
    
    def get_all(self):
        """Get all members"""
        return self.repository.get_all()
    
    def add(self, name: str, age: int, phone: str):
        """Add a new member"""
        member = Member(name, age, phone)
        self.repository.save(member.to_dict())
        print(f"✅ Member added: {name}")
        return member
    
    def find_by_id(self, member_id: str):
        """Find member by ID"""
        return self.repository.find_by_id(member_id)
    
    def find_by_phone(self, phone: str):
        """Find member by phone number"""
        results = self.repository.find_by_phone(phone)
        return results[0] if results else None
    
    def update(self, member_id: str, **kwargs):
        """Update member information"""
        return self.repository.update(member_id, kwargs)
    
    def delete(self, member_id: str):
        """Delete a member"""
        success = self.repository.delete(member_id)
        if success:
            print(f"✅ Member deleted: {member_id}")
        return success
    def update(self, member_id: str, **kwargs):
        """
        Update member information
        Repository Pattern: Delegates to MemberRepository
        """
        success = self.repository.update(member_id, kwargs)
        if success:
            print(f"✅ Member updated: {member_id}")
        return success