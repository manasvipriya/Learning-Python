# Python3 code to demonstrate working of
# Extract Indices of substring matches
# Using loop + enumerate()
 
# initializing list
test_list = ["vscode is good", "for begginers", "I love vscode", "Its useful"]
 
# initializing K
K = "Gfg"
 
# printing original list
print("The original list : " + str(test_list))
 
# using loop to iterate through list
res = []
for idx, ele in enumerate(test_list):
  if K in ele:
    res.append(idx)
 
# printing result
print("The indices list : " + str(res))