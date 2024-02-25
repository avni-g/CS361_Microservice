import requests 
import time
import json

def post_values(): 

    URL = "http://localhost:5000/api/healthdata/post"

    print("Input patient ID, systolic bp, diastolic bp, weight, and height.")
    print("Patient ID:")
    patient_id = input()
    if patient_id == '':
        patient_id = None
    print("Systolic BP:")
    sys_bp = input()
    if sys_bp == '':
        sys_bp = None 
    print("Diastolic BP:")
    dia_bp = input()
    if dia_bp == '':
        dia_bp = None
    print("Weight in LB:")
    weight_lb = input()
    if weight_lb == '':
        weight_lb = None
    print("Height in IN:")
    height_in = input()
    if height_in == '':
        height_in = None

    values = {
        "patient_id": patient_id,
        "sys_bp": sys_bp,
        "dia_bp": dia_bp,
        "weight_lbs": weight_lb,
        "height_inches": height_in
    }

    r = requests.post(url = URL, data = values)

    if r.status_code == 200: 
        print("Post request successful!")
        print("Response:", r.text)
    else:
        print("Post request failed with status code:", r.status_code)

    return


def get_values(): 

    URL = "http://localhost:5000/api/healthdata"

    g = requests.get(url = URL)
    data = g.json()
    for item in data:
        print(item, "\r\n")
    time.sleep(2)
    return 

def get_value(ID):
    URL = f"http://localhost:5000/api/healthdata/{ID}"

    g_i = requests.get(url = URL)
    data = g_i.json()
    #for item, value in data.items():
    #   print(item, ":", value, "\r\n")
    for item in data:
        print(item, "\r\n")
    time.sleep(2)
    return 

"""
def put_value(ID):
    URL = f"http://localhost:5000/vitals/{ID}"
    
    get_value(ID)
    
    print("Input systolic bp, diastolic bp, weight, and height.")
    print("Systolic BP:")
    sys_bp = input()
    print("Diastolic BP:")
    dia_bp = input()
    print("Weight in LB:")
    weight_lb = input()
    print("Height in IN:")
    height_in = input()

    values = {
        "sys_bp": int(sys_bp),
        "dia_bp": int(dia_bp),
        "weight_lbs": float(weight_lb),
        "height_inches": int(height_in)
        }

    p = requests.put(url = URL, json = values)
    return 

def delete_value(ID):
    URL = f"http://localhost:5000/vitals/{ID}"

    d = requests.delete(url = URL)
    return 

"""
while True: 
    print("What would you like to do? Choose from the following:"
          "Select 1 to POST a value.\r\n"
          "Select 2 to GET all values.\r\n"
          "Select 3 to GET all values for a patient.\r\n"
          "Type * to exit.\r\n"
            )
    action = input()
    if action == "1":
        post_values()
    elif action == "2":
        get_values()
    elif action == "3":
        print("Which patient ID would you like to look up data for?")
        id = input()
        get_value(id)
    elif action == "*":
        break



# data = g.json()
# print(data)
