import os

def menu():
    os.system('cls')
    print("="*50)
    print("Tools Menghitung Osiloskop \n"
          "Fitur\n"
          "- Vdd\n"
          "- frekuensi\n"
          "- output ideal")
    print("="*50)

def menu_luas_pp():
    # os.system('cls')
    print("="*50)
    print("Menghitung Luas Persegi Panjang \n")
    print("Pertama masukan nilai panjang\n"
          "kemudian masukan nilai lebar\n")
    print("Untuk keluar masukan input string")
    print("="*50)

def luas_persegi_panjang():
    menu_luas_pp()
    
    panjang = int(input("Masukan panjang: "))
    lebar = int(input("Masukan lebar: "))
    luas = panjang * lebar
    print(f"Luas Persegi panjang {luas}")

def looping_funsion():
    loop = True
    while loop:
        answer = input("lanjutkan untuk perhitungan ini? ")
        if answer == 'y' or 'Y':  
            luas_persegi_panjang()
        else:
            loop = False
        

def main():
    loop = True

    menu()
    while loop:
        data_input = input("Pilih Metode Perhitungan: ")
        data_integer = int(data_input)
        if data_integer == 1:
            looping_funsion()
            os.system('cls')

        if data_input == 'x':
            loop = False
            os.system('cls')

        



if __name__ == "__main__":
    main()