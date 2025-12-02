from repositories.base_repository import BaseRepository


class SubscriptionRepository(BaseRepository):
    """
    Repository for Subscription data access.
    """
    
    def __init__(self):
        super().__init__("data/subscription.csv")
    
    def find_by_member(self, member_id: str):
        """Get all subscriptions for a specific member"""
        return self.find_by(member_id=member_id)
    
    def find_by_activity(self, activity_id: str):
        """Get all subscriptions for a specific activity"""
        return self.find_by(activity_id=activity_id)
