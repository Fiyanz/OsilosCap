from all_fungsi.menu import menu
from all_fungsi.alfa import alfa
from all_fungsi.cek_int_type import cek_input

"""fungsi persegi panjang"""
def luas_persegi_panjang():
    loop = True
    while loop:
        answer = input("lanjutkan untuk perhitungan ini? ")
        if answer == 'y' or 'Y' and not alfa():
            # print(type(answer))
            # loop = False  
            menu("LUAS PERSEGI", 
                 "Gunakan perintah 'x' untuk keluar\nGunakan 'y' untuk melanjutkan",
                 "Masukan Panjang persegi panjang",
                 "Masukan Lebar Persegi panjang")
            
            try:
                panjang = int(input("Masukan panjang: "))
                lebar = int(input("Masukan lebar: "))
                panjang, lebar = cek_input(panjang, lebar)
                luas = panjang * lebar
                print(f"Luas Persegi panjang {luas}")
                
            except ValueError:
                print("Masukan input Angka please!!")

        elif answer == 'x' or 'X' and not alfa():
            # print(type(answer))
            loop = False

        elif alfa():
            print("Masukan huruf sesuai perintah!!")