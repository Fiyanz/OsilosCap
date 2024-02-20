from fungsi.menu import menu
from fungsi.menu import clear

import fungsi.osiloscop as osiloscop
import os
  

def handleVpp():
    while True:
        VoltDiv = float(input("Masukan Volt/Div: "))
        DivVertikal = float(input("Masukan Div Vertikal: "))
        HasilVPP = osiloscop.vpp(VoltDiv = VoltDiv, DivVertikal=DivVertikal)
        print(f"Hasil VPP {HasilVPP}")

"""main fungsion"""
def main():
    loop = True
    menu("1. Osiloscop",
            "2. luas persegi panjang")

    while loop:
        
        input_user = input("Pilih Metode Perhitungan: ")

        if input_user == '1':
            handleVpp()
            # VoltDiv = float(input("Masukan Volt/Div: "))
            # DivVertikal = float(input("Masukan Div Vertikal: "))
            # HasilVPP = osiloscop.vpp(VoltDiv = VoltDiv, DivVertikal=DivVertikal)
            # print(HasilVPP)

        elif input_user == '2':
            DivHorisintal = float(input("Masukan Div Horisontal: "))
            TimeDiv = float(input("Masukan Time Div: "))
            HasilFrekuensi = osiloscop.frekuansi(DivHorisontal= DivHorisintal, TimeDiv=TimeDiv)
            print(HasilFrekuensi)

        elif input_user == 'x':
            loop = False
            clear()
            



if __name__ == "__main__":
    main()