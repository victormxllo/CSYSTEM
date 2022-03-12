
print()
print("\t CSYSTEM (Consigned System).")
print("\t Developed bt Victor Mello, 2022.")
print()
nam = input("\t What's your name? ")
print()
print(f"\t Welcome, {nam}!")
print()

while True: 
    ques = input("\t \t     SIMULATE: \n \t[1] MARGIN   [2] CARD   [3] EXIT: ")
    print()
    
    if ques == "1": 
        mar = float(input("\t MARGIN VALUE: "))
        coef = 0.02707
        res = mar * coef
        print()

        convmarg = f"\t MAX VALUE TO BE LIBERED: R$ {res:.3f},00."

        print(convmarg)
            
        print()
        print()
        

    elif ques == "2":
        cmar = float(input("\t CARD MARGIN VALUE: "))
        lim = cmar * 32
        saq = (lim * 70) / 100 
        print()

        convcard = f"\t MAX CARD VALUE TO BE LIBERED: R$ {saq}0. \n \t LIMIT OF THE CARD: {lim}0."

        print(convcard)
            
        print()
        print()

    else:
        ques == "3"
        break
