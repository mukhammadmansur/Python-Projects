firstNum = int(input("Birinchi sonni kirgazing!: "))
mathAc = input("Amalni kirgazing!: ")
secondNum = int(input("Ikkinchi sonni kirgazing!: "))

if ( mathAc == "+" ):
    print(firstNum + secondNum);

elif ( mathAc == "-" ):
    print(firstNum - secondNum);

elif ( mathAc == "*" ):
    print(firstNum * secondNum);

elif ( mathAc == "/" ):
    print(firstNum / secondNum);

elif (mathAc == "**", "darajaga ko'tar"):
    print(firstNum ** secondNum);

else : print('Amallarda xatolik bor')