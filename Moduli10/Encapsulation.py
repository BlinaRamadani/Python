class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get__name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


student1 = Student("Nita", 18)

print("Name: ", student1.get__name())
student1.set_name("Arianita")
print("Updated Name: ", student1.get__name())

print("Age: ", student1.get_age())
student1.set_age(20)
print("Updated Age: ", student1.get_age())


