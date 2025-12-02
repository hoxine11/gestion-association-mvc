from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """
    Abstract Observer interface.
    
    Design Pattern: Observer Pattern
    Justification:
    - Defines one-to-many dependency between objects
    - When one object changes state, all dependents are notified
    - Promotes loose coupling between subject and observers
    - Easy to add new observers without modifying existing code
    """
    
    @abstractmethod
    def update(self, subject, event_type: str, data: dict):
        """
        Called when the subject notifies observers of a change.
        
        Args:
            subject: The object that triggered the notification
            event_type: Type of event (e.g., "NEW_SUBSCRIPTION")
            data: Additional data about the event
        """
        pass


class Subject:
    """
    Subject (Observable) that maintains a list of observers
    and notifies them of state changes.
    """
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """Register an observer"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"✅ Observer attached: {observer.__class__.__name__}")
    
    def detach(self, observer: Observer):
        """Unregister an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"❌ Observer detached: {observer.__class__.__name__}")
    
    def notify(self, event_type: str, data: dict):
        """Notify all observers about an event"""
        print(f"\n🔔 Event triggered: {event_type}")
        for observer in self._observers:
            observer.update(self, event_type, data)
