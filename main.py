import lotteri
import os

lotteriet = lotteri.Lotteri()
looping = True

while looping:
    os.system('cls' if os.name == 'nt' else 'clear')
    antal_lotter = input("\n\t\tHur många lotter vill du ha? Max 3st! ")

    try:
        int_antal_lotter = int(antal_lotter)
        
        if int_antal_lotter <= 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\t\tGrattis du vann det här! ")
            i = 0
            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                print("\t\t" + vinst)
                i += 1
        else:
            print("\n\t\tDu har valt för många lotter!")
    except ValueError:
        print("\n\t\tEndast siffror tillåtet!")

    print("--------------------------------------------------------------------------------")
    spela_igen = input("\n\t\tVill du spela igen? j/n: ")

    if spela_igen.lower() == "n":
        looping = False
