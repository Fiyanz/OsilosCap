def type_int(var):
    return type(var) == int

def cek_input(Vdiv, div_s):
    if (type_int(Vdiv) and type_int(div_s)):
        return Vdiv, div_s
    
    else:
        print("Masukan angka please!!")