import os

"""fungsi menu"""
title = '''
==========================================
      SELAMAT DATANG DI TOOLS UNTUK
MENGHITUNG BEBERAPA PERHITUNGAN MATEMATIKA
==========================================
'''
def menu(title_sec: str, list_1: str, list_2: str, list_3: str, list_4: str):
    """
    fungsi menu
      ==========================================
            SELAMAT DATANG DI TOOLS UNTUK
      MENGHITUNG BEBERAPA PERHITUNGAN MATEMATIKA
      ==========================================
    
    """
    win = 'cls'
    linux = 'clear'
    os.system([linux, win][os.name == 'nt'])
    print(title)
    print(f'{title_sec}\n\n'
          f'{list_1}\n'
          f'{list_2}\n'
          f'{list_3}\n'
          f'{list_4}')
    
def alfa():
    """
    mengembalikan sebuah huruf alfabet kapital ataupun kecil
    """
    low_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z']
    big_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Z']
    all_alfa = low_alfa + big_alfa
    return all_alfa


def type_int(var):
    return type(var) == int

def cek_input(user_one, user_second):
    """
    fungsi untuk memengecek input int
    """
    if (type_int(user_one) and type_int(user_second)):
        return user_one, user_second
    
    else:
        print("Masukan angka please!!")
        return False