# 6. Develop a simple OOP-based Python class Student with attributes like name, roll
# number, and marks. Implement methods to input and display details.


class Student:
    def input_details(self):
        self.name = input("Name : ")
        self.roll_number = int(input("Roll number : "))
        self.marks = float(input("Marks : "))

    def display_details(self):
        print("Name = ", self.name)
        print("Roll number = ", self.roll_number)
        print("Marks = ", self.marks)


alisa=  Student()
alisa.input_details()
print()
alisa.display_details()