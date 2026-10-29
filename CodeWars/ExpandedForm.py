def expanded_form(num):
    total = []
    for i,v in enumerate(str(num)[::-1]):
        value = int(v) * (10 ** i)
        if value:
            total.append(str(value))
    return " + ".join(total[::-1])


print(expanded_form(123))
