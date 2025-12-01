import json
from data.config import DATA_UMKM

def load_umkm():
    with open(DATA_UMKM, "r") as f:
        return json.load(f)

def save_umkm(data):
    with open(DATA_UMKM, "w") as f:
        json.dump(data, f, indent=4)

def add_umkm(data_baru):
    data = load_umkm()
    data.append(data_baru)
    save_umkm(data)