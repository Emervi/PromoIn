import csv
import os
from data.config import DATA_LAMARAN


# function untuk mengambil data lamaran
def data_lamaran():
    if not os.path.exists(DATA_LAMARAN):
        return []
    
    with open(DATA_LAMARAN, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# procedure untuk menyimpan data ke dalam file data lamaran
def simpan_lamaran(data_baru):

    file_ada = os.path.exists(DATA_LAMARAN)
        
    with open(DATA_LAMARAN, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
        writer.writerow(data_baru)

# procedure untuk mengupdate data lamaran
def update_lamaran(data_baru):

    with open(DATA_LAMARAN, mode="w", newline='') as file:
        nama_kolom = data_baru[0].keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)        
        writer.writeheader()
        writer.writerows(data_baru)