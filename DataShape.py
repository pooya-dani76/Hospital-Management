from SqliteFunctions import UpdateMedicine


class Human:
    def __init__(self, FirstName, LastName, Age, NationalNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.NationalNumber = NationalNumber


class Doctor(Human):
    def __init__(self, id, FirstName, LastName, Age, Degree, NationalNumber):
        super().__init__(FirstName, LastName, Age, NationalNumber)
        self.id = id
        self.Degree = Degree

    def __str__(self):
        return f'Dr.{self.FirstName} {self.LastName} , {self.Degree}'


class Patient(Human):
    def __init__(self, id, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber, NationalNumber):
        super().__init__(FirstName, LastName, Age, NationalNumber)
        self.id = id
        self.Sickness = Sickness
        self.VisitorDoctorNationalNumber = VisitorDoctorNationalNumber

    def __str__(self):
        return f'{self.FirstName} {self.LastName}   NationalNumber: {self.NationalNumber}  Sickness: {self.Sickness}'


class Medicine:
    def __init__(self, id, Name, Stock, Description):
        self.id = id
        self.Name = Name
        self.Stock = Stock
        self.Description = Description

    def Sell(self, NumberOfSold):
        self.Stock -= NumberOfSold
        UpdateMedicine(self.id, self.Name, self.Stock, self.Description)

    def __str__(self):
        return f'{self.Name}  Stock: {self.Stock}'
