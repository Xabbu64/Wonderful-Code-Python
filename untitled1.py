# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:51:31 2022

@author: mmoec
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name} is now sitting")