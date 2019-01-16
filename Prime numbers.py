n = int(input("Please enter a number: "))
prime = [1, 2, 3, 5, 7]
for i in range(2,n):
    if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0:
        continue
    else:
        prime.append(i)

print(prime)
