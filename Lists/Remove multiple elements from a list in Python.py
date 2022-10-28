# Python program to remove multiple
# elements from a list
 
# creating a list
list1 = [11, 5, 17, 18, 23, 50]
 
# Iterate each element in list
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)
 
# printing modified list
print("New list after removing all even numbers: ", list1)

#now removing odd numbers from original list list1...

list1 = [11, 5, 17, 18, 23, 50]
 
# Iterate each element in list
for ele in list1:
    if ele % 2 != 0:
        list1.remove(ele)
 
# printing modified list
print("New list after removing all odd numbers: ", list1)
