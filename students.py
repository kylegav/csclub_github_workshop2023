from majors import Major

class Student:
    def __init__(self,student_id: int, first_name: str, last_name: str,
                 age: int, major: Major):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.active_courses = []


    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} \nMajor: {self.major.name}" \
               f"\n ================="



