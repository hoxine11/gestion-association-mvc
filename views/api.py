from fastapi import FastAPI
from controllers.member_controller import MemberController
from controllers.instructor_controller import InstructorController
from controllers.activity_controller import ActivityController
from controllers.subscription_controller import SubscriptionController

app = FastAPI(title="Association Management MVC API")

member_controller = MemberController()
instructor_controller = InstructorController()
activity_controller = ActivityController()
subscription_controller = SubscriptionController()

@app.get("/members")
def get_members():
    return member_controller.get_all()

@app.post("/members")
def add_member(name: str, age: int, phone: str):
    member = member_controller.add(name, age, phone)
    return member.to_dict()

@app.delete("/members/{member_id}")
def delete_member(member_id: str):
    success = member_controller.delete(member_id)
    return {"deleted": success}

@app.get("/instructors")
def get_instructors():
    return instructor_controller.get_all()

@app.post("/instructors")
def add_instructor(name: str, specialty: str):
    instructor = instructor_controller.add(name, specialty)
    return instructor.to_dict()

@app.delete("/instructors/{instructor_id}")
def delete_instructor(instructor_id: str):
    return {"deleted": instructor_controller.delete(instructor_id)}

@app.get("/activities")
def get_activities():
    return activity_controller.get_all()

@app.post("/activities")
def add_activity(name: str, category: str, instructor_id: str):
    activity = activity_controller.add(name, category, instructor_id)
    return activity.to_dict()

@app.delete("/activities/{activity_id}")
def delete_activity(activity_id: str):
    return {"deleted": activity_controller.delete(activity_id)}

@app.get("/subscriptions")
def get_subscriptions():
    return subscription_controller.get_all()

@app.get("/subscriptions/member/{member_id}")
def get_member_subscriptions(member_id: str):
    return subscription_controller.find_by_member(member_id)

@app.post("/subscriptions")
def add_subscription(member_id: str, activity_id: str, amount: float):
    subscription = subscription_controller.add(member_id, activity_id, amount)
    return subscription.to_dict()

@app.delete("/subscriptions/{subscription_id}")
def delete_subscription(subscription_id: str):
    return {"deleted": subscription_controller.delete(subscription_id)}