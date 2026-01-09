import os
import msvcrt

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

def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    pw = ""
    while True:
        ch = msvcrt.getch()
        if ch in {b"\r", b"\n"}:  # Enter
            print()
            return pw
        if ch == b"\x08":  # Backspace
            if pw:
                pw = pw[:-1]; print("\b \b", end="", flush=True)
            continue
        if ch in {b"\x00", b"\xe0"}:  # Tombol fungsi → abaikan
            msvcrt.getch(); continue
        pw += ch.decode(); print("*", end="", flush=True)

def format_email(email):
    # membagi email menjadi dua bagian, dipisahkan dengan '@'
    bagian = email.split('@')
    
    # mengecek format tidak kosong
    if not email:
        print("❌ Email tidak boleh kosong ❌")
        return False
    
    # mengecek karakter pada email agar hanya mengandung alfabet, angka, titik, dan '@'
    for karakter in email:
        if not (karakter.isalnum() or karakter in '.@'):
            print("❌ Karakter hanya boleh berupa alfabet (a-z), angka (0-9), titik (.), dan @ ❌")
            return False
    
    # mengecek hanya ada satu '@'
    if email.count('@') != 1:
        print("❌ Format email salah ❌")
        return False

    # mengecek bagian sebelum dan sesudah '@' tidak kosong
    if len(bagian[0]) < 6 or len(bagian[0]) > 30:
        print("❌ Maaf, panjang username email Anda harus antara 6 karakter dan 30 karakter ❌")
        return False
    
    if len(bagian[1]) == 0:
        print("❌ Format email salah ❌")
        return False
    
    # mengecek hanya ada satu titik pada bagian domain email (bagian setelah '@')
    if bagian[1].count('.') > 3:
        print("❌ Format email salah ❌") 
        return False
    
    # mengecek bagian domain email tidak diawali dan diakhiri dengan titik
    if bagian[1].startswith('.') or bagian[1].endswith('.'):
        print("❌ Format email salah ❌")
        return False
    
    # mengecek bagian sebelum domain email berawalan karakter ASCII atau angka
    if not (bagian[0][0].isalnum()):
        print("❌ Maaf, Karakter awal username email harus berupa alfabet (a-z) atau angka (0-9) ❌")
        return False
    
    # mengecek bagian sebelum domain email berakhiran karakter ASCII atau angka
    if not (bagian[0][-1].isalnum()):
        print("❌ Maaf, Karakter akhir username email harus berupa alfabet (a-z) atau angka (0-9) ❌")
        return False

def ada_huruf(text):
    for char in text:
        if char.isalpha():
            return True
    return False