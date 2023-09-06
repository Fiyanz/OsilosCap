from menu.menu import menu
from menu.menu import alfa


"""fungsi osiloscop"""
def osiloscop():
    loop = True
    while loop:
        answer = input("lanjut perhitungan vdd? ")
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
                luas = panjang * lebar
                print(f"Luas Persegi panjang {luas}")
                
            except ValueError:
                print("Masukan input Angka please!!")

        elif answer == 'x' or 'X' and not alfa():
            # print(type(answer))
            loop = False

        elif alfa():
            print("Masukan huruf sesuai perintah!!")