from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run.")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Lion(Animal):
    def move(self):
        print("I can run and roar.")

r = Human()
r.move()
x = Snake()
x.move()
y = Lion()
y.move()
