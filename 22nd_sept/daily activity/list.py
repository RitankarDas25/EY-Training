#creating list
num =[10,20,30,40]
print(num)
print(num[0]) #1st element
print(num[-1]) # last elements
print(len(num)) # length of list
print(max(num)) #max element
print(min(num)) #min element
print(sum(num)) # sum of elements
print(sum(num)/len(num)) # average

fruits=["apple","banana","orange"]
#add
fruits.append("peach") #adds at end
fruits.insert(1,"abc") #adds at index

#remove
fruits.remove("banana") #removes element by name
fruits.pop() # removes last element
print(fruits)