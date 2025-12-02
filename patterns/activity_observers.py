from patterns.observer import Observer
from datetime import datetime


class LogObserver(Observer):
    """
    Observer that writes system logs to a file.
    Useful for debugging and tracking system events.
    """
    
    def update(self, subject, event_type: str, data: dict):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {event_type}: {data}"
        
        # Print to console
        print(f"📝 LOG: {log_message}")
        
        # Write to log file
        try:
            with open("data/system.log", "a", encoding="utf-8") as f:
                f.write(log_message + "\n")
        except Exception as e:
            print(f"❌ Error writing log: {e}")


class EmailObserver(Observer):
    """
    Observer that simulates sending email notifications.
    In production, this would integrate with an email service.
    """
    
    def update(self, subject, event_type: str, data: dict):
        if event_type == "NEW_SUBSCRIPTION":
            member_name = data.get('member_name', 'Unknown')
            activity_name = data.get('activity_name', 'Unknown')
            print(f"📧 EMAIL SENT to {member_name}:")
            print(f"   Subject: Subscription Confirmation")
            print(f"   Message: You have successfully subscribed to '{activity_name}'")
        
        elif event_type == "ACTIVITY_CANCELLED":
            activity_name = data.get('activity_name', 'Unknown')
            member_count = data.get('member_count', 0)
            print(f"📧 EMAIL SENT to {member_count} members:")
            print(f"   Subject: Activity Cancelled")
            print(f"   Message: '{activity_name}' has been cancelled")
        
        elif event_type == "ACTIVITY_UPDATED":
            activity_name = data.get('activity_name', 'Unknown')
            print(f"📧 EMAIL SENT:")
            print(f"   Subject: Activity Update")
            print(f"   Message: '{activity_name}' details have been updated")
        
        elif event_type == "SUBSCRIPTION_CANCELLED":
            member_name = data.get('member_name', 'Unknown')
            activity_name = data.get('activity_name', 'Unknown')
            print(f"📧 EMAIL SENT to {member_name}:")
            print(f"   Subject: Subscription Cancelled")
            print(f"   Message: Your subscription to '{activity_name}' has been cancelled")


class SMSObserver(Observer):
    """
    Observer that simulates sending SMS notifications.
    In production, this would integrate with an SMS gateway.
    """
    
    def update(self, subject, event_type: str, data: dict):
        if event_type == "NEW_SUBSCRIPTION":
            member_name = data.get('member_name', 'Unknown')
            activity_name = data.get('activity_name', 'Unknown')
            print(f"📱 SMS SENT to {member_name}:")
            print(f"   Subscription confirmed: {activity_name}")
        
        elif event_type == "ACTIVITY_CANCELLED":
            activity_name = data.get('activity_name', 'Unknown')
            member_count = data.get('member_count', 0)
            print(f"📱 SMS SENT to {member_count} members:")
            print(f"   ALERT: {activity_name} cancelled")
        
        elif event_type == "SUBSCRIPTION_CANCELLED":
            print(f"📱 SMS SENT:")
            print(f"   Your subscription has been cancelled")
