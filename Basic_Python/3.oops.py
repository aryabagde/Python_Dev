from abc import ABC, abstractmethod


# ===============================
# ABSTRACTION
# ===============================
class Person(ABC):
    def __init__(self, name, age):
        self.name = name          # public
        self._age = age           # protected

    @abstractmethod
    def get_role(self):
        pass

    def display_basic_info(self):
        print("Name:", self.name)
        print("Age:", self._age)


# ===============================
# INHERITANCE
# ===============================
class Student(Person):
    def __init__(self, name, age, roll, cgpa):
        super().__init__(name, age)
        self.roll = roll
        self.__cgpa = cgpa        # private (name mangling)

    # POLYMORPHISM (method overriding)
    def get_role(self):
        return "Student"

    # ENCAPSULATION (getter & setter)
    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self, value):
        if 0 <= value <= 10:
            self.__cgpa = value
        else:
            print("Invalid CGPA")

    def display_student_info(self):
        self.display_basic_info()
        print("Roll:", self.roll)
        print("CGPA:", self.__cgpa)


# ===============================
# ANOTHER CHILD CLASS
# ===============================
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_role(self):
        return "Teacher"

    def display_teacher_info(self):
        self.display_basic_info()
        print("Subject:", self.subject)


# ===============================
# POLYMORPHISM (FUNCTION LEVEL)
# ===============================
def show_role(person):
    print("Role:", person.get_role())


# ===============================
# MAIN EXECUTION
# ===============================
student = Student("Arya", 22, 1, 9.1)
teacher = Teacher("Dr. Rao", 45, "Machine Learning")

# Student info
student.display_student_info()
show_role(student)

print()

# Teacher info
teacher.display_teacher_info()
show_role(teacher)

print()

# Encapsulation demo
print("Original CGPA:", student.get_cgpa())
student.set_cgpa(9.5)
print("Updated CGPA:", student.get_cgpa())

# Direct access test (will fail)
# print(student.__cgpa)   # ❌ AttributeError
