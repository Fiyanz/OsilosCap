from fungsi.menu import menu
from fungsi.menu import clear

import fungsi.osiloscop as osiloscop

  

def handleVpp():
    # next handle eror input waktu memasukan selain float dan int
    # juga mungkin buat fungsi baru untuk mencari waktu agar lebih spesifik
    loop = True
    while loop:
        menu("")
        VoltDiv = float(input("Masukan Volt/Div: "))
        DivVertikal = float(input("Masukan Div Vertikal: "))
        HasilVPP = osiloscop.vpp(VoltDiv=VoltDiv, DivVertikal=DivVertikal)
        print(f"Hasil VPP dari {VoltDiv} dan {DivVertikal} = {HasilVPP}")

        close = input("Kembali ke menu (y/n) ")
        if close == 'y':
            loop = False

def handleFrequensi() -> None:
    loop = True
    while loop:
        menu("Masukan Time/Div dengan satuan 's'")
        DivHorisintal = float(input("Masukan Div Horisontal: "))
        TimeDiv = float(input("Masukan Time Div: "))
        HasilFrekuensi = osiloscop.frekuansi(DivHorisontal= DivHorisintal, TimeDiv=TimeDiv)
        print(f"Frequensi dari {DivHorisintal} dan {TimeDiv} = {HasilFrekuensi}")

        close = input("Kembali ke menu (y/n) ")
        if close == 'y':
            loop = False


"""main fungsion"""
def main():
    loop = True

    while loop:
        menu("1. Osiloscop",
             "2. luas persegi panjang",
             "n. untuk keluar")
        
        input_user = input("Pilih Metode Perhitungan: ")

        if input_user == '1':
            handleVpp()

        elif input_user == '2':
            handleFrequensi()

        elif input_user == 'n':
            loop = False
            clear()
            



if __name__ == "__main__":
    main()