# Problem Statement : Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers. 

from functools import reduce

def Equals(List):
    if(List >= 70 and List <= 90):
        return List
    
def Increase(List):
    List = List + 10
    return List

def Product(No1, No2):
    Ans = No1 * No2
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
# Input  : List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
#          List after filter = [76, 89, 86, 90, 70] 
#          List after map = [86, 99, 96, 100, 80] 
# Output : of reduce = 6538752000