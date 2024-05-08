numbers = [5,2,3,7,3,9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
