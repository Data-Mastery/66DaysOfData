### Packing & Unpacking

testlist = [1,2,3,4,5]
a, b, c, d, e = testlist
a, *b, c = testlist

packed = a, b, c
packed

teststring = "Ich bin ein String"
*splittet_string, = teststring
splittet_string

user = {"name": "Max", "password": "test"}
user

name, password = user.values()
name

def add_values(a, b, c):
    return a + b + c

add_values(1,2,3)
add_values(1, 2, 3, 4)

def add_values(*args):
    print(args)
    return sum(args)

add_values(1,2,3,4,5)

liste1 = [1,2,3]
liste2 = [5,4,3]

add_values(*liste1, *liste2)

# Nutzer aus Datenbank
customers = [
        {"firstname": "Max", "lastname": "Schmidt", "balance" : 2000},
        {"firstname": "John", "lastname": "Doe", "balance" : 1200},    
             ]

class Customer:
    def __init__(self, firstname, lastname, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

customer_obj = []
for person in customers:
    customer_obj.append(Customer(person["firstname"], person["lastname"], person["balance"]))
    

[Customer(person["firstname"], person["lastname"], person["balance"]) for person in customers]
[Customer(**person) for person in customers]

