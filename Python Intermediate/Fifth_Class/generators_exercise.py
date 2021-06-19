def odd_generator(start, end):
    current = start
    while current <= end:
        if current % 2 != 0:
            yield current
            current += 1
        else:
            current += 1


for item in odd_generator(1, 20):
    print(item)
