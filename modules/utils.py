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

def validasi_email(email):
    bagian = email.split('@')
    
    for karakter in email:
        if not (karakter.isalnum() or karakter in '.@'):
            return False
    
    if not email or email.count('@') != 1:
        return False

    if len(bagian[0]) == 0 or len(bagian[1]) == 0:
        return False
    
    if '.' not in bagian[1]:
        return False
    
    if bagian[1].startswith('.') or bagian[1].endswith('.'):
        return False
    
    return True