

import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state



with open('D:\\employee1.json', 'r') as f:
    data = json.load(f)


employees = []
for employee in data['employees']:
    employees.append(Employee(employee['Name'], employee['DOB'], employee['Height'], employee['City'], employee['State']))

for employee in employees:
   print(employee.__dict__)

