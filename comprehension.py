# list comprehension

#double prize money weekend bonanza
prizes = [5, 10, 50, 100, 1000]

#normal way
dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize * 2)
print(dbl_prizes)

#list comprehension way
dbl_prizes = [ prize * 2 for prize in prizes ]
print(dbl_prizes)