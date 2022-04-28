"""
LAB 1 - OOP

Create one class called FruitShop. This class should receive a name which should be a string, and fruits as a list. 
Create also a method called get_fruits_count() which should return amount of fruits in the shop.
Input:
my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
Output: 4
"""
from urllib.parse import ParseResultBytes


class FruitShop:
    def __init__(self, name, fruits_list):
        self.name = name
        self.fruits_list = fruits_list
    def get_fruits_count(self):
        return len(self.fruits_list)

my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
print(my_shop.get_fruits_count())
print(40*"=")
"""
LAB 2 - OOP

Create the following classes: Animal, Horse and Dog.
The Animal class should have a method eat ( ) and it should return "eating.. nom.. nom.."
The Horse class should have a method called neigh ( ) and it should return "neigh! "
The Dog class should have a method called bark ( ) and it should return "voof voof!"
And remember that the Horse and Dog class should inherit form the Animal class.
"""
class Animal:
    def eat(self):
        return print("eating.. nom.. nom..")

class Horse(Animal):
    def neigh(self):
        return print("neigh! ")

class Dog(Animal):
    def bark(self):
        return print("voof voof!")

pet1 = Dog()
pet1.bark()
pet1.eat()

pet2 = Horse()
pet2.neigh()
pet2.eat()
print(40*"=")

"""
LAB 3 - OOP

Create the following classes: 
Person
Staff
Busdriver
Person should have one method named walk( ) that should return "walking"
Staff should have one method called work( ) that should return "working"
Busdriver should have one method called driving ( ) that returns "diving the bus"
The Busdriver class should inherit from both Person and Staff 
"""

class Person:
    def walk(self):
        return print("Walking ...")
class Staff:
    def work(self):
        return print("Working ...")
class Busdriver(Staff, Person):
    def driving(self):
        return print("Driving the bus")

Hossein = Busdriver()
Hossein.walk()
Hossein.work()
Hossein.driving()
print(40*"=")


def avg(*num_lst):
    sum = 0
    for num in num_lst:
        sum += num
    n = len(num_lst)
    return print(sum/n)

avg(20, 40)