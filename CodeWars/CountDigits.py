def nb_dig(n, d):
    squared_list = [i**2 for i in range(n + 1)]
    return sum(str(num).count(str(d)) for num in squared_list)
print(nb_dig(5750, 0))
