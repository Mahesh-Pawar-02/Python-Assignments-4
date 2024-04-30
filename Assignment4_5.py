# Problem Statement : Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the 
# numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number 
# from that numbers. (We use normal functions instead of lambda functions).

from functools import reduce

def Prime(List):
    if List <= 1:
        return False
    for i in range(2, int(List**0.5) + 1):
        if List % i == 0:
            return False
    return True
    
def Multiplication(List):
    List = List * 2
    return List

def Maximum(List,Max):
    if(List > Max):
            Max = List
    return Max

def main():
    Data = []

    print("Enter number of elements : ", end = "")
    Size = int(input())

    print("Enter the elements : ")
    for No in range(Size):
        No = int(input())
        Data.append(No)
    
    FilterData = list(filter(Prime,Data))
    print("Data after filter activity : ",FilterData)

    MapData = list(map(Multiplication,FilterData))
    print("Data after map activity : ",MapData)

    ReduceData = reduce(Maximum,MapData)
    print("Data after reduce activity : ",ReduceData)

if __name__ == "__main__":
    main()

# Test Case : 1
# Input  : List = [2, 70 , 11, 10, 17, 23, 31, 77]  
#          List after filter = [2, 11, 17, 23, 31] 
#          List after map = [4, 22, 34, 46, 62]
# Output : of reduce = 62