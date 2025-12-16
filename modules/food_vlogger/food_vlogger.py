# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_FOOD_VLOGGER

# function untuk mengambil data Food Vlogger
def data_fv():
    data = []
    
    if not os.path.exists(DATA_FOOD_VLOGGER):
        return []
    
    with open(DATA_FOOD_VLOGGER, mode="r", newline='') as file:
        reader = csv.reader(file)
        for baris in reader:
            data.append(baris)
            
    return data

# procedure untuk menyimpan data ke dalam file data Food Vlogger
def simpan_fv(data_user):
    with open(DATA_FOOD_VLOGGER, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_user)