def prime_to_infinity():
    x = 2
    while True:
        yield x
        x += 1

print("This will show you prime numbers in order.")

while True:
    for i in prime_to_infinity():
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i)
            ask = input("Next? Y/N")
            if ask.upper()[0] == 'Y':
                continue
            else:
                break

        elif i % 2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0:
            continue
        else:
            print(i)
            ask = input("Next? Y/N")
            if ask.upper()[0] == 'Y':
                continue
            else:
                break
