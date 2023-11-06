#python3
# Json Example

import json

student = {
    'firstName' : 'Joe',
    'lastName' : "Lunchbox",
    'grade' : 12,
    'studentNumber' : 19333,
    'block' : {
        'A' : "Math",
        'B' : "English",
        'C' : "PE",
        'D' : "Basket Weaving"

    }
}
encoded = json.dumps(student)

print('student')
print(type(student))
print(student)
print('\n\n')
print('encoded')
print(type(encoded))
print(encoded)