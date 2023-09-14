from all_fungsi.menu import menu
from all_fungsi.alfa import alfa
from osiloscop.osiloscop import osiloscop
from luas_persegi.luas_persegi import luas_persegi_panjang

import os
  
        
"""main fungsion"""
def main():
    loop = True

    while loop:
        menu("",
            "1. Osiloscop",
            "2. luas persegi panjang",
            "3. GLBB",)
        
        input_user = input("Pilih Metode Perhitungan: ")

        # pemangilan fungsi osiloscop
        if input_user == '1':
            osiloscop()
        #pemangilan fungsi persegi panjang
        elif input_user == '2':
            luas_persegi_panjang()
        # pemangilan fungsi persegi
        elif input_user == '3':
            luas_persegi_panjang()
        # pemangilan fungsi GLBB
        elif input_user == '4':
            luas_persegi_panjang()
        

        exit_input = input("ingin keluar? ")
        if exit_input == 'x'or 'X' and not alfa():
            main()
        elif exit_input == 'y'or 'Y':
            loop = False
            os.system('cls')



if __name__ == "__main__":
    main()