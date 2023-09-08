from all_fungsi.menu import menu
from all_fungsi.alfa import alfa
from osiloscop.osiloscop import osiloscop
from luas_persegi.luas_persegi import luas_persegi_panjang

import os
  
        
"""main fungsion"""
def main():
    loop = True

    while loop:
        menu("tools simple kalkulator",
            "",
            "1. Osiloscop",
            "2. luas persegi panjang",
            "3. GLBB",)
        try:
            input_user = int(input("Pilih Metode Perhitungan: "))
            """pemangilan fungsi osiloscop"""
            if input_user == 1:
                osiloscop()
                os.system('cls')
            # """pemangilan fungsi persegi panjang"""
            # if input_user == 2:
            #     luas_persegi_panjang()
            #     os.system('cls')
            # """pemangilan fungsi persegi"""
            # if input_user == 1:
            #     luas_persegi_panjang()
            #     os.system('cls')
            # """pemangilan fungsi GLBB"""
            # if input_user == 1:
            #     luas_persegi_panjang()
            #     os.system('cls')


        except ValueError:
            exit_input = input("ingin keluar? ")
            if exit_input == 'x'or 'X' and not alfa():
                main()
            elif exit_input == 'y'or 'Y':
                loop = False
                os.system('cls')



if __name__ == "__main__":
    main()