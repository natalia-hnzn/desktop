class Employee():
    new_id = 1

    def __init__(self, name):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def del_name(self):
        del self._name


e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())


class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        super().say_id()
        print(f"My id is {self.id}")


class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I am an admin.")


class Manager(Admin):
    def say_id(self):
        print("I am in charge!")
        super().say_id()


e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()
e3 = Admin()
e3.say_id()
e4 = Manager()
e4.say_id()


def __dunder__(self):
    return len(self.list_variable)


class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1


class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print("ID {} added.".format(employee.id))
        self.attendees.append(employee)

    # Write your code
    def __len__(self):
        return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))


class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))


class User:
    def __init__(self, username, role="Customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))


class Admin(Employee, User):
    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()
        print("I am an admin.")


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()


class Dog:
    sound = "Woof"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(Dog.sound)


class Dog:
    def bark(self):
        print("Woof!")


class Cat:
    def meow(self):
        print("Meow!")


class Animal:
    def eat(self):
        print("Nom Nom Nom...eating food!")


class Dog(Animal):
    def bark(self):
        print("Bark!")


class Cat(Animal):
    def meow(self):
        print("Meow!")


fluffy = Dog()
zoomie = Cat()

fluffy.eat()  # Nom Nom Nom...eating food!
zoomie.eat()  # Nom Nom Nom...eating food!


class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print("{} says, Grrrr".format(self.name))


pet1 = Animal("Rex")
pet1.make_noise()  # Rex says, Grrrr


class Cat(Animal):
    def make_noise(self):
        print("{} says, Meow!".format(self.name))


pet2 = Cat("Maisy")
pet2.make_noise()  # Maisy says, Meow!


class Animal:
    def __init__(self, name, sound="Grrrr"):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow!")


pet_cat = Cat("Rachel")
pet_cat.make_noise()  # Rachel says, Meow!


class Animal:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("{} says, Hi!".format(self.name))


class Cat(Animal):
    pass


class Angry_Cat(Cat):
    pass


my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi()  # Mr. Cranky says, Hi!


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def action(self):
        print("{} wags tail. Awwww".format(self.name))


class Wolf(Animal):
    def action(self):
        print("{} bites. OUCH!".format(self.name))


class Hybrid(Dog, Wolf):
    def action(self):
        super().action()
        Wolf.action(self)


my_pet = Hybrid("Fluffy")
my_pet.action()  # Fluffy wags tail. Awwww
# Fluffy bites. OUCH!
