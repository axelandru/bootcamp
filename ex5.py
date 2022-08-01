list = [1,3,6,9,81,99,100]
print(list)
condition = True
for element in list:
    if element % 9 == 0 and element != 81:
        print(element)
    elif element == 81:
        continue
    if list[len(list) - 1] >= 100:
        break
    if element >= 100:
        condition = False
    if condition:
        print("All good")