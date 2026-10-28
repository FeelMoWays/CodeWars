def bin_rota(arr):
    rota = []
    for i,row in enumerate(arr):
        if i % 2 == 0:
            rota.extend(row)
        else:
            rota.extend(row[::-1])
    return rota

print(bin_rota([ ["Stefan", "Raj",    "Marie"],
  ["Alexa",  "Amy",    "Edward"],
  ["Liz",    "Claire", "Juan"],
  ["Dee",    "Luke",   "Katie"] ]))
