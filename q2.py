
dog = {} #empty dictionary
dog["name"] = "Max"
dog["colour"] = "Brown"
dog["breed"] = "German Shepherd"
dog["legs"] = 4
dog["age"] = 6
print(dog)

Student = {} #empty student dict
Student["First_name"] = "jack"   #adding keys and values
Student["Last_name"] = "son"
Student["gender"] = "male"
Student["Age"] = 21
Student["marital_status"] = "not married"
Student["Skills"] = ['fast learner', 'programmer', 'hacker']
Student["Country"] = "India"
Student["City"] = "Hyderabad"
Student["address"] = "6-1-87"
print(Student)
print('length of student',len(Student)) #finding length
print("value of skills is ", Student["Skills"]) #printing value of skills
print('data_type of value of skills is ', type(Student["Skills"])) #finding type of skills value
Student["Skills"].append('java') #adding skills
Student["Skills"].append('python')
keys=[] #list of keys
values=[] #list of values
for i in Student:
    values.append(Student[i]) #adding values to values list
    keys.append(i) #adding keys to keys list
print("keys are ", keys)
print("values are ", values)
