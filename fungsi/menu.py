import os

"""fungsi menu"""
title = '''
==========================================
      SELAMAT DATANG DI TOOLS UNTUK
          MENGHITUNG OSILOSCOP
==========================================
'''
def menu(list_1: str | None, list_2: str | None, list_3: str | None, list_4: str | None) -> None:
    """
    fungsi menu
      ==========================================
            SELAMAT DATANG DI TOOLS UNTUK
      MENGHITUNG BEBERAPA PERHITUNGAN MATEMATIKA
      ==========================================
    title_set: menempilakn sebuah judul
    list_1: list ke 1
    list_2: list ke 2
    list_3: list ke 3
    list_4: list ke 4
    """
    win = 'cls'
    linux = 'clear'
    os.system([linux, win][os.name == 'nt'])
    print(title)
    print(f'{list_1}\n'
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