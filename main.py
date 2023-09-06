import os

low_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z']
big_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Z']
all_alfa = low_alfa + big_alfa



"""fungsi menu"""
def menu(title = "", title_sec = "", list_1 = "", list_2 = "", list_3 = "", list_4 = ""):
    os.system('cls')
    print('='* 50)
    print(title)
    print('='* 50)
    print(f'{title_sec}\n'
          f'{list_1}\n'
          f'{list_2}\n'
          f'{list_3}\n'
          f'{list_4}')

def menu_luas_pp():
    # os.system('cls')
    print("="*50)
    print("Menghitung Luas Persegi Panjang \n")
    print("Pertama masukan nilai panjang\n"
          "kemudian masukan nilai lebar\n")
    print("Untuk keluar masukan input string")
    print("="*50)

"""fungsi persegi panjang"""
def luas_persegi_panjang():
    loop = True
    while loop:
        answer = input("lanjutkan untuk perhitungan ini? ")
        if answer == 'y' or 'Y' and not all_alfa:
            # print(type(answer))
            # loop = False  
            menu("LUAS PERSEGI", 
                 "Gunakan perintah 'x' untuk keluar\nGunakan 'y' untuk melanjutkan",
                 "Masukan Panjang persegi panjang",
                 "Masukan Lebar Persegi panjang")
            
            try:
                panjang = int(input("Masukan panjang: "))
                luas = panjang * lebar
                lebar = int(input("Masukan lebar: "))
                print(f"Luas Persegi panjang {luas}")
                
            except ValueError:
                print("Masukan input Angka please!!")

        elif answer == 'x' or 'X' and not all_alfa:
            # print(type(answer))
            loop = False

        elif all_alfa:
            print("Masukan huruf sesuai perintah!!")
    
    
        
"""main loop"""
def main():
    loop = True

    while loop:
        menu("tools simple kalkulator",
            "",
            "osiloscop",
            "luas persegi panjang",
            "GLBB",)
        data_input = input("Pilih Metode Perhitungan: ")
        data_integer = int(data_input)
        if data_integer == 1:
            luas_persegi_panjang()
            os.system('cls')

        if data_input == 'x':
            loop = False
            os.system('cls')

        



if __name__ == "__main__":
    main()