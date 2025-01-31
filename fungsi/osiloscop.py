
def vpp(VoltDiv: int | float, DivVertikal: int | float) -> float:
    """
    Menghitung tegangan Vpp dari osiloskop
    
    parameter:
    VoltDiv atau volt/div: sebuah volt setting dari osiloscop
    divVertikal: tinggi gelombang  
    """

    if isinstance((VoltDiv and DivVertikal), (int, float)):
        return VoltDiv * DivVertikal
    else:
        print("value harus integer atau float")
    
    
def frekuansi(DivHorisontal: int | float, TimeDiv: int | float) -> float:
    '''
    untuk mencati waktu pada osiloskop sebelum mencari frekuansi

    masukan argumen dengan satuan ms (millisecond)

    paramater:
    DivHorisontal: tinggi pankang gelombang
    TimeDiv atau time/div: negatur sekala waktu
    '''

    if isinstance((DivHorisontal and TimeDiv), (int | float)):
        time = DivHorisontal * TimeDiv
        return 1 / (time / 1000)
    else:
        print("value harus integer atau float")


def time(DivHorisontal: int | float, TimeDiv: int | float) -> float:
    '''
    untuk mencati waktu pada osiloskop sebelum mencari time 

    masukan argumen dengan satuan ms (millisecond)

    paramater:
    DivHorisontal: tinggi pankang gelombang
    TimeDiv atau time/div: negatur sekala waktu
    '''

    if isinstance((DivHorisontal and TimeDiv), (int | float)):
        return DivHorisontal * TimeDiv
    else:
        print("value harus integer atau float")


# if __name__ == "__main__":
#     print(frekuansi(3, "4"))
#     print(vpp(5,"4"))




