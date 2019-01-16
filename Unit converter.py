# This is a unit converter for:

# Temp:     Celsius     /   Kelvin  /   Farenheit
# Currency: USD         /   PLN     /   EUR     /   BTC
# Mass:     KG          /   Pounds
# Length:   miles       /   meters  /   feet    /   flight level
# Speed:    m/s         /   km/h    /   mph     /   knots       / Ma

def temperature_conv(unit,number):
    if unit.upper()[0] == 'C':
        celsius = number
        kelvin = 273.15 + number
        farenheit = 32 + (9/5)*number
    elif unit.upper()[0] == 'K':
        kelvin = number
        celsius = number - 273.15
        farenheit = 32 + (9/5)*celsius
    else unit.upper()[0] == 'F':
        farenheit = number
        celsius = (5/9) * (number - 32)
        kelvin = 273.15 + celsius

    return [celsius, kelvin, farenheit]

def currency_conv (currency,amount):
    print("\nThe currency converter uses the prices for 15th Jan 2019.\n")
    currencies = {'usd_pln':3.7690, 'eur_pln':4.2953, 'btc_pln':14047.42, 'eur_usd':1.1395, 'btc_usd':3725.4, 'btc_eur':3263.0}

    if currency == 'U':
        pln = amount * currencies['usd_pln']
        usd = amount
        eur = amount * 1/currencies['eur_usd']
        btc = amount * 1/currencies['btc_usd']

    elif currency == 'P':
        pln = amount
        usd = amount * 1/currencies['usd_pln']
        eur = amount * 1/currencies['eur_pln']
        btc = amount * 1/currencies['btc_pln']

    elif currency == 'E':
        pln = amount * currencies['eur_pln']
        usd = amount * currencies['eur_usd']
        eur = amount
        btc = amount * 1/currencies['btc_eur']

    elif currency == 'B':
        pln = amount * currencies['btc_pln']
        usd = amount * currencies['btc_usd']
        eur = amount * currencies['btc_eur']
        btc = amount

    return [pln, usd, eur, btc]

def mass_conv (unit,number):
    if unit == 'K':
        kilo = number
        libra = number*2.20462
    elif unit == 'L':
        libra = number
        kilo = number*0.4535923

    return [kilo, libra]

def length_conv (unit,number):
    if unit == 'FL':
        if number < 1:
            FL = 'Terrain! Terrain!'
        elif number >=1 and number <= 510:
            FL = number
        else:
            FL = 'You are in Space!'

        feet = number * 100
        miles = feet * 0.0001893939
        meters = feet * 0.3048
    else:
        if unit == 'mile':
            miles = number
            meters = number * 1609.344
            feet = number * 5280

        elif unit == 'meter':
            miles = number * 0.000621371192
            meters = number
            feet = number * 3.2808399

        elif unit == 'feet':
            miles = number * 0.0001893939
            meters = number * 0.3048
            feet = number

        if feet < 1000:
                FL = 'Terrain! Terrain!'
        elif feet == 1000:
            FL = '010'
        elif feet > 1000 and feet < 10000:
            if feet % 1000 == 0:
                FL = int(feet / 100)
                FL = f"0{FL}"
            else:
                feet = feet - (feet % 1000)
                FL = int(feet / 100)
                FL = f"0{FL}"
        elif feet > 10000 and feet < 51000:
            if feet % 1000 == 0:
                FL = (feet / 100)
            else:
                feet = feet - (feet % 1000)
                FL = int(feet / 100)

        else:
            FL = 'You are in Space!'

    return [miles, meters, feet, FL]

def speed_conv (unit,number):
    if unit == 'm/s':
        m_s = number
        km_h = number * 3.6
        mph = number * 2.2369
        knots = number * 1.9438
        mach = number/340.3
    elif unit == 'km/h':
        m_s = number/3.6
        km_h = number
        mph = number/1.61
        knots = number/1.852
        mach = m_s/340.3
    elif unit == 'mph':
        m_s = number * 0.447031111
        km_h = number * 1.61
        mph = number
        knots = number/1.15078
        mach = m_s/340.3
    elif unit == 'knots':
        m_s = number*0.51444
        km_h = number*1.852
        mph = number*1.15078
        knots = number
        mach = m_s/340.3
    elif unit == 'Ma':
        m_s = number * 340.3
        km_h = number * 1225
        mph = number * 761.21
        knots = number * 661.47084
        mach = number

    return [m_s, km_h, mph, knots, mach, "Ma for speed of sound equal 340 m/s - air temp 15 Ceslsius."]

# MAIN PROGRAM
print("---C O N V E R S I O N    C A L C U L A T O R---")
while True:
    execute = input("Fancy for conversion? Y/N")
    if execute.upper()[0] == 'Y':
        change_conv = True
    else:
        break

    print("Temperature:     T")
    print("Currency:        $")
    print("Mass:            M")
    print("Length:          S")
    print("Speed:           V")
    conv = input("\nWhat do you want to convert: ")

    while change_conv == True:
        if conv.upper()[0] == "T":
            unit = input("Please pass in the unit. Pick from:\nC    K   F")
            number = int(input("Please pass in the number:"))
            unit = unit.upper()[0]

            result = temperature_conv(unit,number)
            print(f"\nTemperature:\n {result[0]} Celsius\n {result[1]} Kelvin\n {result[2]} Farenheit")

            again = input("again? Y/N")
            if again.upper()[0] == 'Y':
                change_conv = True
            else:
                change_conv = False

        elif conv.upper()[0] == "$":
            currency = input("Please pass in the unit. Pick from:\nPLN    USD   EUR     BTC")
            number = int(input("Please pass in the number:"))
            currency = currency.upper()[0]

            result = currency_conv(currency,number)
            print(f"\nCurrency:\n {result[0]} PLN\n {result[1]} USD\n {result[2]} EUR\n {result[3]} BTC")

            again = input("again? Y/N")
            if again.upper()[0] == 'Y':
                change_conv = True
            else:
                change_conv = False

        elif conv.upper()[0] == "M":
            unit = input("Please pass in the unit. Pick from:\nKG    LBS")
            number = int(input("Please pass in the number:"))
            unit = unit.upper()[0]

            result = mass_conv(unit,number)
            print(f"\nMass:\n {result[0]} kg\n {result[1]} lbs\n")

            again = input("again? Y/N")
            if again.upper()[0] == 'Y':
                change_conv = True
            else:
                change_conv = False

        elif conv.upper()[0] == "S":
            unit = input("Please pass in the unit. Pick from:\nmile    meter   feet     FL")
            number = int(input("Please pass in the number:"))

            result = length_conv(unit,number)
            print(f"\nLength:\n {result[0]} miles\n {result[1]} meters\n {result[2]} feet\n {result[3]} FL\n")

            again = input("again? Y/N")
            if again.upper()[0] == 'Y':
                change_conv = True
            else:
                change_conv = False

        elif conv.upper()[0] == "V":
            unit = input("Please pass in the unit. Pick from:\nm/s    km/h   mph     knots      Ma")
            number = int(input("Please pass in the number:"))

            result = speed_conv(unit,number)
            print(f"\nVelocity:\n {result[0]} m/s\n {result[1]} km/h\n {result[2]} mph\n {result[3]} knots\n {result[4]} Ma\n {result[5]}")

            again = input("again? Y/N")
            if again.upper()[0] == 'Y':
                change_conv = True
            else:
                change_conv = False
