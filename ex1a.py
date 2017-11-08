numbers=[]
char=input("enter the number [or type end]")
while char != "end":
    n=int(char)
    numbers.append(n)
    char=input("enter the number [or type end]")
def bubble_sort ( num ):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]> num[j+1]:
                temp= num[j]
                num[j]= num[j+1]
                num[j+1]= temp
    return num
def insertion_sort(num):
    for i in range(1,len(num)):
        j = i                    
        while j > 0 and num[j] < num[j-1]:
            num[j], num[j-1] = num[j-1], num[j]
            j=j-1 
    return  num               
sorted_numbers1 = bubble_sort(numbers)
sorted_numbers2 = insertion_sort(numbers)
print("sorted by bubble sort", sorted_numbers1)
print("sorted by insertion sort", sorted_numbers2)
