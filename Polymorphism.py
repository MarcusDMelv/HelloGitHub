# The word polymorphism means having many forms.
# In programming, polymorphism means same function name
# (but different signatures) being uses for different types.
# Person.speak != Baby.speak


class Person:
    description = 'Adult'
    last_name = 'Melvin'

    # attributes of every instance
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method I will polymorphism
    def speak(self):
        print('My name is {} and I am {} years old'.format(self.name, self.age))

    def job(self, job):
        print('{} is an {}'.format(self.name, job))

    def sport(self, sport_played):
        print('When {} was in High School they was a {} star!'.format(self.name, sport_played))


# Subclass/ child class has been created
# Person class is placed in () now Baby class has inherit everything from
# Person class
class Baby(Person):
    description = 'Baby'

    # inherit will do something different that is polymorphism
    def speak(self):
        print('ba ba ba ba ba')
