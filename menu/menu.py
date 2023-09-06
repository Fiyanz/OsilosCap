import os

def alfa():
    low_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z']
    big_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Z']
    all_alfa = low_alfa + big_alfa
    return all_alfa

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