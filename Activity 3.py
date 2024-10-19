from abc import ABC, abstractmethod

class India:
    def capital(self):
        print("New Delhi")
    
    def language(self):
        print("Hindi,Sanskrit")
    
    def culture(self):
        print("Rich in traditions,many festivals")

class Japan():

    def capital(self):
        print("Tokyo")

    def language(self):
        print("Japanese")
 
    def culture(self):
        print("Known for technology and ancient customs")

a = India()
b = Japan()

for country in  (a,b):
     country.capital()
     country.language()
     country.culture()