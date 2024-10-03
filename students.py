class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")

student1 = Student("Alice", "REG2024001")
student2 = Student("Bob", "REG2024002")
student3 = Student("Kenneth", "REG202400395")
student4 = Student("Darius", "REG2024006")

student1.display_info()
print()  
student2.display_info()
student3.display_info()
student4.display_info()