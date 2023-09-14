import os

"""fungsi menu"""
title = '''
==========================================
      SELAMAT DATANG DI TOOLS UNTUK
MENGHITUNG BEBERAPA PERHITUNGAN MATEMATIKA
==========================================
'''
def menu(title_sec = "", list_1 = "", list_2 = "", list_3 = "", list_4 = ""):
    os.system('cls')
    print(title)
    print(f'{title_sec}\n\n'
          f'{list_1}\n'
          f'{list_2}\n'
          f'{list_3}\n'
          f'{list_4}')
    


