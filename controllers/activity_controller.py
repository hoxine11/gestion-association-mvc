from models.activity import Activity
from utils.csv_loader import read_csv, write_csv

class ActivityController:

    FILEPATH = "data/activities.csv"

    def get_all(self):
        return read_csv(self.FILEPATH)

    def add(self, name: str, category: str, instructor_id: str):
        activity = Activity(name, category, instructor_id)
        data = self.get_all()
        data.append(activity.to_dict())
        write_csv(self.FILEPATH, data)
        return activity

    def find_by_id(self, activity_id: str):
        for a in self.get_all():
            if a["id"] == activity_id:
                return a
        return None

    def delete(self, activity_id: str):
        data = self.get_all()
        new_data = [a for a in data if a["id"] != activity_id]
        write_csv(self.FILEPATH, new_data)
        return len(data) != len(new_data)
