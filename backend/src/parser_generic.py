import abc
from abc import ABC, abstractmethod

class MedicalDocParser(metaclass=abc.ABCMeta):    #this class is being used as an abstract class
    def __init__(self,text):
        self.text = text

    @abc.abstractmethod
    def parse(self):
        pass

