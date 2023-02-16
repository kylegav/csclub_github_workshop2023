from students import Student
from majors import Major

#Lists to store our Student and Major objects, these can be added to with .append or .extend(iterable object)
list_of_majors = []
list_of_active_students = []

#These functions will initalize a set of starting majors and starting students to choose from.
def major_init():
    csci = Major(720392,"Computer Science","PEMACS")
    info = Major(721392,"Information Technology", "PEMACS")
    engr = Major(722440,"Engineering","PEMACS")
    bizz_admin = Major(440192, "Business Administration","College of Business")
    nursing = Major(701621,"Nursing Science","College of Nursing and Public Health")
    list_of_majors.extend([csci, info, engr, bizz_admin, nursing])

def student_init():
    stud1 = Student(10574211,"Jameel","Bryce",24, list_of_majors[0])
    stud2 = Student(10521823,"Stephon","Fonrose", 25, list_of_majors[0])
    stud3 = Student(10615734,"Nick","Rose", 22, list_of_majors[1])
    stud4 = Student(10633211, "Dorian","Freeman", 26, list_of_majors[3])
    stud5 = Student(10655321,"Mary","Jones", 21, list_of_majors[4])
    list_of_active_students.extend([stud1,stud2,stud3,stud4,stud5])


#These functions will display the Objects using the __str__ print format defined in the object class
def display_majors():
    for major in list_of_majors:
        print(major)

def display_students():
    for student in list_of_active_students:
        print(student)


#These functions will create an instance of a new Student or Object
def create_new_student(student_id: int, first_name: str, last_name: str, age: int, major: Major) -> Major:
    new_student = Student(student_id, first_name, last_name, age, major)
    return new_student

def create_new_major(department_id: int, name: str, division: str) -> Major:
    new_major = Major(department_id, name, division)
    return new_major





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Under this statement, interact with all the main.py functions, and work with creating new students, majors, and courses.
    major_init()
    student_init()
    display_students()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
