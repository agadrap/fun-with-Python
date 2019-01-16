#MORTAGE CALCULATOR

print("This is a mortage calculator. Please provide following information.")
try:
    amount = int(input("How much money you want to loan: "))
    years = int(input("For how many years: "))
    percent = float(input("Interest rate [%]: "))
    constant = input("Do you want to pay constant instalments? Y/N")

    
    n = years*12

    if constant.upper()[0] == 'Y':
        #contant instalments
        q = 1 + ((percent/100)/12)
        instalment = amount * (q**n) * ((q-1)/(q**n-1))
        print(n)
        print(f"Your monthly instalment is equal {instalment}")

    else:

        instalments = []

        for item in range(1,n+1):
            instalment = amount/n * (1 + ((n - item + 1)*percent/100/12))

            instalments.append(instalment)

        print("Instalments:")

        for x in instalments:
            print(x)

except:
    print("\nYou have entered information that I cannot process. Please put \na whole number for money/years \na decimal number for interest rate [like 3.5 or 11]")
