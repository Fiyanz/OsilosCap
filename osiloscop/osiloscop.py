from all_fungsi.menu import menu
from all_fungsi.alfa import alfa
from all_fungsi.cek_int_type import cek_input


def vdd():
    pass

"""fungsi osiloscop"""
def osiloscop():
    loop = True
    while loop:
        answer = input("lanjut perhitungan vdd? ")
        if answer == 'y' or 'Y' and not alfa():
            # print(type(answer))
            # loop = False  
            menu("", 
                 "Gunakan perintah 'x' untuk keluar\nGunakan 'y' untuk melanjutkan",
                 "'DIV/V' adalah tinggi gelombang dari atas ke bawah atau Vertikal",
                 "'DIV/v' adalah ")
            
            try:
                Vdiv = int(input("Masukan DIV/V: "))
                div_s = int(input("Masukan DIV/v: "))
                
                Vdiv, div_s = cek_input(Vdiv, div_s)
                value_vpp = Vdiv * div_s
                print(f"Hasil Volt Peak to Peak 'VPP': {value_vpp}")
                
            except ValueError:
                print("Masukan input Angka please!!")

        elif answer == 'x' or 'X' and not alfa():
            # print(type(answer))
            loop = False

        elif alfa():
            print("Masukan huruf sesuai perintah!!")