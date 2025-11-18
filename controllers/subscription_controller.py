from models.subscription import Subscription
from utils.csv_loader import read_csv, write_csv

class SubscriptionController:

    FILEPATH = "data/subscription.csv"  

    def get_all(self):
        return read_csv(self.FILEPATH)

    def add(self, member_id: str, activity_id: str, amount: float):
        subscription = Subscription(member_id, activity_id, amount)
        data = self.get_all()
        data.append(subscription.to_dict())
        write_csv(self.FILEPATH, data)
        return subscription

    def find_by_member(self, member_id: str):
        return [s for s in self.get_all() if s["member_id"] == member_id]

    def delete(self, subscription_id: str):
        data = self.get_all()
        new_data = [s for s in data if s["id"] != subscription_id]
        write_csv(self.FILEPATH, new_data)
        return len(data) != len(new_data)