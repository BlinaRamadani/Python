class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        print("My name is", self.name, "I am", self.age, "And the email is", self.email)

She = Person ("Blina", "16", "blinaramadani@gmail.com")

print(She.greet())