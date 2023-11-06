#python3
# Json Example

import json

numbers = [3,4,5]
encodedNumbers = json.dumps(numbers)
print("numbers",numbers)
print(f"numbers is a variable of type : {type(numbers)} and contains {numbers}")
print(f"encodedNumbers is a variable of type {type(encodedNumbers)} and contains {encodedNumbers}")

decoded = json.loads(encodedNumbers)
print(f"decodedNumbers is a variable of type {type(decoded)} and contains {decoded}")
