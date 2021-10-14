from DataShape import *
from SqliteFunctions import *


def WithoutDigit(text):
    return not any(map(str.isdigit, text))

def EmployDoctor(NationalNumber, FirstName, LastName, Age, Degree):
    if WithoutDigit(FirstName) and WithoutDigit(LastName) and WithoutDigit(LastName):
        try:
            InsertDoctor(NationalNumber, FirstName, LastName, Age, Degree)
            return True
        except Exception as ErrorMessage:
            return ErrorMessage