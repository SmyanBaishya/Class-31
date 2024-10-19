from abc import ABC, abstractmethod

class BMW:
    
    def top_speed(self):
        print("250 km/h")
    
    def engine(self):
        print("6-cylinder engines")
    
    def brand_origin(self):
        print("German")

class Ferrari:
    
    def top_speed(self):
        print("350 km/h")
    
    def engine(self):
        print("V8 and V12 engines")
    
    def brand_origin(self):
        print("Italian")

a = BMW()
b = Ferrari()

for car in (a,b):
    car.top_speed()
    car.engine()
    car.brand_origin()