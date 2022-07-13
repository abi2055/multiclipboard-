import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"
# All clipboard data will be saved in a json filed titled this 

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
# Function saves whatever is in clipboard and writes it to the json file 

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
# Function loads the data or reads the data in the json file at the users discretion and returns it 
# it tries to read data if it exists otherwise nothing happens 


if len(sys.argv) == 2:
    command = sys.argv[1]
    # takes the comman prompt as the second string in the list after the file name 
    data = load_data(SAVED_DATA)
    # loads data from the clipboard to the file (writes it in)
    
    if command == "save": 
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Date Saved!")
    # if the user command is save, whatever is in your clipboard at the moment will be saved under
    # a unique key indicated by the user within a json file dictionary 
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key does no exist")
    # if the user command is load, whatever key is inputted will load the data associated to your clipbaord 
    # in the json dictionary otherwise if an invalid key is inputted the data will not load 
    elif command == "list":
        print(data)
    # this command simply prints the list of keys and data stored in the json file 
    else:
        print("Unknown Command")
    # if none of the commands indicated above are inputted, this "error" message comes up
else:
    print("Please pass exactly one command!")
# multiple commands cannot be entered for obvious reasons, so the program exception handles for one command 