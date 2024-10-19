from abc import ABC, abstractmethod

class ABCclass():
    def print(self,x):
        print("Passed value: ",x)

    @abstractmethod
    def task(self):
        print("I am inside ABC class")

class test_Class(ABCclass):
    def task(self):
        print("I am inside test_class, function task")

test_obj = test_Class()
test_obj.task()
test_obj.print(62)
