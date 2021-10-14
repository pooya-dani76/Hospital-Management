import sqlite3


def ConnectSqlite():
    conn = sqlite3.connect('Hospital.db')
    cur = conn.cursor()
    return cur, conn


def CreateTables():
    cur, conn = ConnectSqlite()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Doctors(
        id INTEGER PRIMARY KEY,
        NationalNumber TEXT,
        FirstName TEXT,
        LastName TEXT,
        Age INTEGER,
        Degree TEXT,
        UNIQUE (NationalNumber))''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Medicines(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Stock INTEGER,
        Description TEXT,
        UNIQUE (Name))''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Patients(
        id INTEGER PRIMARY KEY,
        NationalNumber TEXT,
        FirstName TEXT,
        LastName TEXT,
        Sickness TEXT, 
        Age INTEGER,
        VisitorDoctorNationalNumber TEXT,
        UNIQUE (NationalNumber))''')
    conn.commit()
    conn.close()


######################### Doctors Operators ###############################


def AllDoctors():
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Doctors''')
    Doctors = cur.fetchall()
    conn.close()
    return Doctors


def InsertDoctor(NationalNumber, FirstName, LastName, Age, Degree):
    cur, conn = ConnectSqlite()
    cur.execute('''
    INSERT INTO Doctors VALUES (NULL, ?, ?, ? ,? ,?)''', (NationalNumber, FirstName, LastName, Age, Degree))
    conn.commit()
    conn.close()


def UpdateDoctor(id, NationalNumber, FirstName, LastName, Age, Degree):
    cur, conn = ConnectSqlite()
    cur.execute('''
    UPDATE Doctors SET NationalNumber=?,FirstName=?,LastName=?,Age=?,Degree=? WHERE id = ?''',
                (NationalNumber, FirstName, LastName, Age, Degree, id))
    conn.commit()
    conn.close()


def DeleteDoctor(id):
    cur, conn = ConnectSqlite()
    cur.execute('''DELETE FROM Doctors WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def SearchDoctor(NationalNumber="", FirstName="", LastName="", Age="", Degree=""):
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Doctors WHERE NationalNumber=? OR FirstName=? OR LastName=? OR Age=? OR Degree=?''',
                (NationalNumber, FirstName, LastName, Age, Degree))
    Doctors = cur.fetchall()
    conn.close()
    return Doctors


######################### Medicines Operators ###############################


def AllMedicines():
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Medicines''')
    Medicines = cur.fetchall()
    conn.close()
    return Medicines


def InsertMedicine(Name, Stock, Description):
    cur, conn = ConnectSqlite()
    cur.execute('''
    INSERT INTO Medicines VALUES (NULL, ?, ?, ?)''', (Name, Stock, Description))
    conn.commit()
    conn.close()


def UpdateMedicine(id, Name, Stock, Description):
    cur, conn = ConnectSqlite()
    cur.execute('''
    UPDATE Medicines SET Name=?, Stock=?, Description=? WHERE id = ?''',
                (Name, Stock, Description, id))
    conn.commit()
    conn.close()


def DeleteMedicine(id):
    cur, conn = ConnectSqlite()
    cur.execute('''DELETE FROM Medicines WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def SearchMedicine(Name="", Stock="", Description=""):
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Medicines WHERE Name=? OR Stock=? OR Description=?''',
                (Name, Stock, Description))
    Medicines = cur.fetchall()
    conn.close()
    return Medicines


######################### Patients Operators ###############################


def AllPatients():
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Patients''')
    Patients = cur.fetchall()
    conn.close()
    return Patients


def InsertPatient(NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber):
    cur, conn = ConnectSqlite()
    cur.execute('''
    INSERT INTO Patients VALUES (NULL, ?, ?, ? ,?, ? ,?)
    ''', (NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber))
    conn.commit()
    conn.close()


def UpdatePatient(id, NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber):
    cur, conn = ConnectSqlite()
    cur.execute('''
    UPDATE Patients SET
    NationalNumber=?,
    FirstName=?,
    LastName=?,
    Sickness=?,
    Age=?,
    VisitorDoctorNationalNumber=?
    WHERE id = ?''',
                (NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber, id))
    conn.commit()
    conn.close()


def DeletePatient(id):
    cur, conn = ConnectSqlite()
    cur.execute('''DELETE FROM Patients WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def SearchPatient(FirstName="", LastName="", Age="", Sickness="", VisitorDoctorNationalNumber=""):
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Patients WHERE 
    FirstName=? OR 
    LastName=? OR 
    Sickness=? OR 
    Age=? OR 
    VisitorDoctorNationalNumber=?''',
                (FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber))
    Patients = cur.fetchall()
    conn.close()
    return Patients


CreateTables()
