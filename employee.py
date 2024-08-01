import datetime

today = datetime.date.today()
year=today.year

class company:
    def __init__(self, cname):
        self._cname= cname
    def displayCname(self):
        print("Company name", self._cname)
    def address(self):
        return "TechnoPark"+" "+"Trivandrum"
class Employee:
    isMarried = True
    empcount = 0
    def __init__(self,fname,lname,yob):
        self._fname = fname
        self._lname = lname
        self._age = year - yob
        Employee.empcount+=1
    def address(self):
        print("Employee Address: Rahatani , pune")
    def getEmpDetails(self):
        self.displayCname()
        print("Full Name : ",self._fname," ",self._lname)
        print("Age : ",self._age)
        print("Marital Status : ", self.isMarried)
        print("company Address:", super().)



e=Employee("Mubeen","TM",2001)
e.isMarried=False
e.getEmpDetails()

e1=Employee("Hane","Ashra",2000)

e1.getEmpDetails()
