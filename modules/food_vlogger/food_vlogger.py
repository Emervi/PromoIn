# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_FOOD_VLOGGER

# function untuk mengambil data Food Vlogger
def data_fv():
    if not os.path.exists(DATA_FOOD_VLOGGER):
        return []
    
    with open(DATA_FOOD_VLOGGER, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)


# procedure untuk menyimpan data ke dalam file data Food Vlogger
def simpan_fv(data_baru):
    file_ada = os.path.exists(DATA_FOOD_VLOGGER)
        
    with open(DATA_FOOD_VLOGGER, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
        writer.writerow(data_baru)