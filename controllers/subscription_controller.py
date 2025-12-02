from models.subscription import Subscription
from repositories.subscription_repository import SubscriptionRepository
from repositories.member_repository import MemberRepository
from repositories.activity_repository import ActivityRepository
from patterns.observer import Subject
from patterns.activity_observers import LogObserver, EmailObserver, SMSObserver


class SubscriptionController(Subject):
    """
    Controller for Subscription operations.
    Uses Repository Pattern + Observer Pattern.
    Notifies observers when subscriptions are created/cancelled.
    """
    
    def __init__(self):
        super().__init__()
        self.repository = SubscriptionRepository()
        self.member_repo = MemberRepository()
        self.activity_repo = ActivityRepository()
        
        # Attach observers for subscription events
        self.attach(LogObserver())
        self.attach(EmailObserver())
        self.attach(SMSObserver())
    
    def get_all(self):
        """Get all subscriptions"""
        return self.repository.get_all()
    
    def add(self, member_id: str, activity_id: str, amount: float):
        """
        Add a new subscription and notify observers.
        This is where Observer Pattern is most useful!
        """
        # Create subscription
        subscription = Subscription(member_id, activity_id, amount)
        self.repository.save(subscription.to_dict())
        
        # Get additional info for notification
        member = self.member_repo.find_by_id(member_id)
        activity = self.activity_repo.find_by_id(activity_id)
        total_subs = len(self.repository.find_by_activity(activity_id))
        
        # Notify all observers
        self.notify("NEW_SUBSCRIPTION", {
            "member_name": member.get("name") if member else "Unknown",
            "activity_name": activity.get("name") if activity else "Unknown",
            "amount": amount,
            "total_subscribers": total_subs
        })
        
        print(f"✅ Subscription created successfully")
        return subscription
    
    def find_by_member(self, member_id: str):
        """Get all subscriptions for a member"""
        return self.repository.find_by_member(member_id)
    
    def find_by_activity(self, activity_id: str):
        """Get all subscriptions for an activity"""
        return self.repository.find_by_activity(activity_id)
    
    def cancel(self, subscription_id: str):
        """Cancel a subscription and notify observers"""
        # Get subscription info before deleting
        subscription = self.repository.find_by_id(subscription_id)
        if not subscription:
            return False
        
        member = self.member_repo.find_by_id(subscription.get("member_id"))
        activity = self.activity_repo.find_by_id(subscription.get("activity_id"))
        
        # Delete subscription
        success = self.repository.delete(subscription_id)
        
        if success:
            # Notify observers
            self.notify("SUBSCRIPTION_CANCELLED", {
                "member_name": member.get("name") if member else "Unknown",
                "activity_name": activity.get("name") if activity else "Unknown"
            })
            print(f"✅ Subscription cancelled")
        
        return success
    
    def delete(self, subscription_id: str):
        """Delete a subscription"""
        return self.repository.delete(subscription_id)
