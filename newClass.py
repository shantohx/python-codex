#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myName(self):
        print("My name is " + self.name)
p1 = Person("Nilm", 10)
p1.myName()
