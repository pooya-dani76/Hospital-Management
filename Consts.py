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


def CheckPatientNationalNumberIsExists(NationalNumber: str):
    """Check Given National Number is Exists in DataBase or not

    Args:
        NationalNumber (str): The National Number

    Raises:
        KeyError: when Given National Number Exists in DataBase
    """
    if len(list(filter(lambda x: x[1] == NationalNumber, AllPatients()))) > 0:
        raise TypeError('Another Patient with This National Number is Exists in This Hospital!')


def CheckDoctorNationalNumberIsExists(NationalNumber: str):
    """Check Given Doctor National Number is Exists in DataBase or not

    Args:
        NationalNumber (str): The National Number

    Raises:
        KeyError: when Given National Number Exists in DataBase
    """
    if len(list(filter(lambda x: x[1] == NationalNumber, AllDoctors()))) > 0:
        raise TypeError('Another Doctor with This National Number is Exists in This Hospital!')


def CheckMedicineNameIsExists(Name: str):
    """Check Given Medicine Name is Exists in DataBase or not

    Args:
        Name (str): The Medicine Name

    Raises:
        KeyError: when Given Medicine Name Exists in DataBase
    """
    if len(list(filter(lambda x: x[1] == Name, AllMedicines()))) > 0:
        raise TypeError('Another Medicine with Same Name is Already Exists!')


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

    if int(Age) < 1:
        raise TypeError('Minimum Age is 1!')


def CheckDoctorInput(Type: str) -> None:
    """Check Class ```Doctor``` Arg(s) to be Right Shape

    Args:
        Type (str): Doctor Type

    Raises:
        TypeError: When ```Type``` isn't in Types There is in Hospital
    """
    # if NationalNumber in list(map(lambda x: x[1], AllDoctors())):
    #     raise TypeError('This Doctor Has Already Exist in This Hospital!')

    if Type == "":
        raise TypeError('Doctor Type Cannot be Empty!')

    if Type not in TypeList:
        raise TypeError("Type is Invalid!")


def CheckPatientInput(NationalNumber: str, VisitorDoctorNationalNumber: str, Sickness: str) -> None:
    """Check Class ```Patient``` Arg(s) to be Right Shape

    Args:
        NationalNumber (str): National Number of Patient
        VisitorDoctorNationalNumber (str): Visitor Doctor's National Number

    Raises:
        TypeError: When ```VisitorDoctorNationalNumber``` is not in Hospital's Doctors
        PermissionError: When A Doctor Cannot be Own Doctor(```NationalNumber``` = ```VisitorDoctorNationalNumber```)
    """
    if all(list(map(lambda x: ord(x) == 10 or ord(x) == 32, Sickness))):
        raise TypeError('Sickness Cannot be Empty!')

    Doctors = list(map(lambda x: x[1], AllDoctors()))
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

    if len(Name) > 30:
        raise TypeError("Drug Name is too Long!")   

    if  all(list(map(lambda x: ord(x) == 10 or ord(x) == 32, Description))):
        raise TypeError('Description Cannot be Empty!')

    if Stock == "":
        raise TypeError('Stock Cannot be Empty!')

    try:
        int(Stock)
    except:
        raise TypeError("Stock doesn't Should Be Contains Characters!")

    if int(Stock) < 0:
        raise TypeError('Stock Cannot be Negative!')

HospitalPageHelp = '''
Patient Page:
 حذف، اضافه یا ویرایش بیماران 

Doctor Page:
 حذف، اضافه یا ویرایش پزشکان 

Drug Page:
حذف، اضافه یا ویرایش دارو ها

Exit:
خروج از برنامه '''

PatientPageHelp = '''
 بصورت پیشفرض همه بیماران در لیست نمایش داده می شوند و با دابل کلیک کردن روی هر بیمار اطلاعات آن را مشاهده کنید

Add Patient:
اضافه کردن بیمار جدید

Search Patient:
 جستجوی بیمار بر اساس نام یا نام خانوادگی
 نتیجه جستجو در لیست نمایش داده میشود

Show All Patients:
بازگرداندن لیست به حالت دیفالت - کارایی این دکمه بعد از اتمام عملیات جستجو می باشد

Back:
بازگشت به صفحه قبل'''

AddPatientsHelp = '''
First Name:
نام بیمار - نباید خالی یا شامل عدد باشد

Last Name:
نام خانوادگی بیمار - نباید خالی یا شامل عدد باشد

Age:
سن بیمار - نباید خالی یا شامل حروف باشدهمچنین نمیتواند کمتر از 1 یا بیشتر از 130 باشد

Doctor Name: 
نام پزشک معالج - از لیست موجود انتخاب شود، نباید خالی باشد

National Number:
کد ملی بیمار - نباید خالی یا شامل حروف باشد و بایستی 10 رقمی باشد همچنین این مقدار برای هر بیمار منحصر به فرد است

Sickness:
توضیحی در مورد مشکل بیمار - نباید خالی باشد

Save:
ذخیره اطلاعات وارد شده

Back:
بازگشت به صفحه قبل'''

# SearchPatientHelp = '''
# با وارد کردن هر یک از نام یا نام خانوادگی بیمار میتوانید به جستجوی بیمار بپردازید
# نتیجه جستجو در لیست نمایش داده میشود
# '''

UpdateAndDeletePatientsHelp = '''
در این صفحه می توانید به ویرایش اطلاعات یک بیمار یا حذف آن بپردازید

First Name:
نام بیمار - نباید خالی یا شامل عدد باشد

Last Name:
نام خانوادگی بیمار - نباید خالی یا شامل عدد باشد

Age:
سن بیمار - نباید خالی یا شامل حروف باشد همچنین نمیتواند کمتر از 1 یا بیشتر از 130 باشد

Doctor Name: 
نام پزشک معالج - از لیست موجود انتخاب شود، نباید خالی باشد

National Number:
کد ملی بیمار - نباید خالی یا شامل حروف باشد و بایستی 10 رقمی باشد همچنین این مقدار برای هر بیمار منحصر به فرد است

Sickness:
توضیحی در مورد مشکل بیمار - نباید خالی باشد

Update:
ذخیره اطلاعات ویرایش شده

Delete:
حذف بیمار از بانک اطلاعاتی بیمارستان

Back:
بازگشت به صفحه قبل'''

DoctorPageHelp = '''
 بصورت پیشفرض همه پزشکان در لیست نمایش داده می شوند و با دابل کلیک کردن روی هر پزشک اطلاعات آن را مشاهده کنید

Add Doctor:
اضافه کردن پزشک جدید

Search Doctor:
جستجوی پزشک بر اساس نام یا نام خانوادگی یا نوع
نتیجه جستجو در لیست نمایش داده میشود

Show All Doctors:
بازگرداندن لیست به حالت دیفالت - کارایی این دکمه بعد از اتمام عملیات جستجو می باشد

Back:
بازگشت به صفحه قبل'''

AddDoctorsHelp = '''
First Name:
نام پزشک - نباید خالی یا شامل عدد باشد

Last Name:
نام خانوادگی پزشک - نباید خالی یا شامل عدد باشد

Age:
سن پزشک - نباید خالی یا شامل حروف باشدهمچنین نمیتواند کمتر از 1 یا بیشتر از 130 باشد

National Number:
کد ملی پزشک - نباید خالی یا شامل حروف باشد و بایستی 10 رقمی باشد همچنین این مقدار برای هر پزشک منحصر به فرد است

Type:
نوع پزشک - مثلا عمومی، چشم پزشک و... - نباید خالی باشد

Save:
ذخیره اطلاعات وارد شده

Back:
بازگشت به صفحه قبل'''

# SearchDoctorHelp = '''
# با وارد کردن هر یک از نام یا نام خانوادگی یا نوع پزشک میتوانید به جستجوی پزشک بپردازید
# نتیجه جستجو در لیست نمایش داده میشود
# '''

UpdateAndDeleteDoctorsHelp = '''
در این صفحه می توانید به ویرایش اطلاعات یک پزشک یا حذف آن بپردازید

First Name:
نام پزشک - نباید خالی یا شامل عدد باشد

Last Name:
نام خانوادگی پزشک - نباید خالی یا شامل عدد باشد

Age:
سن پزشک - نباید خالی یا شامل حروف باشدهمچنین نمیتواند کمتر از 1 یا بیشتر از 130 باشد

National Number:
کد ملی پزشک - نباید خالی یا شامل حروف باشد و بایستی 10 رقمی باشد همچنین این مقدار برای هر پزشک منحصر به فرد است

Type:
نوع پزشک - مثلا عمومی، چشم پزشک و... - نباید خالی باشد

Update:
ذخیره اطلاعات ویرایش شده

Delete:
حذف پزشک از بانک اطلاعاتی بیمارستان 
توجه داشته باشید هنگام حذف یک پزشک، بیمارانی که پزشک حذف شده، پزشک معالج آن ها بوده است، در صورت وجود 
پزشک با نوع مشابه، بصورت تصادفی یک پزشک معالج دیگر به آنها تخصیص خواهد یافت و در صورت عدم وجود پزشکی 
با نوع مشابه، بیمار نیز حذف خواهد شد

Back:
بازگشت به صفحه قبل'''

DrugPageHelp = '''
بصورت پیشفرض همه دارو های موجود در بیمارستان در لیست نمایش داده می شوند 
و با دابل کلیک کردن روی هر دارو اطلاعات آن را مشاهده کنید

Add Drug:
اضافه کردن داروی جدید

Search Drug:
 جستجوی دارو بر اساس نام
 نتیجه جستجو در لیست نمایش داده میشود

Show All Drugs:
بازگرداندن لیست به حالت دیفالت - کارایی این دکمه بعد از اتمام عملیات جستجو می باشد

Back:
بازگشت به صفحه قبل'''

AddDrugsHelp = '''
Name:
نام دارو - نباید خالی باشد. توجه داشته باشید نام دارو برای هر دارو منحصر به فرد است

Stock:
موجودی انبار - نباید خالی یا شامل حروف باشدهمچنین نمیتواند منفی باشد

Description:
توضیحات در مورد تاثیرات و عملکرد دارو - نباید خالی باشد

Save:
ذخیره اطلاعات وارد شده

Back:
بازگشت به صفحه قبل'''

SearchDrugHelp = '''
با وارد کردن نام دارو میتوانید به جستجوی دارو بپردازید
نتیجه جستجو در لیست نمایش داده میشود
'''

UpdateAndDeleteDrugsHelp = '''
در این صفحه می توانید به ویرایش اطلاعات یک دارو یا حذف آن بپردازید

Name:
نام دارو - نباید خالی باشد. توجه داشته باشید نام دارو برای هر دارو منحصر به فرد است

Stock:
موجودی انبار - نباید خالی یا شامل حروف باشدهمچنین نمیتواند منفی باشد
در اپدیت دارو نمیتوان مستقیما به این ویژگی دسترسی داشت همچنین
.با دکمه های خرید یا فروش میتوانید موجودی انبار را تغییر دهید
ابتدا تعداد را در ورودی مربوطه وارد کرده و یکی از دکمه های خرید یا فروش را فشار دهید

Description:
توضیحات در مورد تاثیرات و عملکرد دارو - نباید خالی باشد

Update:
ذخیره اطلاعات ویرایش شده

Delete:
حذف دارو از بانک اطلاعاتی بیمارستان 

Back:
بازگشت به صفحه قبل'''