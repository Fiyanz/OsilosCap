from all_fungsi.menu import menu
from all_fungsi.alfa import alfa
from all_fungsi.cek_int_type import cek_input


def vdd():
    Vdiv = int(input("Masukan DIV/V: "))
    div_s = int(input("Masukan DIV/v: "))
    print(Vdiv, div_s)

    # entah kenapa code dibawah tidak di exsekusi 
    # masih mencari dimana kesalahannya
    Vdiv, div_s = cek_input(Vdiv, div_s)
    value_vpp = Vdiv * div_s
    return value_vpp
    # print(f"Hasil Volt Peak to Peak 'VPP': {value_vpp}")

"""fungsi osiloscop"""
def osiloscop():
    loop = True
    while loop:
        menu("",
            "1. VDD",
            "2. Frekuansi",
            "3. ",)
        
        input_osiloscop = input("Pilih Metode Perhitungan: ")
        
        if input_osiloscop == '1':
            vdd()

        elif input_osiloscop == '2':
            print('hai')
            


        # answer = input("lanjut perhitungan vdd? ")
        # if answer == 'y' or 'Y' and not alfa():
        #     # print(type(answer))
        #     # loop = False  
        #     menu("", 
        #          "Gunakan perintah 'x' untuk keluar\nGunakan 'y' untuk melanjutkan",
        #          "'DIV/V' adalah tinggi gelombang dari atas ke bawah atau Vertikal",
        #          "'DIV/v' adalah ")
            

        # elif answer == 'x' or 'X' and not alfa():
        #     # print(type(answer))
        #     loop = False

        # elif alfa():
        #     print("Masukan huruf sesuai perintah!!")