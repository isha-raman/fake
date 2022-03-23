#installed faker through pycharm terminal
from faker import Faker
fake = Faker()
#print(fake.name())
#print(fake.email())
#print(fake.country())

#print(fake.profile())

#print(fake.text())

#data = fake.profile()
#print(data)
#for x,y in data.items():
#    print(f"{x} : {y}")

for x in range(10):
    data = fake.profile()
    print("Profile:",x+1) #x+1 starts the counting from 1 instead of 0
    print() #creates a blank line
    for x, y in data.items():
        print(f"{x} : {y}")
    print()