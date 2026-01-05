# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_BUKTI_PROMOSI

# function untuk mengambil data bukti_promosi
def data_bukti_promosi():
    if not os.path.exists(DATA_BUKTI_PROMOSI):
        return []
    
    with open(DATA_BUKTI_PROMOSI, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# procedure untuk menyimpan data ke dalam file data bukti_promosi
def simpan_bukti_promosi(data_baru):
    file_ada = os.path.exists(DATA_BUKTI_PROMOSI)
        
    with open(DATA_BUKTI_PROMOSI, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
        writer.writerow(data_baru)