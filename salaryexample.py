allowances={"HRA":0.4,"DA":0.30, "TA":0.15}
deductions = {"PF":0.12, "Insurance":5000}
def calculateAllowances(basic):
    total_allowances=0
    for key in allowances:
        total_allowances+=allowances[key]*basic
    return total_allowances
def calculateDeductions(basic):
    total_deductions = 0
    for key in deductions:
        if type(deductions[key]) is not int:
            total_deductions += deductions[key] * basic
        else:
            total_deductions += deductions[key]
    return total_deductions

def professionaltax(msal):
    prof_tax=0
    if msal>=8500 and msal<=10000:
        prof_tax==200
    elif msal>10000 and msal<=30000:
        prof_tax=300
    elif msal > 30000:
        prof_tax = 500
    return prof_tax

def calculatesalary():
    gsal = basic + calculateAllowances((basic))
    ptax=professionaltax(gsal)
    nsal=gsal - ptax- calculateDeductions(basic)
    print("basic salary", basic)
    print("Allowances", calculateAllowances(basic))
    print("Deductions", calculateDeductions(basic))
    print("Professional tax",ptax)
    print("Gross salary",gsal)
    print("Net salary ",nsal)


print("-" * 25 , "Salary calculator : ","-" * 25)
basic = int(input("Enter your basic salary"))
calculatesalary()