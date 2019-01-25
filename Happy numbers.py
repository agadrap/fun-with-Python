happy_number_input = input("Please provide a number greater than 0:   ")

if int(happy_number_input) > 0 :
    happy_number = happy_number_input

    while True:
        num = [number for number in happy_number]
        num = list(map(int,num))
        num = [i**2 for i in num]
        num = sum(num)

        happy = num
        if happy == 1:
            print(f"{happy_number_input} IS A HAPPY NUMBER!")
            break
        else:
            continue
else:
    print("Wrong input.")
