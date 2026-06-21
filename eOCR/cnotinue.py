total = 0

for number in range(0, 10):
    print(list(range(0,10)))
    if number < 0:
        continue
    total += number

print(total)