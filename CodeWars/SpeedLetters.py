import string
def speedify(st): 
    empty_string = ""
    for i in st:
        empty_string += string.ascii_uppercase[string.ascii_uppercase.index(i) + string.ascii_uppercase(i)]
    return empty_string