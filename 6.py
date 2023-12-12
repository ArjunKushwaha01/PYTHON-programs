class Student:
    def __init__(self):
        self.marks = []

    def enter_marks(self):
        for i in range(3):
            mark = float(input(f"Enter mark for subject {i + 1}: "))
            self.marks.append(mark)

    def check_result(self):
        pass_mark = 40
        for mark in self.marks:
            if mark < pass_mark:
                print("Failed")
                return
        print("Passed")

# Creating an object of the Student class
student = Student()

# Reading marks for three subjects
student.enter_marks()

# Checking and displaying pass or failed
student.check_result()
