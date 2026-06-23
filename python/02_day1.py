
num1=int(input("Enter your 1st number: "))
num2=int(input("Enter your 2nd number: "))
print("Operation Available\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floor Division")
op=int(input("Enter your choice : "))
if(op==1):
    print(num1+num2)
elif(op==2):
    print(num1-num2)
elif(op==3):
    print(num1*num2)
elif(op==4):
    if (num2==0):
        print("Error!!! Denominator cant be zero")
    else:
        print(num1/num2)
elif(op==5):
    if (num2==0):
        print("Error!!! Denominator cant be zero")
    else:
        print(num1//num2)
else:
    print("Invalid Choice!!!")