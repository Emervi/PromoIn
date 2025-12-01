import json
from data.config import DATA_FOOD_VLOGGER

def load_fv():
    with open(DATA_FOOD_VLOGGER, "r") as f:
        return json.load(f)

def save_fv(data):
    with open(DATA_FOOD_VLOGGER, "w") as f:
        json.dump(data, f, indent=4)

def add_fv(data_baru):
    data = load_fv()
    data.append(data_baru)
    save_fv(data)