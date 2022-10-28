# length of list using naive method
 
# Initializing list
test_list = [1, 4, 5, 7, 8]

# Finding length of list
# using loop
# Initializing counter
counter = 0
for i in test_list:
 
    # incrementing counter
    counter = counter + 1
 
# Printing length of list
print("Length of list using naive method is : " + str(counter))

# Using len()

print("The length of list is: ", len(test_list))

# using len() and length_hint
from operator import length_hint
 
 
# Finding length of list
# using length_hint()

list_len_hint = length_hint(test_list)
 
# Printing length of list
print("Length of list using length_hint() is : " + str(list_len_hint))
