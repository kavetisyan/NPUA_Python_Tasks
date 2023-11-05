operators = ["+", "-", "/", "*"]

def calculate(num1, num2, operator):
    if(operator=="+") :
        return num1 + num2;
    elif(operator=="-") :
        return num1 - num2;
    elif(operator=="*") :
        return num1 * num2;
    elif(num2==0) :
        print("Can't divide on 0.");
    else:
        return num1/num2;

Num1 = float(input("Enter First Number: "));
Num2 = float(input("Enter Second Number: "));
Operator = input("Enter Operator, avaliable operators are: '+', '-', '/', '*' : ");
while(Operator not in operators):
    Operator = input("Invalid Operator, avaliable operators are: '+', '-', '/', '*' : ");
print("Result is : ", calculate(Num1, Num2, Operator));
