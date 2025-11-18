from models.base_model import BaseModel

class Subscription(BaseModel):

    def __init__(self, member_id: str, activity_id: str, amount: float):
        super().__init__("subscription")
        self.member_id = member_id
        self.activity_id = activity_id
        self.amount = amount

    def to_dict(self):
        return {
            "id": self.id,
            "member_id": self.member_id,
            "activity_id": self.activity_id,
            "amount": self.amount,
            "created_at": self.created_at
        }
