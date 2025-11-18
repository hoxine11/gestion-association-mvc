from models.instructor import Instructor
from utils.csv_loader import read_csv, write_csv

class InstructorController:

    FILEPATH = "data/instructors.csv"

    def get_all(self):
        return read_csv(self.FILEPATH)

    def add(self, name: str, specialty: str):
        instructor = Instructor(name, specialty)
        data = self.get_all()
        data.append(instructor.to_dict())
        write_csv(self.FILEPATH, data)
        return instructor

    def find_by_id(self, instructor_id: str):
        for i in self.get_all():
            if i["id"] == instructor_id:
                return i
        return None

    def delete(self, instructor_id: str):
        data = self.get_all()
        new_data = [i for i in data if i["id"] != instructor_id]
        write_csv(self.FILEPATH, new_data)
        return len(data) != len(new_data)
