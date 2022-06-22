while True:
    try:
        print("------------------------------------")
        print("----Welcome to the program----")
        print("----Find out the simple interest----")
        p = float(input("Principle Amount:\n"))
        r = float(input("Rate of Interest:\n"))
        t = float(input("Time span:\n"))

        SI = (p*r*t)/100
        print(f"The simple Interest is {SI}")
        
    except ValueError:
        print("KIndly write in numerical values...")