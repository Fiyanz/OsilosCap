import fungsi.menu as menu
import fungsi.osiloscop as osiloscop


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

        

        # # exit_input = input("ingin keluar? ")
        # elif input_user == 'y'or 'Y':
        #     loop = False
        #     os.system(['clear', 'cls'][os.name == 'nt'])

        # elif input_user  == 'x'or 'X' and not alfa():
        #     main()



if __name__ == "__main__":
    main()