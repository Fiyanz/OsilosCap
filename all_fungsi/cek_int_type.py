# from all_fungsi.alfa import alfa
def type_int(var):
    return type(var) == int

def cek_input(user_one, user_second):
    if (type_int(user_one) and type_int(user_second)):
        return user_one, user_second
    
    else:
        print("Masukan angka please!!")
        return False
    


