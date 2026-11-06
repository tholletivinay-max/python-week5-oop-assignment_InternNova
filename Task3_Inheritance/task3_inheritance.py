
# TASK 3: INHERITANCE IN PYTHON

# Parent class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Common method
    def display_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class inheriting from Person
class Student(Person):

    def __init__(self, name, age, roll_number, department):
        
        # Calling parent class constructor
        super().__init__(name, age)

        self.roll_number = roll_number
        self.department = department

    # Specific method of Student class
    def display_student_details(self):
        print("\nSTUDENT DETAILS")
        print("----------------------------")

        # Inherited method
        self.display_person_details()

        # Child class attributes
        print("Roll Number:", self.roll_number)
        print("Department:", self.department)
        print("----------------------------")


# Creating first student object
student1 = Student("Vinay", 21, 101, "AI & Data Science")

# Creating second student object
student2 = Student("Arun", 22, 102, "Computer Science")

# Displaying student information
print("COLLEGE STUDENT MANAGEMENT SYSTEM")

student1.display_student_details()
student2.display_student_details()
