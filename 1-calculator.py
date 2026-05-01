firstNum = int(input("Birinchi sonni kirgazing!: "))
mathAc = input("Amalni kirgazing!: ")
secondNum = int(input("Ikkinchi sonni kirgazing!: "))

if ( mathAc == "+" ):
    
    print(f"{firstNum} + {secondNum} = {firstNum + secondNum}");

elif ( mathAc == "-" ):
    print(f"{firstNum} - {secondNum} = {firstNum - secondNum}");

elif ( mathAc == "*" ):
    print(f"{firstNum} * {secondNum} = {firstNum * secondNum}");

elif ( mathAc == "/" ):
    if secondNum != 0:
        print(f"{firstNum} / {secondNum} = {int(firstNum / secondNum)}");
    else :
        print("0 ga bo'lib bo'lmaydi");

elif (mathAc == "**", "darajaga ko'tar"):
    print(f"{firstNum} ** {secondNum} = {firstNum ** secondNum}");

else : print('Amallarda xatolik bor')
