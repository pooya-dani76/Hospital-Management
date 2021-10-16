from SqliteFunctions import *
from Consts import *


######################### Doctors Operators ##############################
def EmployDoctor(NationalNumber: str, FirstName: str, LastName: str, Age: str, Type: str):
    """Add Doctor to Table ```Doctors``` if Data be Right Shape

    Args:
        NationalNumber (str): National Number of Doctor
        FirstName (str): First Name of Doctor 
        LastName (str): Last Name of Doctor
        Age (int): Age of Doctor
        Type (str): Doctor Type

    Returns:
        True: if Data Correctly Added to Sqlite Table
        tuple(str, False): if Updating Data Encountered an Error(Error Message, False)  
    """
    try:
        CheckHumanInput(NationalNumber, FirstName, LastName, Age)
        CheckDoctorInput(Type)
        InsertDoctor(NationalNumber, FirstName, LastName, Age, Type)
        return True
    except Exception as ErrorMessage:
        return ErrorMessage, False        

######################### Patient Operators ###############################

def ReceptionPatient(NationalNumber: str, FirstName: str, LastName: str, Sickness: str, Age: str,\
     VisitorDoctorNationalNumber: str):
    """Add Patient to Table ```Patients``` if Data be Right Shape

    Args:
        NationalNumber (str): National Number of Patient
        FirstName (str): First Name of Patient 
        LastName (str): Last Name of Patient
        Sickness (str): Problem of Patient Cause Him Sick
        Age (int): Age of Patient
        VisitorDoctorNationalNumber (str): Visitor Doctor's National Number

    Returns:
        True: if Data Correctly Added to Sqlite Table
        tuple(str, False): if Updating Data Encountered an Error(Error Message, False) 
    """
    try:
        CheckHumanInput(NationalNumber, FirstName, LastName, Age)
        CheckPatientInput(NationalNumber, VisitorDoctorNationalNumber)
        InsertPatient(NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber)
        return True
    except Exception as ErrorMessage:
        return ErrorMessage    

######################### Medicine Operators ##############################

def AddNewMedicine(Name: str, Stock: int, Description: str):
    """Add Medicine to Table ```Medicines``` if Data be Right Shape

    Args:
        Name (str): Name of Medicine
        Stock (int): Number of Medicine There is in Hospital's Drug Store 
        Description (str): Description about What Medicine does

    Returns:
        True: if Data Correctly Added to Sqlite Table
        tuple(str, False): if Updating Data Encountered an Error(Error Message, False)
    """
    try:
      CheckMedicineInput(Stock)
      InsertMedicine(Name, Stock, Description)
      return True
    except Exception as ErrorMessage:
      return ErrorMessage, False


