print()
print("\t CSYSTEM (Consigned System).")
print("\t Developed bt Victor Mello, 2022.")
print()
nam = input("\t What's yout name? ")
print()
print(f"\t Welcome, {nam}!")
print()

while True: 
    mar = float(input("\t MARGIN VALUE: "))
    coef = 0.02707
    res = mar / coef
    print()

    conv = f"\t MAX VALUE TO BE LIBERED: R$ {res:.2f}"

    print(conv)
        
    print()
    print()
    

