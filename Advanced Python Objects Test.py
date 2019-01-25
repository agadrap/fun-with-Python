#---ADVANCED NUMBERS---

#convert 1024 to binary and hexadecimal
number = 1024
binary_number = bin(number)
hex_number = hex(number)

#round 5.23222 to two decimal points
round(5.23222,2)

#---ADVANCED STRINGS---

#check if every letter in the string is lower case
s = "hello how are you Mary, are you feeling okay?"
s.islower()
#returns False because of Mary

#how many times does 'w' show up in the sentence
st = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
st.count('w')

#---ADVANCED SETS-----

# find the elements in set1 that are not in set2
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
set1.difference(set2)

#find all elements that are in either set
set1.union(set2)

#---ADVANCED DICTIONARIES---

#create dictionary {0:0,1:1,2:8,3:27,4:64}
{x:x**3 for x in range(5)}

#---ADVANCED LISTS----

#reverse the list 
list1.reverse()
#this itself doesnt carry value cannot be assigned but it changes the original list permanently
list3 = list1[::-1]

#sort the list
list2 = [3,4,2,5,1]
list2.sort()
print(list2)
