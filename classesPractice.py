class Animal:

    def __init__(self,name,age,species):
        self._name = name
        self._age = age
        self._species = species

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self,age):
        self._age = age

    def get_species(self):
        return self._species

    def set_species(self,species):
        self._species = species

    def move(self):
        print("Moving")
    
    def eat(self):
        print("Eating")

class Book:
    def __init__(self,title,author):
        self._title = title
        self._aurthor = author
        
    def get_title(self):
        return self._title

    def set_title(self,title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self,author):
        self._author = author

class Vehicle:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year
        
    def get_make(self):
        return self._make

    def set_make(self,make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self,model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self,year):
        self._year = year

    def drive(self):
        print("Driving")

class Fish(Animal):
    """Fish class, inheriting from Animal"""
    def __init__(self,name,age,fish):
        super().__init__(name)
        super().__init__(age)
        super().__init__(fish)

    def swim(self):
        print("Swimming")

class Snake(Animal):
    """Snake class, inheriting from Animal"""
    def __init__(self,name,age,snake):
        super().__init__(name)
        super().__init__(age)
        super().__init__(snake)

    def slither(self):
        print("Slithering")

    def hiss(self):
        print("Hisssss!")

class Person(Animal):
    """Person class, inheriting from Animal"""
    def __init__(self,name,age,person):
        super().__init__(name)
        super().__init__(age)
        super().__init__(person)

class TextBook(Book):
    """TextBook class, inheriting from Book"""
    def __init__(self,title,author):
        super().__init__(title)
        super().__init__(author)

class AddressBook(Book):
    """AddressBook class, inheriting from Book"""
    def __init__(self,title,author):
        super().__init__(title)
        super().__init__(author)

class Car(Vehicle):
    """Car class, inheriting from Vehicle"""
    def __init__(self,make,model,year):
        super().__init__(make)
        super().__init__(model)
        super().__init__(year)

class Bicycle(Vehicle):
    """Bicycle class, inheriting from Vehicle"""
    def __init__(self,make,model,year):
        super().__init__(make)
        super().__init__(model)
        super().__init__(year)

    def ride(self):
        print("Riding")

class Boat(Vehicle):
    """Boat class, inheriting from Vehicle"""
    def __init__(self,make,model,year):
        super().__init__(make)
        super().__init__(model)
        super().__init__(year)

class HotAirBalloon(Vehicle):
    """Hot Air Balloon class, inheriting from Vehicle"""
    def __init__(self,make,model,year):
        super().__init__(make)
        super().__init__(model)
        super().__init__(year)

    def fly(self):
        print("Flying")