import json
from data.config import DATA_FOOD_VLOGGER

def load_fv():
    with open(DATA_FOOD_VLOGGER, "r") as f:
        return json.load(f)

def save_fv(data):
    with open(DATA_FOOD_VLOGGER, "w") as f:
        json.dump(data, f, indent=4)

def register_fv(data_baru):
    data = load_fv()
    
    # input food vlogger baru
    nama = input("Masukan nama anda: ")
    email = input("Masukan email anda: ")
    password = input("Masukan password anda: ")
    
    # generate id baru untuk data
    id_baru = data[-1]["id"] + 1 if data else 1
    
    data_baru = {
        "id": id_baru,
        "nama": nama,
        "email": email,
        "password": password
    }
    
    data.append(data_baru)
    save_fv(data)