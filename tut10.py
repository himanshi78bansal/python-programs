class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    
    def talk(self):
        print(f"My name is {self.name}, I'm {self.age} years old, and my roll number is {self.roll_number}.")

# Create a new Student object
s = Student("John", 20, "A001")

# Call the talk function
s.talk()  # Output: My name is John, I'm 20 years old, and my roll number is A001.
