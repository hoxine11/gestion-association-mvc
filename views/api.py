from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from controllers.member_controller import MemberController
from controllers.instructor_controller import InstructorController
from controllers.activity_controller import ActivityController
from controllers.subscription_controller import SubscriptionController


app = FastAPI()


# Initialize controllers (with Repository Pattern)
member_ctrl = MemberController()
instructor_ctrl = InstructorController()
activity_ctrl = ActivityController()
subscription_ctrl = SubscriptionController()


# ============================================
# Pydantic Models (Request/Response schemas)
# ============================================

class MemberCreate(BaseModel):
    name: str
    age: int
    phone: str


class InstructorCreate(BaseModel):
    name: str
    specialty: str


class ActivityCreate(BaseModel):
    name: str
    category: str
    instructor_id: str


class SubscriptionCreate(BaseModel):
    member_id: str
    activity_id: str
    amount: float


# ============================================
# MEMBER ENDPOINTS
# ============================================

@app.get("/members")
async def get_all_members():
    """Get all members (using Repository Pattern)"""
    return member_ctrl.get_all()


@app.post("/members")
async def create_member(member: MemberCreate):
    """Create a new member"""
    new_member = member_ctrl.add(member.name, member.age, member.phone)
    return {"message": "Member created", "data": new_member.to_dict()}


@app.get("/members/{member_id}")
async def get_member(member_id: str):
    """Get member by ID"""
    member = member_ctrl.find_by_id(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@app.delete("/members/{member_id}")
async def delete_member(member_id: str):
    """Delete a member"""
    success = member_ctrl.delete(member_id)
    if not success:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member deleted successfully"}


# ============================================
# INSTRUCTOR ENDPOINTS
# ============================================

@app.get("/instructors")
async def get_all_instructors():
    """Get all instructors (using Repository Pattern)"""
    return instructor_ctrl.get_all()


@app.post("/instructors")
async def create_instructor(instructor: InstructorCreate):
    """Create a new instructor"""
    new_instructor = instructor_ctrl.add(instructor.name, instructor.specialty)
    return {"message": "Instructor created", "data": new_instructor.to_dict()}


@app.get("/instructors/{instructor_id}")
async def get_instructor(instructor_id: str):
    """Get instructor by ID"""
    instructor = instructor_ctrl.find_by_id(instructor_id)
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


@app.delete("/instructors/{instructor_id}")
async def delete_instructor(instructor_id: str):
    """Delete an instructor"""
    success = instructor_ctrl.delete(instructor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return {"message": "Instructor deleted successfully"}


# ============================================
# ACTIVITY ENDPOINTS
# ============================================

@app.get("/activities")
async def get_all_activities():
    """Get all activities (using Repository Pattern)"""
    return activity_ctrl.get_all()


@app.post("/activities")
async def create_activity(activity: ActivityCreate):
    """
    Create a new activity
    Triggers Observer Pattern: LogObserver, EmailObserver, SMSObserver
    """
    new_activity = activity_ctrl.add(
        activity.name,
        activity.category,
        activity.instructor_id
    )
    return {"message": "Activity created", "data": new_activity.to_dict()}


@app.get("/activities/{activity_id}")
async def get_activity(activity_id: str):
    """Get activity by ID"""
    activity = activity_ctrl.find_by_id(activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@app.put("/activities/{activity_id}/cancel")
async def cancel_activity(activity_id: str):
    """
    Cancel an activity
    Triggers Observer Pattern: Notifies all subscribed members
    """
    success = activity_ctrl.cancel(activity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Activity not found")
    return {"message": "Activity cancelled, observers notified"}


@app.delete("/activities/{activity_id}")
async def delete_activity(activity_id: str):
    """Delete an activity"""
    success = activity_ctrl.delete(activity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Activity not found")
    return {"message": "Activity deleted successfully"}


# ============================================
# SUBSCRIPTION ENDPOINTS
# ============================================

@app.get("/subscriptions")
async def get_all_subscriptions():
    """Get all subscriptions (using Repository Pattern)"""
    return subscription_ctrl.get_all()


@app.post("/subscriptions")
async def create_subscription(subscription: SubscriptionCreate):
    """
    Create a new subscription
    Triggers Observer Pattern: LogObserver, EmailObserver, SMSObserver
    This is the main demonstration of Observer Pattern!
    """
    new_subscription = subscription_ctrl.add(
        subscription.member_id,
        subscription.activity_id,
        subscription.amount
    )
    return {
        "message": "Subscription created, observers notified",
        "data": new_subscription.to_dict()
    }


@app.get("/subscriptions/member/{member_id}")
async def get_member_subscriptions(member_id: str):
    """Get all subscriptions for a specific member"""
    subscriptions = subscription_ctrl.find_by_member(member_id)
    return subscriptions


@app.get("/subscriptions/activity/{activity_id}")
async def get_activity_subscriptions(activity_id: str):
    """Get all subscriptions for a specific activity"""
    subscriptions = subscription_ctrl.find_by_activity(activity_id)
    return subscriptions


@app.delete("/subscriptions/{subscription_id}")
async def cancel_subscription(subscription_id: str):
    """
    Cancel a subscription
    Triggers Observer Pattern: Notifies member and instructor
    """
    success = subscription_ctrl.cancel(subscription_id)
    if not success:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"message": "Subscription cancelled, observers notified"}


# ============================================
# STATISTICS ENDPOINT
# ============================================

@app.get("/statistics")
async def get_statistics():
    """Get system statistics"""
    members = member_ctrl.get_all()
    instructors = instructor_ctrl.get_all()
    activities = activity_ctrl.get_all()
    subscriptions = subscription_ctrl.get_all()
    
    return {
        "total_members": len(members),
        "total_instructors": len(instructors),
        "total_activities": len(activities),
        "total_subscriptions": len(subscriptions),
        "patterns_used": [
            {
                "name": "Repository Pattern",
                "purpose": "Data access abstraction",
                "implementation": "BaseRepository + specific repositories"
            },
            {
                "name": "Observer Pattern",
                "purpose": "Event notification system",
                "implementation": "Subject + LogObserver + EmailObserver + SMSObserver"
            }
        ]
    }


# ============================================
# ROOT ENDPOINT
# ============================================

@app.get("/")
async def api_root():
    """API information"""
    return {
        "message": "Association Management API",
        "version": "1.0.0",
        "architecture": "MVC",
        "patterns": ["Repository Pattern", "Observer Pattern"],
        "documentation": "/docs",
        "endpoints": {
            "members": "/members",
            "instructors": "/instructors",
            "activities": "/activities",
            "subscriptions": "/subscriptions",
            "statistics": "/statistics"
        }
    }
# ============================================
# MEMBER UPDATE ENDPOINT
# ============================================

class MemberUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    phone: str | None = None


@app.put("/members/{member_id}")
def update_member(member_id: str, member: MemberUpdate):
    """
    Update member information
    Repository Pattern: Uses MemberRepository.update()
    """
    existing_member = member_controller.find_by_id(member_id)
    if not existing_member:
        raise HTTPException(status_code=404, detail="Member not found")
    
    # Prepare update data (only non-None fields)
    update_data = {k: v for k, v in member.dict().items() if v is not None}
    
    success = member_controller.update(member_id, **update_data)
    if success:
        updated_member = member_controller.find_by_id(member_id)
        return {
            "message": "Member updated successfully",
            "data": updated_member
        }
    return {"error": "Update failed"}


# ============================================
# INSTRUCTOR UPDATE ENDPOINT
# ============================================

class InstructorUpdate(BaseModel):
    name: str | None = None
    specialty: str | None = None


@app.put("/instructors/{instructor_id}")
def update_instructor(instructor_id: str, instructor: InstructorUpdate):
    """
    Update instructor information
    Repository Pattern: Uses InstructorRepository.update()
    """
    existing_instructor = instructor_controller.find_by_id(instructor_id)
    if not existing_instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    
    update_data = {k: v for k, v in instructor.dict().items() if v is not None}
    
    success = instructor_controller.update(instructor_id, **update_data)
    if success:
        updated_instructor = instructor_controller.find_by_id(instructor_id)
        return {
            "message": "Instructor updated successfully",
            "data": updated_instructor
        }
    return {"error": "Update failed"}


# ============================================
# ACTIVITY UPDATE ENDPOINT
# ============================================

class ActivityUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    instructor_id: str | None = None


@app.put("/activities/{activity_id}")
def update_activity(activity_id: str, activity: ActivityUpdate):
    """
    Update activity information
    Repository Pattern: Uses ActivityRepository.update()
    Observer Pattern: Notifies observers about the update
    """
    existing_activity = activity_controller.find_by_id(activity_id)
    if not existing_activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    update_data = {k: v for k, v in activity.dict().items() if v is not None}
    
    success = activity_controller.update(activity_id, **update_data)
    if success:
        updated_activity = activity_controller.find_by_id(activity_id)
        return {
            "message": "Activity updated successfully, observers notified",
            "data": updated_activity
        }
    return {"error": "Update failed"}


# ============================================
# SUBSCRIPTION UPDATE ENDPOINT
# ============================================

class SubscriptionUpdate(BaseModel):
    amount: float | None = None


@app.put("/subscriptions/{subscription_id}")
def update_subscription(subscription_id: str, subscription: SubscriptionUpdate):
    """
    Update subscription information (mainly amount)
    Repository Pattern: Uses SubscriptionRepository.update()
    """
    existing_subscription = subscription_controller.repository.find_by_id(subscription_id)
    if not existing_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    update_data = {k: v for k, v in subscription.dict().items() if v is not None}
    
    success = subscription_controller.repository.update(subscription_id, **update_data)
    if success:
        updated_subscription = subscription_controller.repository.find_by_id(subscription_id)
        return {
            "message": "Subscription updated successfully",
            "data": updated_subscription
        }
    return {"error": "Update failed"}
