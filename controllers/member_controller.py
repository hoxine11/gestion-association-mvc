from models.member import Member
from utils.csv_loader import read_csv, write_csv

class MemberController:

    FILEPATH = "data/members.csv"

    def get_all(self):
        return read_csv(self.FILEPATH)

    def add(self, name: str, age: int, phone: str):
        member = Member(name, age, phone)
        data = self.get_all()
        data.append(member.to_dict())
        write_csv(self.FILEPATH, data)
        return member

    def find_by_id(self, member_id: str):
        for m in self.get_all():
            if m["id"] == member_id:
                return m
        return None

    def delete(self, member_id: str):
        data = self.get_all()
        new_data = [m for m in data if m["id"] != member_id]
        write_csv(self.FILEPATH, new_data)
        return len(data) != len(new_data)
