# try:
    """
    num1 = int(input("Enter the number1 : "))
    num2 = int(input("Enter the number2 : "))
    result = num1/num2
    print("Division result for " ,num1, "and ", num2 ," = ", result)
    """
    """
    # primenumbers = []
    num=int(input("Enter an even number"))
    assert num%2==0
except ZeroDivisionError:
    print("Error : Denominator cannot be zero")#ZeroDevisionerror
except IndexError:
    # print("Error Direct insertion with list not possible")
    print("The value cannot be even")
else:
    print(num)
finally:
    print("Program is ended ")
    # num = int(input("Enter the value to be inserted : "))
    # prime_numbers.append(num)
    """
yob = int(input("Enter the year of birth : "))
age=2024-yob
if age<18:
    raise Exception(f' age shoulf be greater tgan 18 and you have your {age}')
