from fungsi.menu import menu
from fungsi.menu import clear

import fungsi.osiloscop as osiloscop

  

def handleVpp() -> None:
    
    loop = True
    while loop:
        menu("")
        try:
            VoltDiv = float(input("Masukan Volt/Div: "))
            DivVertikal = float(input("Masukan Div Vertikal: "))
            HasilVPP = osiloscop.vpp(VoltDiv=VoltDiv, DivVertikal=DivVertikal)
            print(f"VPP = {HasilVPP}")
        except:
            print("Masukan nilai dengan angka\n")
            print("Jika nilai desimal gunakan '.' (titik)")

        close = input("Kembali ke menu (y/n) ")
        if close == 'y':
            loop = False

def handleFrequensi() -> None:
    loop = True
    while loop:
        menu("Masukan Time/Div dengan satuan 's'")
        try:
            DivHorisintal = float(input("Masukan Div Horisontal: "))
            TimeDiv = float(input("Masukan Time Div: "))
            HasilFrekuensi = osiloscop.frekuansi(DivHorisontal= DivHorisintal, TimeDiv=TimeDiv)
            print(f"Frequensi = {HasilFrekuensi}")
        except:
            print("Masukan nilai dengan angka\n")
            print("Jika nilai desimal gunakan '.' (titik)")

        close = input("Kembali ke menu (y/n) ")
        if close == 'y':
            loop = False

def handleTime() -> None:
    loop = True
    while loop:
        menu("Masukan Time/Div dengan satuan 's'")
        try:
            DivHorisintal = float(input("Masukan Div Horisontal: "))
            TimeDiv = float(input("Masukan Time Div: "))
            HasilFrekuensi = osiloscop.frekuansi(DivHorisontal= DivHorisintal, TimeDiv=TimeDiv)
            print(f"Time = {HasilFrekuensi}")
        except:
            print("Masukan nilai dengan angka\n")
            print("Jika nilai desimal gunakan '.' (titik)")

        close = input("Kembali ke menu (y/n) ")
        if close == 'y':
            loop = False


"""main fungsion"""
def main():
    loop = True

    while loop:
        menu("1. Vpp",
             "2. Frekuensi",
             "3. Time",
             "('n') untuk keluar")
        
        input_user = input("Pilih Metode Perhitungan: ")

        if input_user == '1':
            handleVpp()

        elif input_user == '2':
            handleFrequensi()
        
        elif input_user == '3':
            handleTime()

        elif input_user == 'n':
            loop = False
            clear()
            



if __name__ == "__main__":
    main()