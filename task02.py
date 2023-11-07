#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

url = 'http://sdcaf.hungrybeagle.com/menu.php'
response = requests.get(url)


# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains
if response.status_code == 200:
    try: 
        data = json.loads(response.text)
        if 'menu' in data:
            weekly_menu = data['menu']
            print("Weekly Menu:")
            for i, menu_item in enumerate(weekly_menu):
                print(f"Day {i + 1}: {menu_item}")
        else:
            print("JSON data does not contain a 'menu' key.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")