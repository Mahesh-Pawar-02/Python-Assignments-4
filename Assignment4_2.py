# Problem Statement : Write a program which contains one lambda function which accepts two parameters and return its multiplication. 
 
Multiplication = lambda No1, No2 : No1 * No2

def main():
    print("Enetr First number : ",end=" ")
    Value1 = int(input())

    print("Enetr second number : ",end=" ")
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)

    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()

# Test Case : 1
# Input  : Enetr first number : 5
# Input  : Enetr second number : 2
# Output : Multiplication is : 10

# Test Case : 2
# Input  : Enetr first number : 11
# Input  : Enetr second number : 21
# Output : Multiplication is : 231