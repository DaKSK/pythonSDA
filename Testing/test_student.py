from student import Student


def test_class_student():
    # input
    name = "Jaan"
    age = 33

    # process
    student = Student(name, age)

    # assert
    assert isinstance(student, Student) is not None


def test_when_student_not_approved():
    # input
    name = "Paul"
    age= 22
    grade = 6

    # process
    student = Student(name, age, grade)

    # assert
    student.name = "Paul"
    student.age = 22
    student.grade = 6
    student.is_approved() is False
