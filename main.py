from fungsi.menu import menu

import fungsi.osiloscop as osiloscop
import os
  
        
"""main fungsion"""
def main():
    loop = True

    while loop:
        menu("1. Osiloscop",
             "2. luas persegi panjang")
        
        input_user = input("Pilih Metode Perhitungan: ")

        if input_user == '1':
            VoltDiv = float(input("Masukan Volt/Div: "))
            DivVertikal = float(input("Masukan Div Vertikal: "))
            HasilVPP = osiloscop.vpp(VoltDiv = VoltDiv, DivVertikal=DivVertikal)
            print(HasilVPP)

        elif input_user == '2':
            DivHorisintal = float(input("Masukan Div Horisontal: "))
            TimeDiv = float(input("Masukan Time Div: "))
            HasilFrekuensi = osiloscop.frekuansi(DivHorisontal= DivHorisintal, TimeDiv=TimeDiv)
            print(HasilFrekuensi)

        elif input_user == 'x':
            loop = False



if __name__ == "__main__":
    main()