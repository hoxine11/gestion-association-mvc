from models.activity import Activity
from repositories.activity_repository import ActivityRepository
from patterns.observer import Subject
from patterns.activity_observers import LogObserver, EmailObserver, SMSObserver


class ActivityController(Subject):
    """
    Controller for Activity operations.
    Uses Repository Pattern + Observer Pattern.
    """
    
    def __init__(self):
        super().__init__()
        self.repository = ActivityRepository()
        
        # Attach observers
        self.attach(LogObserver())
        self.attach(EmailObserver())
        self.attach(SMSObserver())
    
    def get_all(self):
        """Get all activities"""
        return self.repository.get_all()
    
    def add(self, name: str, category: str, instructor_id: str):
        """Add a new activity"""
        activity = Activity(name, category, instructor_id)
        self.repository.save(activity.to_dict())
        print(f"✅ Activity added: {name}")
        
        # Notify observers
        self.notify("ACTIVITY_CREATED", {
            "activity_name": name,
            "category": category
        })
        
        return activity
    
    def find_by_id(self, activity_id: str):
        """Find activity by ID"""
        return self.repository.find_by_id(activity_id)
    
    def find_by_instructor(self, instructor_id: str):
        """Find activities by instructor"""
        return self.repository.find_by_instructor(instructor_id)
    
    def update(self, activity_id: str, **kwargs):
        """Update activity and notify observers"""
        activity = self.repository.find_by_id(activity_id)
        success = self.repository.update(activity_id, kwargs)
        
        if success and activity:
            self.notify("ACTIVITY_UPDATED", {
                "activity_name": activity.get("name"),
                "changes": kwargs
            })
        
        return success
    
    def cancel(self, activity_id: str):
        """Cancel an activity and notify all subscribers"""
        from repositories.subscription_repository import SubscriptionRepository
        
        activity = self.repository.find_by_id(activity_id)
        if not activity:
            return False
        
        # Get all subscriptions for this activity
        sub_repo = SubscriptionRepository()
        subscriptions = sub_repo.find_by_activity(activity_id)
        
        # Notify observers
        self.notify("ACTIVITY_CANCELLED", {
            "activity_name": activity.get("name"),
            "member_count": len(subscriptions)
        })
        
        # Delete activity
        return self.repository.delete(activity_id)
    
    def delete(self, activity_id: str):
        """Delete an activity"""
        success = self.repository.delete(activity_id)
        if success:
            print(f"✅ Activity deleted: {activity_id}")
        return success
    def update(self, activity_id: str, **kwargs):
        """
        Update activity and notify observers
        Repository Pattern + Observer Pattern
        """
        activity = self.repository.find_by_id(activity_id)
        success = self.repository.update(activity_id, kwargs)
    
        if success and activity:
            self.notify("ACTIVITY_UPDATED", {
            "activity_name": activity.get("name"),
            "changes": kwargs
        })
            print(f"✅ Activity updated: {activity_id}")
    
        return success
