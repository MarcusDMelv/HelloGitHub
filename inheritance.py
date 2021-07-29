# todo inheritance
# creating a family using inheritance
# Parent Class / Child Class
# child class inherits from parent class
# child class will automatically inherit from the parent class
# child class can have their own attributes and methods
class Person:
    description = 'Adult'
    last_name = 'Melvin'

    # attributes of every instance
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def speak(self):
        print('My name is {} and I am {} years old'.format(self.name, self.age))

    def job(self, job):
        print('{} is an {}'.format(self.name,job))

    def sport(self, sport_played):
        print('When {} was in High School they was a {} star!'.format(self.name, sport_played))


# Subclass/ child class has been created
# Person class is placed in () now Baby class has inherit everything from
# Person class
class Baby(Person):
    description = 'Baby'

    def speak(self):
        print('ba ba ba ba ba')

    def nap(self):
        print('{} is now napping shhhhh'.format(self.name))


dad = Person('Marcus', 30)
print(dad.description)
dad.speak()
dad.job('Computer Programmer')
dad.sport('Football')
print('\n')
son = Baby('Joel', 2)
print(son.description)
son.speak()
print('\n')
print('{} {} is the father to {} {}'.format(dad.name, dad.last_name,son.name,son.last_name))
# function to show instances
print(isinstance(son, Person))

