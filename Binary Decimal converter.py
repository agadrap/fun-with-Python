# This is a converter that translates numbers from
#Binary to decimal &
# Decimal to binary

print("This is a binary/decimal converter")
print("What you want to convert:")
print("0: Decimal to Binary")
print("1: Binary to Decimal \n")

try:

    while True:
        conv = int(input("Pick 0 or 1: "))

        while conv == 0 or conv == 1:

            if conv == 0:
                decimal = int(input("Give me a decimal: "))
                binary = []

                while decimal != 1 and decimal > 0:
                    bina = decimal%2
                    binary.append(bina)
                    if bina == 0:
                        decimal = decimal/2
                    elif bina ==1:
                        decimal = (decimal-1)/2


                binary.append(1)

                result = binary[::-1]
                print(f"Result: {result}")
                result = []



            elif conv == 1:
                binary = input("Give me a binary:")
                binary_list = list(binary)
                length = len(binary)
                #binary.split()
                print(binary_list)
                map(int,binary_list)
                print(binary_list)

                for item in binary_list:
                    if item == '0':
                        continue
                    elif item == '1':
                        component = 2**(length-int(item))
                        print(component)
                        result += component


                print(f"Result: {result}")
                result = 0
        else:
            break
except:
    print("Wrong input")
