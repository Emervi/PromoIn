import os

# merapihkan tampilan sistem
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# mengecek apakah nilai yang diterima berupa int
def apakah_int(nilai):
    try:
        int(nilai)
        return True
    
    except ValueError:
        return False