class Book:
    def __init__(self,  name):
        self.name = name
    
    
learning_python = Book('learning python in 100days ')

print(learning_python.name)


class Planet:
    def __init__(self, name): pass
    def __init__(self): pass
 
planet = Planet()





class Planet:
    def __init__(self, name="Earth"):
        self.name = name
 
planet1 = Planet()
print(planet1.name)  # Output: "Earth"
planet2 = Planet("Jupiter")
print(planet2.name)  # Output: "Jupiter"


class Planet:
    def __init__(self, name="Earth"):
        self.name = name
        self.speed = 10
        self.distance_from_sun = 10000
 
planet = Planet()
 
print(planet.speed)  # Output: 10
 
print(planet.distance_from_sun)  # Output: 10000