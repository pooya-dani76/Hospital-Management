import sqlite3


def ConnectSqlite() -> tuple:
    """Create & Connects To Hospital.db File 

    Returns:
        Tuple: Sqlite File Cursor, Sqlite Connection
    """
    Conn = sqlite3.connect('Hospital.db')
    Cur = Conn.cursor()
    return Cur, Conn


def CreateTables() -> None:
    """Creates Tables Doctors, Medicines, Patients in Hospital.db File
    """
    cur, conn = ConnectSqlite()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Doctors(
        id INTEGER PRIMARY KEY,
        NationalNumber TEXT,
        FirstName TEXT,
        LastName TEXT,
        Age INTEGER,
        Type TEXT,
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


def AllDoctors() -> list:
    """All Doctors Info There is in ```Doctors``` Table

    Returns:
        list: A List of Doctors Recorded in Doctors Table
    """
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Doctors''')
    Doctors = cur.fetchall()
    conn.close()
    return Doctors


def InsertDoctor(NationalNumber: str, FirstName: str, LastName: str, Age: int, Type: str) -> None:
    """Add a New Doctor to ```Doctors``` Table

    Args:
        NationalNumber (str): National Number of Doctor
        FirstName (str): First Name of Doctor 
        LastName (str): Last Name of Doctor
        Age (int): Age of Doctor
        Type (str): Doctor Type
    """
    cur, conn = ConnectSqlite()
    cur.execute('''
    INSERT INTO Doctors VALUES (NULL, ?, ?, ? ,? ,?)''', (NationalNumber, FirstName, LastName, Age, Type))
    conn.commit()
    conn.close()


def UpdateDoctor(id: int, NationalNumber: str, FirstName: str, LastName: str, Age: int, Type: str) -> None:
    """Update a Doctor Info From ```Doctors``` Table

    Args:
        id (int): id of Doctor in ```Doctors``` Table
        NationalNumber (str): National Number of Doctor
        FirstName (str): First Name of Doctor 
        LastName (str): Last Name of Doctor
        Age (int): Age of Doctor
        Type (str): Doctor Type
    """
    cur, conn = ConnectSqlite()
    cur.execute('''
    UPDATE Doctors SET NationalNumber=?,FirstName=?,LastName=?,Age=?,Type=? WHERE id = ?''',
                (NationalNumber, FirstName, LastName, Age, Type, id))
    conn.commit()
    conn.close()


def DeleteDoctor(id: int) -> None:
    """Delete a Doctor From ```Doctors``` Table

    Args:
        id (int): id of Doctor in ```Doctors``` Table
    """
    cur, conn = ConnectSqlite()
    cur.execute('''DELETE FROM Doctors WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def SearchDoctor(NationalNumber="", FirstName="", LastName="", Age="", Type="") -> list:
    """Search a Doctor in ```Doctors``` Table

    Args:
        NationalNumber (str, optional): National Number of Doctor. Defaults to "".
        FirstName (str, optional): First Name of Doctor. Defaults to "".
        LastName (str, optional): Last Name of Doctor. Defaults to "".
        Age (str, optional): Age of Doctor. Defaults to "".
        Type (str, optional): Doctor Type. Defaults to "".

    Returns:
        list: A List of Doctors
    """
    cur, conn = ConnectSqlite()
    cur.execute("""SELECT * FROM Doctors
                WHERE NationalNumber LIKE ? AND
                FirstName LIKE ? AND
                LastName LIKE ? AND
                Age LIKE ? AND 
                Type LIKE ? """,
                ('%'+NationalNumber+'%', '%'+FirstName+'%', '%'+LastName+'%', '%'+Age+'%', '%'+Type+'%'))
    Doctors = cur.fetchall()
    conn.close()
    return Doctors


######################### Medicines Operators ###############################


def AllMedicines() -> list:
    """All Medicines Info There is in ```Medicines``` Table

    Returns:
        list: A List of Medicines Recorded in Medicines Table
    """
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Medicines''')
    Medicines = cur.fetchall()
    conn.close()
    return Medicines


def InsertMedicine(Name: str, Stock: int, Description: str) -> None:
    """Add a Medicine Info to ```Medicines``` Table

    Args:
        Name (str): Name of Medicine
        Stock (int): Number of Medicine There is in Hospital's Drug Store 
        Description (str): Description about What Medicine does
    """
    cur, conn = ConnectSqlite()
    cur.execute('''
    INSERT INTO Medicines VALUES (NULL, ?, ?, ?)''', (Name, Stock, Description))
    conn.commit()
    conn.close()


def UpdateMedicine(id: int, Name: str, Stock: int, Description: str) -> None:
    """Add a Medicine Info to ```Medicines``` Table

    Args:
        id (int): id of Medicine in ```Medicines``` Table
        Name (str): Name of Medicine
        Stock (int): Number of Medicine There is in Hospital's Drug Store 
        Description (str): Description about What Medicine does
    """
    cur, conn = ConnectSqlite()
    cur.execute('''
    UPDATE Medicines SET Name=?, Stock=?, Description=? WHERE id = ?''',
                (Name, Stock, Description, id))
    conn.commit()
    conn.close()


def DeleteMedicine(id: int) -> None:
    """Delete a Medicine From ```Medicines``` Table

    Args:
        id (int): id of Medicine in ```Medicines``` Table
    """
    cur, conn = ConnectSqlite()
    cur.execute('''DELETE FROM Medicines WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def SearchMedicine(Name="", Stock="", Description="") -> list:
    """Search a Medicine in ```Medicines``` Table

    Args:
        Name (str, optional): Name of Medicine. Defaults to "".
        Stock (str, optional): Number of Medicine There is in Hospital's Drug Store . Defaults to "".
        Description (str, optional): Description about What Medicine does. Defaults to "".

    Returns:
        list: A List of Doctors
    """
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Medicines WHERE Name LIKE ? AND Stock LIKE ? AND Description LIKE ?''',
                ('%' + Name + '%', '%' + Stock + '%', '%' + Description + '%'))
    Medicines = cur.fetchall()
    conn.close()
    return Medicines


######################### Patients Operators ###############################


def AllPatients() -> list:
    """All Patients Info There is in ```Patients``` Table

    Returns:
        list: A List of Patients Recorded in Patients Table
    """
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Patients''')
    Patients = cur.fetchall()
    conn.close()
    return Patients


def InsertPatient(NationalNumber: str, FirstName: str, LastName: str, Sickness: str, Age: int,\
     VisitorDoctorNationalNumber: str) -> None:
    """Add a New Patient to ```Patients``` Table

    Args:
        NationalNumber (str): National Number of Patient
        FirstName (str): First Name of Patient 
        LastName (str): Last Name of Patient
        Sickness (str): Problem of Patient Cause Him Sick
        Age (int): Age of Patient
        VisitorDoctorNationalNumber (str): Visitor Doctor's National Number
    """
    cur, conn = ConnectSqlite()
    cur.execute('''
    INSERT INTO Patients VALUES (NULL, ?, ?, ? ,?, ? ,?)
    ''', (NationalNumber, FirstName, LastName, Sickness, Age, VisitorDoctorNationalNumber))
    conn.commit()
    conn.close()


def UpdatePatient(id: int,NationalNumber: str, FirstName: str, LastName: str, Sickness: str, Age: int,\
     VisitorDoctorNationalNumber: str) -> None:
    """Update a Patient Info From ```Patients``` Table

    Args:
        id (int): id of Patient in ```Patients``` Table 
        NationalNumber (str): National Number of Doctor
        FirstName (str): First Name of Patient 
        LastName (str): Last Name of Patient
        Sickness (str): Problem of Patient Cause Him Sick
        Age (int): Age of Patient
        VisitorDoctorNationalNumber (str): Visitor Doctor's National Number
    """
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


def DeletePatient(id: int) -> None:
    """Delete a Patient From ```Patients``` Table

    Args:
        id (int): id of Patient in ```Patients``` Table
    """
    cur, conn = ConnectSqlite()
    cur.execute('''DELETE FROM Patients WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def SearchPatient(NationalNumber="", FirstName="", LastName="", \
    Sickness="", Age="", VisitorDoctorNationalNumber="") -> list:
    """Search a Patient Info In ```Patients``` Table

    Args:
        NationalNumber (str): National Number of Doctor
        FirstName (str): First Name of Patient 
        LastName (str): Last Name of Patient
        Sickness (str): Problem of Patient Cause Him Sick
        Age (int): Age of Patient
        VisitorDoctorNationalNumber (str): Visitor Doctor's National Number
    """
    cur, conn = ConnectSqlite()
    cur.execute('''SELECT * FROM Patients WHERE
    NationalNumber LIKE ? AND
    FirstName LIKE ? AND 
    LastName LIKE ? AND 
    Sickness LIKE ? AND 
    Age LIKE ? AND 
    VisitorDoctorNationalNumber LIKE ?''',
                ('%' + NationalNumber + '%', '%' + FirstName + '%', '%' + LastName + '%', '%' + Sickness + '%',\
                     '%' + Age + '%', '%' + VisitorDoctorNationalNumber + '%'))
    Patients = cur.fetchall()
    conn.close()
    return Patients


CreateTables()
