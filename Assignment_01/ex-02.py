class employee():
 def _init_(self,name,age,id,salary):
    #creating a function
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
 emp1 = employee("harshit",22,1000,1234) #creating objects
 emp2 = employee("arjun",23,2000,2234)
print(emp1._dict_) #Prints dictionary

dic = {1: 'geeks', 2: 'for', 3: 'geeks'}
print('original: ', dic)

# Accessing value for key
print(dic.get(1))

# Accessing keys for the dictionary
print(dic.keys())

# Accessing keys for the dictionary
print(dic.values())

# Printing all the items of the Dictionary
print(dic.items())