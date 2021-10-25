from SqliteFunctions import *
from Consts import *
import random


class Human:
    """Generate a Human Model
    """

    def __init__(self, FirstName: str, LastName: str, Age: int, NationalNumber: str):
        """Initialize a Human

        Args:
        FirstName (str): First Name of a Human 
        LastName (str): Last Name of a Human 
        Age (int): Age of a Human 
        NationalNumber (str): National Number of a Human 
        """
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.NationalNumber = NationalNumber


class Doctor(Human):
    """Generate A Doctor Model

    Args:
        Human (```Human```): Inherits From ```Human``` model
    """

    def __init__(self, id: int, NationalNumber: str, FirstName: str, LastName: str, Age: int, Type: str):
        """Initialize a Doctor

        Args:
            id (int): id of Doctor in ```Doctors``` Table
            NationalNumber (str): National Number of a Doctor
            FirstName (str): First Name of a Doctor 
            LastName (str): Last Name of a Human 
            Age (int): Age of a Doctor 
            Type (str): Doctor Type
        """
        super().__init__(FirstName, LastName, Age, NationalNumber)
        self.id = id
        self.Type = Type

    def __str__(self) -> str:
        """Convert Doctor Class to Printable Object

        Returns:
            str: Doctor's Info
        """
        return f'{self.NationalNumber} , Dr.{self.FirstName} {self.LastName} , {self.Type}'

    def __repr__(self) -> str:
        """Representation of Doctor Class in Objects

        Returns:
            str: Doctor's Name & Type
        """
        return f'Dr.{self.FirstName} {self.LastName}({self.Type})'

    @property
    def Delete(self) -> None:
        """Delete This Doctor From ```Doctors``` Table When Deleting its Class
        """
        DeleteDoctor(self.id)
        Doctors = list(filter(lambda x: x[5] == self.Type, AllDoctors()))
        if len(Doctors) > 0:
            for DoctorPatient in list(filter(lambda x: x[6] == self.NationalNumber, AllPatients())):
                print('Hi2')
                PatientTemp = Patient(id=DoctorPatient[0], NationalNumber=DoctorPatient[1], FirstName=DoctorPatient[2],
                                      LastName=DoctorPatient[3], Sickness=DoctorPatient[4],
                                      Age=DoctorPatient[5], VisitorDoctorNationalNumber=DoctorPatient[6])
                DoctorTemp = random.choice(Doctors)
                PatientTemp.Update(NationalNumber=DoctorPatient[1], FirstName=DoctorPatient[2],
                                   LastName=DoctorPatient[3], Sickness=DoctorPatient[4],
                                   Age=DoctorPatient[5], VisitorDoctorNationalNumber=DoctorTemp[1])

        else:
            for DoctorPatient in list(filter(lambda x: x[6] == self.NationalNumber, AllPatients())):
                PatientTemp = Patient(id=DoctorPatient[0], NationalNumber=DoctorPatient[1], FirstName=DoctorPatient[2],
                                      LastName=DoctorPatient[3], Sickness=DoctorPatient[4],
                                      Age=DoctorPatient[5], VisitorDoctorNationalNumber=DoctorPatient[6])
                PatientTemp.Delete
                del PatientTemp

    def Update(self, NationalNumber: str, FirstName: str, LastName: str, Age: int, Type: str):
        """Update This Doctor Info With Given Info

        Args:
            NationalNumber (str): National Number of a Doctor
            FirstName (str): First Name of a Doctor 
            LastName (str): Last Name of a Human 
            Age (int): Age of a Doctor 
            Type (str): Doctor Type

        Returns:
            bool: if Data Correctly Added to Sqlite Table
            tuple(str, bool): if Updating Data Encountered an Error(Error Message, False) 
        """
        # try:
        # CheckHumanInput(NationalNumber, FirstName, LastName, Age)
        # CheckDoctorInput(Type)
        PreviousNationalNumber = self.NationalNumber
        self.NationalNumber = NationalNumber
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Type = Type
        UpdateDoctor(self.id, NationalNumber,
                     FirstName, LastName, Age, Type)
        # print('Success!')
        # print(self.NationalNumber)
        # print(list(filter(lambda x: x[6] == self.NationalNumber, AllPatients())))
        if self.NationalNumber != PreviousNationalNumber:
            for DoctorPatient in list(filter(lambda x: x[6] == PreviousNationalNumber, AllPatients())):
                Temp = Patient(id=DoctorPatient[0], NationalNumber=DoctorPatient[1], FirstName=DoctorPatient[2],
                               LastName=DoctorPatient[3], Sickness=DoctorPatient[4],
                               Age=DoctorPatient[5], VisitorDoctorNationalNumber=DoctorPatient[6])
                Temp.Update(NationalNumber=DoctorPatient[1], FirstName=DoctorPatient[2],
                            LastName=DoctorPatient[3], Sickness=DoctorPatient[4],
                            Age=DoctorPatient[5], VisitorDoctorNationalNumber=self.NationalNumber)
        #     return True
        # except Exception as ErrorMessage:
        #     return ErrorMessage, False

    @property
    def ToMap(self) -> dict:
        """Return This Doctor Info as Dictionary

        Returns:
            dict: {'PropertyName': Property}
        """
        return {'id': self.id, 'NationalNumber': self.NationalNumber, 'FirstName': self.FirstName,
                'LastName': self.LastName, 'Age': self.Age, 'Type': self.Type}


class Patient(Human):
    """Generate A Patient Model

    Args:
        Human (```Human```): Inherits From ```Human``` model
    """

    def __init__(self, id: int, NationalNumber: str, FirstName: str, LastName: str, Sickness: str,
                 Age: int, VisitorDoctorNationalNumber: str):
        """Initialize a Patient

        Args:
            id (int): id of Patient in ```Patients``` Table
            NationalNumber (str): National Number of a Patient
            FirstName (str): First Name of a Patient 
            LastName (str): Last Name of a Human 
            Sickness (str): Problem of Patient Cause Him Sick
            Age (int): Age of Patient
            VisitorDoctorNationalNumber (str): Visitor Doctor's National Number
        """
        super().__init__(FirstName, LastName, Age, NationalNumber)
        self.id = id
        self.Sickness = Sickness
        self.VisitorDoctorNationalNumber = VisitorDoctorNationalNumber

    def __str__(self) -> str:
        """Convert Patient Class to Printable Object

        Returns:
            str: Patient's Info
        """
        return f'{self.NationalNumber} , {self.FirstName} {self.LastName}'

    def __repr__(self) -> str:
        """Representation of Patient Class in Objects

        Returns:
            str: Patient's Name & Type
        """
        return f'{self.FirstName} {self.LastName}({self.NationalNumber})'

    @property
    def Delete(self) -> None:
        """Delete This Patient From ```Patients``` Table When Deleting its Class
        """
        DeletePatient(self.NationalNumber)

    @property
    def ToMap(self) -> dict:
        """Return This Patient Info as Dictionary

        Returns:
            dict: {'PropertyName': Property}
        """
        return {'id': self.id, 'NationalNumber': self.NationalNumber, 'FirstName': self.FirstName,
                'LastName': self.LastName, 'Age': self.Age, 'Sickness': self.Sickness,
                'VisitorDoctorNationalNumber': self.VisitorDoctorNationalNumber}

    def Update(self, NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber):
        """Update This Patient Info With Given Info

        Args:
            NationalNumber (str): National Number of a Patient
            FirstName (str): First Name of a Patient 
            LastName (str): Last Name of a Human 
            Sickness (str): Problem of Patient Cause Him Sick
            Age (int): Age of Patient
            VisitorDoctorNationalNumber (str): Visitor Doctor's National Number

        Returns:
            bool: if Data Correctly Added to Sqlite Table
            tuple(str, bool): if Updating Data Encountered an Error(Error Message, False) 
        """
        # try:
        # CheckHumanInput(NationalNumber, FirstName, LastName, Age)
        # CheckPatientInput(NationalNumber, VisitorDoctorNationalNumber, Sickness)
        self.NationalNumber = NationalNumber
        self.FirstName = FirstName
        self.LastName = LastName
        self.Sickness = Sickness
        self.Age = Age
        self.Type = VisitorDoctorNationalNumber
        UpdatePatient(self.id, NationalNumber, FirstName,
                      LastName, Sickness, Age, VisitorDoctorNationalNumber)
        #     return True
        # except Exception as ErrorMessage:
        #     return ErrorMessage, False


class Medicine:
    """Generate a Medicine Model
    """

    def __init__(self, id: int, Name: str, Stock: int, Description: str):
        """Initialize a Medicine

        Args:
            id (int): id of Medicine in ```Medicines``` Table
            Name (str): Name of Medicine
            Stock (int): Number of Medicine There is in Hospital's Drug Store 
            Description (str): Description about What Medicine does
        """
        self.id = id
        self.Name = Name
        self.Stock = Stock
        self.Description = Description

    def Sell(self, NumberOfSold):
        """Sell ```NumberOfSold``` of This Medicine

        Args:
            NumberOfSold (int): Number of This Medicines Sold

        Returns:
            bool: if Data Correctly Added to Sqlite Table
            tuple(str, bool): if Updating Data Encountered an Error(Error Message, False) 
        """
        try:
            CheckMedicineInput(NumberOfSold)
            self.Stock -= NumberOfSold
            CheckMedicineInput(self.Stock)
            UpdateMedicine(self.id, self.Name, self.Stock, self.Description)
        except Exception as ErrorMessage:
            return ErrorMessage, False

    def Buy(self, NumberOfBought):
        """Sell ```NumberOfBought``` of This Medicine

        Args:
            NumberOfBought (int): Number of This Medicines Bought

        Returns:
            bool: if Data Correctly Added to Sqlite Table
            tuple(str, bool): if Updating Data Encountered an Error(Error Message, False) 
        """
        try:
            CheckMedicineInput(NumberOfBought)
            self.Stock += NumberOfBought
            UpdateMedicine(self.id, self.Name, self.Stock, self.Description)
        except Exception as ErrorMessage:
            return ErrorMessage, False

    def Update(self, Name, Stock, Description):
        """Update This Medicine Info With Given Info

        Args:
            Name (str): Name of Medicine
            Stock (int): Number of Medicine There is in Hospital's Drug Store 
            Description (str): Description about What Medicine does

        Returns:
            bool: if Data Correctly Added to Sqlite Table
            tuple(str, bool): if Updating Data Encountered an Error(Error Message, False) 
        """
        try:
            CheckMedicineInput(Stock)
            self.Name = Name
            self.Stock = Stock
            self.Description = Description
            UpdateMedicine(self.id, Name, Stock, Description)
        except Exception as ErrorMessage:
            return ErrorMessage, False

    def __str__(self) -> str:
        """Convert Medicine Class to Printable Object

        Returns:
            str: Medicine's Info
        """
        return f'{self.Name} , {self.Stock} , {self.Description}'

    def __repr__(self) -> str:
        """Representation of Medicine Class in Objects

        Returns:
            str: Medicine's Name & Type
        """
        return f'{self.Name} -> ({self.Stock})'

    @property
    def ToMap(self) -> dict:
        """Return This Medicine Info as Dictionary

        Returns:
            dict: {'PropertyName': Property}
        """
        return {'id': self.id, 'Name': self.Name, 'Stock': self.Stock, 'Description': self.Description}

    @property
    def Delete(self) -> None:
        """Delete This Medicine From ```Medicines``` Table When Deleting its Class
        """
        DeleteMedicine(self.id)

print(ord(' '))