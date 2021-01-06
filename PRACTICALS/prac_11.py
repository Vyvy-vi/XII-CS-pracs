lst=eval(input("Enter list of numbers: "))

def bubble_sort(lst):
  n=len(lst)
  for i in range(n):
    for j in range(0,n-i-1):
      if lst[j]>lst[j+1]:
        lst[j],lst[j+1]=lst[j+1],lst[j]

bubble_sort(lst)
print("The sorted list is",lst)

def binary_search(lst,value):
  low=0
  high=len(lst)-1
  while low<=high:
    mid=(low+high)//2
    if lst[mid]==value:
      return mid
    elif lst[mid]<value:
      low=mid+1
    elif lst[mid]>value:
      high=mid-1
  else:
    return "Not found"

value1=int(input("Enter element to be searched (using binary search): "))
print("Using binary search",value1,"is found in the list at",binary_search(lst,value1))

def linear_search(lst,value):
  index=0
  while index<len(lst) and lst[index]<value:
    index+=1
  if index>=len(lst) or lst[index]!=value:
    return "Not found"
  return index

value2=int(input("Enter element to be searched (using linear search): "))
print("Using linear search",value2,"is found in the list at",linear_search(lst,value2))
