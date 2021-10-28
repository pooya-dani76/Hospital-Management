from SqliteFunctions import *
from Consts import *
import DataShape as cls


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
    # try:
    # CheckHumanInput(NationalNumber, FirstName, LastName, Age)
    # CheckDoctorInput(NationalNumber, Type)
    # InsertDoctor(NationalNumber, FirstName, LastName, Age, Type)
    # return True
    # except Exception as ErrorMessage:
    #     return ErrorMessage, False


def FindDoctor(NationalNumber="", FirstName="", LastName="", Age="", Type="") -> list:
    """Find Doctors With Given Info 

    Args:
        NationalNumber (str, optional): National Number of Doctor. Defaults to "".
        FirstName (str, optional): First Name of Doctor. Defaults to "".
        LastName (str, optional): last Name of Doctor. Defaults to "".
        Age (str, optional): Age of Doctor. Defaults to "".
        Type (str, optional): Type of Doctor. Defaults to "".

    Returns:
        list: A List of Class ```Doctor```
    """
    ClassDoctorsList = []
    Doctors = SearchDoctor(NationalNumber=NationalNumber, FirstName=FirstName, LastName=LastName,
                           Age=Age, Type=Type)
    for Doctor in Doctors:
        ClassDoctorsList.append(cls.Doctor(id=Doctor[0], NationalNumber=Doctor[1],
                                           FirstName=Doctor[2], LastName=Doctor[3], Age=Doctor[4], Type=Doctor[5]))
    return ClassDoctorsList


def LoadDoctors() -> list:
    """Loads All Doctors into ```Doctor``` Classes

    Returns:
        list: a List of ```Doctor``` Class
    """
    ClassDoctorsList = []
    Doctors = AllDoctors()
    for Doctor in Doctors:
        ClassDoctorsList.append(cls.Doctor(id=Doctor[0], NationalNumber=Doctor[1],
                                           FirstName=Doctor[2], LastName=Doctor[3], Age=Doctor[4], Type=Doctor[5]))
    return ClassDoctorsList

######################### Patient Operators ###############################


# def ReceptionPatient(NationalNumber: str, FirstName: str, LastName: str, Sickness: str, Age: str,
#                      VisitorDoctorNationalNumber: str):
#     """Add Patient to Table ```Patients``` if Data be Right Shape

#     Args:
#         NationalNumber (str): National Number of Patient
#         FirstName (str): First Name of Patient 
#         LastName (str): Last Name of Patient
#         Sickness (str): Problem of Patient Cause Him Sick
#         Age (int): Age of Patient
#         VisitorDoctorNationalNumber (str): Visitor Doctor's National Number

#     Returns:
#         True: if Data Correctly Added to Sqlite Table
#         tuple(str, False): if Updating Data Encountered an Error(Error Message, False) 
#     """
#     try:
#         CheckHumanInput(NationalNumber, FirstName, LastName, Age)
#         CheckPatientInput(
#             NationalNumber, VisitorDoctorNationalNumber, Sickness)
#         InsertPatient(NationalNumber, FirstName, LastName,
#                       Sickness, Age, VisitorDoctorNationalNumber)
#         return True
#     except Exception as ErrorMessage:
#         return ErrorMessage


def LoadPatients() -> list:
    """Loads All Patients into ```Patient``` Classes

    Returns:
        list: a List of ```Patient``` Class
    """
    ClassPatientsList = []
    Patients = AllPatients()
    for Patient in Patients:
        ClassPatientsList.append(cls.Patient(id=Patient[0], NationalNumber=Patient[1],
                                             FirstName=Patient[2], LastName=Patient[3],
                                             Sickness=Patient[4], Age=Patient[5],
                                             VisitorDoctorNationalNumber=Patient[6]))
    return ClassPatientsList


def FindPatient(NationalNumber="", FirstName="", LastName="",
                Sickness="", Age="", VisitorDoctorNationalNumber="") -> list:
    """Find Patients With Given Info 

    Args:
        NationalNumber (str, optional): National Number of Patient. Defaults to "".
        FirstName (str, optional): First Name of Patient. Defaults to "".
        LastName (str, optional): last Name of Patient. Defaults to "".
        Sickness (str, optional): Description about Problem of Patient. Defaults to "".
        Age (str, optional): Age of Patient. Defaults to "".
        VisitorDoctorNationalNumber (str, optional): Visitor of Patient. Defaults to "".

    Returns:
        list: A List of Class ```Patient```
    """
    ClassPatientsList = []
    Patients = SearchPatient(NationalNumber=NationalNumber, FirstName=FirstName, LastName=LastName,
                             Sickness=Sickness, Age=Age, VisitorDoctorNationalNumber=VisitorDoctorNationalNumber)
    for Patient in Patients:
        ClassPatientsList.append(cls.Patient(id=Patient[0], NationalNumber=Patient[1], FirstName=Patient[2],
                                             LastName=Patient[3], Sickness=Patient[4], Age=Patient[5], VisitorDoctorNationalNumber=Patient[6]))
    return ClassPatientsList

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
        CheckMedicineInput(Name, Stock, Description)
        InsertMedicine(Name, Stock, Description)
        return True
    except Exception as ErrorMessage:
        return ErrorMessage, False


def LoadMedicines() -> list:
    """Loads All Medicines into ```Medicine``` Classes

    Returns:
        list: a List of ```Medicine``` Class
    """
    ClassMedicinesList = []
    Medicines = AllMedicines()
    for Medicine in Medicines:
        ClassMedicinesList.append(cls.Medicine(id=Medicine[0], Name=Medicine[1], Stock=Medicine[2],
                                               Description=Medicine[3]))
    return ClassMedicinesList


def FindMedicine(Name="", Stock="", Description="") -> list:
    """Find Medicines With Given Info 

    Args:
        NationalNumber (str, optional): National Number of Medicine. Defaults to "".
        FirstName (str, optional): First Name of Medicine. Defaults to "".
        LastName (str, optional): last Name of Medicine. Defaults to "".
        Sickness (str, optional): Description about Problem of Medicine. Defaults to "".
        Age (str, optional): Age of Medicine. Defaults to "".
        VisitorDoctorNationalNumber (str, optional): Visitor of Medicine. Defaults to "".

    Returns:
        list: A List of Class ```Medicine```
    """
    ClassMedicinesList = []
    Medicines = SearchMedicine(Name=Name, Stock=Stock, Description=Description)
    for Medicine in Medicines:
        ClassMedicinesList.append(cls.Medicine(id=Medicine[0], Name=Medicine[1],
                                               Stock=Medicine[2], Description=Medicine[3]))
    return ClassMedicinesList

######################### General Operators ##############################


def LoadAllData():
    """Loads All Data in Sqlite

    Returns:
        tuple[list, list, list]: [Doctors List, Medicines List, Medicines List]
    """
    Doctors = LoadDoctors()
    Patients = LoadPatients()
    Medicines = LoadMedicines()
    return Doctors, Patients, Medicines


def AddNewDoctorType(DoctorType: str) -> None:
    """Add New Type of Doctor to Hospital

    Args:
        DoctorType (str): Doctor Type
    """
    TypeList.append(DoctorType)
