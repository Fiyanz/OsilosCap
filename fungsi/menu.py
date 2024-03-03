import os

"""fungsi menu"""
title = '''
==========================================
      SELAMAT DATANG DI TOOLS UNTUK
          MENGHITUNG OSILOSCOP
==========================================
'''
def menu(list_1: str | None = '', 
         list_2: str | None = '', 
         list_3: str | None = '', 
         list_4: str | None = '') -> None:
    """
    fungsi menu
        ==========================================
              SELAMAT DATANG DI TOOLS UNTUK
                  MENGHITUNG OSILOSCOP
        ==========================================
    title_set: menempilakn sebuah judul
    list_1: list ke 1
    list_2: list ke 2
    list_3: list ke 3
    list_4: list ke 4
    """
    clear()
    print(title)
    print(f'{list_1}\n'
          f'{list_2}\n'
          f'{list_3}\n'
          f'{list_4}')
    
def clear() -> None:
    win = 'cls'
    linux = 'clear'
    os.system([linux, win][os.name == 'nt'])


