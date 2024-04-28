# Problem Statement : Write a program which contains one lambda function which accepts one parameter and return power of two.
 
Power = lambda Value : Value ** 2

def main():
    print("Enetr number : ",end=" ")
    No = int(input())

    Ret = Power(No)

    print("Power of two is : ",Ret)

if __name__ == "__main__":
    main()

# Test Case : 1
# Input  : Enetr number : 4
# Output : Power of two is : 16

# Test Case : 2
# Input  : Enetr number : 6
# Output : Power of two is : 36