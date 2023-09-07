import os

"""fungsi menu"""
def menu(title = "", title_sec = "", list_1 = "", list_2 = "", list_3 = "", list_4 = ""):
    os.system('cls')
    print('='* 50)
    print(title)
    print('='* 50)
    print(f'{title_sec}\n\n'
          f'{list_1}\n'
          f'{list_2}\n'
          f'{list_3}\n'
          f'{list_4}')
    


# alfa()