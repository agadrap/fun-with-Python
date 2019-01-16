n = int(input("Please enter a number: "))

def genfibo(n):

# GENERATE FIBONACCI NUMBER UP TO n
    f1 = 1
    f2 = 1

    for i in range(n):
        yield f1
        f1, f2 = f2, f1+f2

for num in genfibo(n):
    print(num)
