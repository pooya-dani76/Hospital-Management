from SqliteFunctions import *

TypeList = ['General Practitioner',
              'Eye Doctor', 'Lung doctor', 'Kidney doctor']


def WithoutDigit(text: str) -> bool:
    """Detect Given String Contains Digits or not

    Args:
        text (str): String to be Controll

    Returns:
        bool: Returns ```True``` if ```text``` Without Digits Otherwise Returns ```False```  
    """
    return not any(map(str.isdigit, text))


def WithoutChar(text: str) -> bool:
    """Detect Given Number String Contains Characters or not

    Args:
        text (str): a Number as String

    Returns:
        bool: Returns ```True``` if ```text``` Without Characters Otherwise Returns ```False```
    """
    return all(map(str.isdigit, text))


def CheckHumanInput(NationalNumber: str, FirstName: str, LastName: str, Age: str) -> None:
    """Check Class ```Human``` Args to be Right Shape

    Args:
        NationalNumber (str): National Number of Human
        FirstName (str): First Name of Human 
        LastName (str): Last Name of Human
        Age (int): Age of Human

    Raises:
        TypeError: When ```NationalNumber``` Contains Characters
        TypeError: When ```NationalNumber``` not 10 Digits
        TypeError: When ```FirstName``` Contains Digits
        TypeError: When ```LastName``` Contains Digits
        TypeError: When ```Age``` Contains Characters
    """
    if NationalNumber == "":
        raise TypeError("National Number Cannot Be Empty!")  

    if not WithoutChar(NationalNumber):
        raise TypeError(
            "National Number doesn't Should Be Contains Characters!")

    if len(NationalNumber) != 10:
        raise TypeError("National Number Should Be 10 Digits!") 

    if FirstName == "":
        raise TypeError("First Name Cannot Be Empty!")           

    if not WithoutDigit(FirstName):
        raise TypeError("First Name doesn't Should Be Contains Digits!")

    if len(FirstName) > 20:
        raise TypeError('First Name is too Long!')    

    if LastName == "":
        raise TypeError("Last Name Cannot Be Empty!")     

    if not WithoutDigit(LastName):
        raise TypeError("Last Name doesn't Should Be Contains Digits!")

    if len(LastName) > 20:
        raise TypeError('First Name is too Long!')     

    if Age == "":
        raise TypeError('Age Cannot be Empty!')    

    try:
        int(Age)
    except:
        raise TypeError("Age doesn't Should Be Contains Characters!")

    if int(Age) > 130:
        raise TypeError('Maximum Age is 130!') 
        
    if int(Age) < 1 :
        raise TypeError('Minimum Age is 1!')        


def CheckDoctorInput(NationalNumber: str, Type: str) -> None:
    """Check Class ```Doctor``` Arg(s) to be Right Shape

    Args:
        Type (str): Doctor Type

    Raises:
        TypeError: When ```Type``` isn't in Types There is in Hospital
    """
    if NationalNumber in list(map(lambda x: x[1], AllDoctors())):
        raise TypeError('This Doctor Has Already Exist in This Hospital!')

    if Type == "":
        raise TypeError('Doctor Type Cannot be Empty!')

    if Type not in TypeList:
        raise TypeError("Type is Invalid!")


def CheckPatientInput(NationalNumber: str, VisitorDoctorNationalNumber: str, Sickness: str)-> None:
    """Check Class ```Patient``` Arg(s) to be Right Shape

    Args:
        NationalNumber (str): National Number of Patient
        VisitorDoctorNationalNumber (str): Visitor Doctor's National Number

    Raises:
        TypeError: When ```VisitorDoctorNationalNumber``` is not in Hospital's Doctors
        PermissionError: When A Doctor Cannot be Own Doctor(```NationalNumber``` = ```VisitorDoctorNationalNumber```)
    """
    # if NationalNumber in list(map(lambda x: x[1], AllPatients())):
    #     raise TypeError('This Patient Has Already Exist in This Hospital!')

    if  len(Sickness) == 1 :
        raise TypeError('Sickness Cannot be Empty!')

    Doctors = list(map(lambda x: x[1] , AllDoctors()))
    if VisitorDoctorNationalNumber not in Doctors:
        raise TypeError("Doctor is not in This Hospital!")

    if NationalNumber == VisitorDoctorNationalNumber:
        raise PermissionError('A Doctor Cannot be Own Doctor!')


def CheckMedicineInput(Name: str, Stock: str, Description: str) -> None:
    """Check Class ```Medicine``` Arg(s) to be Right Shape

    Args:
        Name (str): Name of Medicine There is in Hospital's Drug Store 
        Stock (str): Number of Medicine There is in Hospital's Drug Store
        Stock (str): Description about Medicine There is in Hospital's Drug Store

    Raises:
        TypeError: When ```Stock``` Contains Characters
    """
    if Name == "":
        raise TypeError("Drug Name Cannot Be Empty!")

    if Name in list(map(lambda x: x[1], AllMedicines())):
        raise TypeError('This Medicine Has Already Exist in This Hospital!')    

    if Description == "":
        raise TypeError("Drug Name Cannot Be Empty!")    

    try:
      int(Stock)
    except:
      raise TypeError("Stock doesn't Should Be Contains Characters!")        
