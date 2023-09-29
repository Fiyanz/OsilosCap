from all_fungsi.menu import menu
from all_fungsi.alfa import alfa


def vdd():
    # DivVertikal = tinggi rekuanesi atau tinggi glelombang per div
    # VoltDiv = besar volt per div di osiloscop
    while True:
        # next mengatasi clear sesudah looping 
        try:
            VoltDiv = float(input("Masukan Volt/Div: "))
            DivVertikal = float(input("Masukan DivVertikal: "))
            finall_vpp = VoltDiv * DivVertikal
            print(f"Hasil Volt Peak to Peak 'VPP': {finall_vpp}")
            # print(VoltDiv, DivVertikal)
        except ValueError:
            return False


"""fungsi osiloscop"""
def osiloscop():
    loop = True
    while loop:
        menu("",
            "1. VDD",
            "2. Frekuansi",
            "3. ",)
        
        input_osiloscop = input("Pilih Metode Perhitungan: ")
        
        match input_osiloscop:
            case '1': print(vdd())
            case '2': print('hi')
            case 'x': return False


        # if input_osiloscop == '1':
        #     vdd()

        # elif input_osiloscop == '2':
        #     print('a')

        # elif input_osiloscop == 'x' or 'X' and not alfa():
        #     # print(type(answer))
        #     loop = False

        # elif alfa():
        #     loop = False