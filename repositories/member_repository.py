from repositories.base_repository import BaseRepository


class MemberRepository(BaseRepository):
    """
    Repository for Member data access.
    Inherits all CRUD operations from BaseRepository.
    """
    
    def __init__(self):
        super().__init__("data/members.csv")
    
    def find_by_phone(self, phone: str):
        """Find member by phone number"""
        return self.find_by(phone=phone)
    
    def find_by_name(self, name: str):
        """Find members by name"""
        return self.find_by(name=name)
