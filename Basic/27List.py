my_list = [10, 20, 30, 40, 50, 60]

my_list.sort()  #nothing return change og List  and if apply mixed datatype get error
print(my_list)
my_list.reverse()
print(my_list) #nothing return change og List
print(min(my_list))
print(max(my_list))
my_list.append(54)
my_list.insert(2,43) #insert in index
print(my_list)
my_list.extend([1,2,3,4,5]) #add multiple value at the end
print(my_list)
my_list[0]=99

print(my_list)
my_list[1:4]=[22,22,22];  # i to 4 and 4 is lenght not index
print(my_list)
my_list.remove(22)   #only first occurance is remove 
print(my_list)
print(my_list.pop())  #remove and return
print(my_list.pop(3))  #index
print(my_list.count(22) )  #index