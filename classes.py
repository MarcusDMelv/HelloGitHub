# Todo Classes
# create a class
class Car_With_Flat_Tire:
    # 'pass' tell python this class is empty
    pass


class Car:
    # class attributes are the same for every instance created
    driver = 'Marcus D Melvin'
    age = '30'

    # initializer is called when object is instantiated
    # init is mandatory
    # python calls this function
    def __init__(self, car_type, model, top_speed, color):
        # instance attributes
        # self tells python to assign to current obj being created
        self.car_type = car_type
        self.model = model
        self.top_speed = top_speed
        self.color = color

    # todo instance methods
    # adding methods / functions that belong to class
    # behaviors
    # include self
    def description(self):
        # no printing directly to console
        return 'Type:{}\nCar Model:{}\nColor:{}\nTop Speed:{}'.format(self.car_type, self.model, self.color,
                                                                      self.top_speed)

    # add a new parameter to the instance method
    def engine_sound(self, sound):
        # no print add new parameter
        return 'Your {} has a top speed of {}mph! {}'.format(self.model, self.top_speed, sound)

    def engine_upgrade(self):
        self.top_speed += 1
        return 'Engine Upgrade! New Top Speed {}'.format(self.top_speed)


"""
# object created
print(Car_With_Flat_Tire())

# different objects created
a = Car_With_Flat_Tire()
b = Car_With_Flat_Tire()
print(a)
print(b)

# different objects have been created PROOF:
print(a == b)
"""
# todo Basic use with classes
"""
# using Car class
ford = Car('Ford', 'Fusion', 125, 'Black')
dodge = Car('Dodge', 'Challenger', 185, 'Black')
print(dodge.color)

# changing instances AND class attributes after creation
dodge.color = 'Red'
print(dodge.color)
dodge.driver = 'Not Owned'

# using instances attributes after creation
my_car1 = 'What I have is an {} {} that goes {}mph! '.format(dodge.color, dodge.car_type, dodge.top_speed)
my_car = 'What I have is an {} {} that does about {}mph!'.format(ford.color, ford.car_type, ford.top_speed)

# using class attributes driver
if dodge.driver == 'Marcus D Melvin':
    print(my_car1)
if ford.driver == 'Marcus D Melvin':
    print(my_car)
"""
# todo more adv use with Car() instances

# using Car class
ford = Car('Ford', 'Fusion', 125, 'Black')
dodge = Car('Dodge', 'Challenger', 185, 'Black')
chevy = Car('Chevy', 'Camero', 160, 'Black')
# run first instance method
print(chevy.description())
# run second instance method must enter added parameter
print(chevy.engine_sound('VROOM!'))

# engine upgrade adds +1 to top speed
print(chevy.engine_upgrade())
print(chevy.top_speed)



