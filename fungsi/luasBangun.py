

def perJang(panjang: int | float, lebar: int | float)-> float:
    """
    fungsi luas persegi panjang yang akan mengambalikan nilai float
    
    parameter:
    panjang: nilai panjang
    lebar: nilai lebar
    """    
    return panjang * lebar

def persegi(sisi: int | float)-> float:
    """
    fungsi luas persegi yang akan mengambalikan nilai float
    
    parameter:
    sisi: nilai sisi dari persegi
    """    
    return sisi * sisi

def luasSegitiga(a: float | int, t: float | int) -> float:
    """
    fungsi untuk menghitung luas segitiga

    parameter:
    a: alas segitiga
    t: tinggi segitiga
    """
    return 0.5 * a * t


print(luasSegitiga(8, 12))


