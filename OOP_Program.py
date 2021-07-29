# to abstract methods must import libs
from abc import ABC, abstractmethod


# todo abstraction part1
# use ABC to identify abstraction class
# this class could be used in all classes
class Felidae(ABC):
    # abstract decorator
    @abstractmethod
    def family_description(self):
        pass

    @abstractmethod
    def species(self):
        pass


# todo using abstract
class Panthera(Felidae):
    def __init__(self):
        # todo Encapsulation part1
        self._random_fact = 'Felinae is a domestic cat that is part of the same Panthera family\nas the big cats?!'
        # todo Encapsulation part2
        self._sound = 'ROARS!'
    def family_description(self):
        return 'Panthera is a genus within the family Felidae that was named and described by\nLorenz Oken in 1816 who' \
               'placed all the spotted cats in this group.Reginald Innes Pocock\nrevised the classification of ' \
               'this genus in 1916 as comprising the species tiger, lion, \njaguar' \
               'and leopard.'

    def species(self):
        return '\n1.)Tigers\n2.)Lion\n3.)Jaguar\n4.)Leopard\n'


# todo Inheritance part 1
# TODO ENCAPSULATION part 2
class BigCat(Panthera):
    # constructor with big type and name as added attributes to the class
    def __init__(self, big_cat_type, name):
        self.name = name
        self.big_cat_type = big_cat_type
        # todo encapsulation
        Panthera.__init__(self)
        print('Random Fact about {}s: {} '.format(self.big_cat_type, self._random_fact))
        print('{} {} like every other big cat in the Panthera family'.format(self.name, self._sound))

    def description(self):
        return '{} is a {}'.format(self.name, self.big_cat_type)

    # todo setting up polymorphism
    def hunting(self):
        return ' likes to hunt alone.'

    def food(self):
        return 'They will try to eat you run!'


# todo Inheritance part 2
class Tiger(BigCat):
    # todo setting up polymorphism
    def hunting(self):
        return 'likes to hunt alone.'

    def food(self):
        return ' They will try to eat you run!'


# todo polymorphism part 1
class Lion(Tiger):
    # TODO POLYMORPHISM
    def hunting(self):
        return 'likes to hunt as a group better know as a Pride.'


# TODO ENCAPSULATION
# _sound , _ random_fact
print('\nInstance of Tiger() class')
big_cat1 = Tiger('Tiger', 'Shellie')
print('\nInstance of Lion() class')
big_cat2 = Lion('Lion', 'Rocko')
# todo POLYMORPHISM
print('\nPOLYMORPHISM:')
print('{} {} {}'.format(big_cat1.big_cat_type,big_cat1.hunting(),big_cat1.food()))
print('{} {} {}\n'.format(big_cat2.big_cat_type,big_cat2.hunting(),big_cat1.food()))
# todo INHERITANCE from Panthera class which ABSTRACTS from Felidae class
print('\nINHERITANCE:')
print('{} Panthera Family: {}'.format(big_cat1.big_cat_type, big_cat1.species()))
print('{} Panthera Family: {}'.format(big_cat2.big_cat_type, big_cat2.species()))
