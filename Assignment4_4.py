# Problem Statement : Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. 
# Reduce will return addition of all that numbers.

from functools import reduce

def Equals(List):
        if(List % 2 == 0):
            return List
    
def Increase(List):
    List = List * List
    return List

def Product(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    Data = []

    print("Enter number of elements : ", end = "")
    Size = int(input())

    print("Enter the elements : ")
    for No in range(Size):
        No = int(input())
        Data.append(No)
    
    FilterData = list(filter(Equals,Data))
    print("Data after filter activity : ",FilterData)

    MapData = list(map(Increase,FilterData))
    print("Data after map activity : ",MapData)

    ReduceData = reduce(Product,MapData)
    print("Data after reduce activity : ",ReduceData)

if __name__ == "__main__":
    main()

# Test Case : 1
# Input  : List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
#          List after filter = [2, 4, 4, 2, 8, 10] 
#          List after map = [4, 16, 16, 4, 64, 100] 
# Output : of reduce = 204