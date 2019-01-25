#Credit card validator
def luhn_algorithm(card_number):
    card_number = [int(i) for i in str(card_number)]
    reverse_card = card_number[::-1]

    luhn_1 = []

    luhn = [reverse_card[index] for index in range(1, len(reverse_card), 2)]
    luhn_2 = [reverse_card[index] for index in range(0, len(reverse_card), 2)]

    for item in luhn:
        item = item*2
        if item > 9:
            item = item-9
        else:
            item = item
        luhn_1.append(item)

    suma_1 = sum(luhn_1)
    suma_2 = sum(luhn_2)
    result = suma_1 + suma_2

    if result % 10 == 0:
        output = "Card is valid"
    else:
        output = "Card not valid"

    return output

def card_origin(card_number):
    amex_inn =('34', '37')
    china_tunion = ('31')
    china_unionpay = ('62')
    din_club_inter = ('36', '300', '301', '302', '303', '304', '305', '3095', '38', '39')
    din_club_us_ca = ('6011', '64', '65')
    maestro = ('60', '6521', '6522')
    mir = ('2200', '2201', '2202', '2203', '2204')
    master_card = ('51', '52', '53', '54', '55')

    card_number = [str(i) for i in str(card_number)]

    if len(card_number) < 12 or len(card_number) > 19:
        print("Incorrect input!")

    elif len(card_number) == 12 or len(card_number) == 13:
        #MAESTRO
        if (card_number[0] == '6' and card_number[1] == '0'):
            print("Maestro")
        else:
            card_number = card_number[0:4]
            check_card = join(card_number)
            if check_card in maestro:
                print("Maestro")
            else:
                print("Unidentifined")

    elif len(card_number) == 14:
        #maestro
        #diners club international
        if (card_number[0] == '6' and card_number[1] == '0'):
            print("Maestro")
        elif (card_number[0] == '3' and card_number[1] == '6'):
            print("Diners Club International")
        else:
            card_number = card_number[0:4]
            check_card = "".join(card_number)
            if check_card in maestro:
                print("Maestro")
            else:
                print("Unidentifined")

    elif len(card_number) == 15:
        #AMEX
        #diners club international
        #maestro
        #uatp check for [0] = 1
        if (card_number[0] == '6' and card_number[1] == '0'):
            print("Maestro")
        elif (card_number[0] == '3' and card_number[1] == '6'):
            print("Diners Club International")
        elif (card_number[0] == '3' and card_number[1] == '7') or (card_number[0] == '3' and card_number[1] == '4'):
            print("American Express")
        elif card_number[0] == '1':
            print("UATP")
        else:
            card_number4 = card_number[0:4]
            check4 = "".join(card_number4)
            if check4 in maestro:
                print("Maestro")
            else:
                print("Unidentifined")

    elif len(card_number) ==16:
        #verve 506099 - 506198   &   650002 - 650027
        #unionpay check in range 810000 - 817199
        #visa check for [0] = 4
        #troy check only 979200 - 979289
        #master card - check tuple & 222100 - 272099
        #mir
        #maestro
        #diners club international
        #diners club usa canada
        #china unionPay
        if card_number[0] == '4':
            print("VISA")
        else:
            card_number2 = card_number[0:2]
            card_number3 = card_number[0:3]
            card_number4 = card_number[0:4]
            card_number6 = card_number[0:6]
            check4 = "".join(card_number4)
            check2 = "".join(card_number2)
            check3 = "".join(card_number3)
            check6 = "".join(card_number6)

            if check2 in china_unionpay:
                print("China Union Pay")
            elif check2 in din_club_inter or check3 in din_club_inter or check4 in din_club_inter:
                print("Diners Club International")
            elif check2 in din_club_us_ca or check4 in din_club_us_ca:
                print("Diners Club USA & Canada")
            elif check2 in maestro or check4 in maestro:
                print("Maestro")
            elif int(check4) in range(2200,2205):
                print("MIR")
            elif check2 in master_card or int(check6) in range(222100,272100):
                print("Master Card")
            elif int(check6) in range(979200,979290):
                print("Troy")
            elif int(check6) in range(810000,817200):
                print("Union Pay")
            elif int(check6) in range(506099,506199) or int(check6) in range(650002,650028):
                print("Verve")
            else:
                print("Unidentifined")

    elif len(card_number) ==17 or len(card_number) ==18:
        #china unionPay
        #diners club international
        #diners club usa canada
        #maestro
        card_number2 = card_number[0:2]
        card_number3 = card_number[0:3]
        card_number4 = card_number[0:4]
        card_number6 = card_number[0:6]
        check4 = "".join(card_number4)
        check2 = "".join(card_number2)
        check3 = "".join(card_number3)
        check6 = "".join(card_number6)

        if check2 in china_unionpay:
            print("China Union Pay")
        elif check2 in din_club_inter or check3 in din_club_inter or check4 in din_club_inter:
            print("Diners Club International")
        elif check2 in din_club_us_ca or check4 in din_club_us_ca:
            print("Diners Club USA & Canada")
        elif check2 in maestro or check4 in maestro:
            print("Maestro")
        else:
            print("Unidentifined")

    elif len(card_number) == 19:
        #china t-union
        #china unionPay
        #diners club international
        #diners club usa canada
        #maestro
        #verve
        card_number2 = card_number[0:2]
        card_number3 = card_number[0:3]
        card_number4 = card_number[0:4]
        card_number6 = card_number[0:6]
        check4 = "".join(card_number4)
        check2 = "".join(card_number2)
        check3 = "".join(card_number3)
        check6 = "".join(card_number6)

        if check2 in china_unionpay:
            print("China Union Pay")
        elif check2 in din_club_inter or check3 in din_club_inter or check4 in din_club_inter:
            print("Diners Club International")
        elif check2 in din_club_us_ca or check4 in din_club_us_ca:
            print("Diners Club USA & Canada")
        elif check2 in maestro or check4 in maestro:
            print("Maestro")
        elif int(check6) in range(506099,506199) or int(check6) in range(650002,650028):
            print("Verve")
        else:
            print("Unidentifined")

# MAIN
card = input("Insert Card number: ")
print(luhn_algorithm(card))
card_origin(card)
