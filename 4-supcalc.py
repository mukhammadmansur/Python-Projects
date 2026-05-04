print("""    Qanday hisobni amalga oshirmoqchisiz?
      
    calculator: 1;
    darajaga oshirish: 2;
    BMI: 3;
      """)
      
calcType = input("Tanlang: ")

if calcType == "1":
    print("""
    calculator ishlamoqda...""")

    firstNum = int(input("Birinchi sonni kirgazing!: "))
    mathAc = input("Amalni kirgazing!(+, -, *, /, **): ")
    secondNum = int(input("Ikkinchi sonni kirgazing!: "))

    if mathAc == "+" :

        print(f"{firstNum} + {secondNum} = {firstNum + secondNum}");

    elif mathAc == "-":
        print(f"{firstNum} - {secondNum} = {firstNum - secondNum}");

    elif mathAc == "*":
        print(f"{firstNum} * {secondNum} = {firstNum * secondNum}");

    elif mathAc == "/" :
        if secondNum != 0:
            print(f"{firstNum} / {secondNum} = {int(firstNum / secondNum)}");
        else :
            print("0 ga bo'lib bo'lmaydi");

    elif mathAc == "**" or "darajaga ko'tar":
        print(f"{firstNum} ** {secondNum} = {firstNum ** secondNum}");

    else : print('Amallarda xatolik bor')

elif calcType == "2":

    print("""
    Darajaga oshirish ishlamoqda...""")

    hbnumber = input("Nechta raqamni darajaga oshirmoqchisiz?: ")
    lvlNumber = int(input("Son(lar)ni necha marta oshirmoqchisiz?: "))
    
    if hbnumber == '1':
        number_1 = int(input("Darajaga oshirmoqchi bo'lgan sonni kirgazing!: "))
        print(f"{number_1} ** {lvlNumber} = {number_1 ** lvlNumber}")

    elif hbnumber == '2':
        number_1 = int(input("Birinchi sonni kirgazing!: "))
        number_2 = int(input("Ikkinchi sonni kirgazing!: "))

        print(f"number-1: {number_1} ** {lvlNumber} = {number_1 ** lvlNumber}")
        print(f"number-2: {number_2} ** {lvlNumber} = {number_2 ** lvlNumber}")
    
    elif hbnumber == '3':
        number_1 = int(input("Birinchi sonni kirgazing!: "))
        number_2 = int(input("Ikkinchi sonni kirgazing!: "))
        number_3 = int(input("Uchinchi sonni kirgazing!: "))
        
        print(f"number-1: {number_1} ** {lvlNumber} = {number_1 ** lvlNumber}")
        print(f"number-2: {number_2} ** {lvlNumber} = {number_2 ** lvlNumber}")
        print(f"number-3: {number_3} ** {lvlNumber} = {number_3 ** lvlNumber}")
    
    elif hbnumber == '4':
        number_1 = int(input("Birinchi sonni kirgazing!: "))
        number_2 = int(input("Ikkinchi sonni kirgazing!: "))
        number_3 = int(input("Uchinchi sonni kirgazing!: "))
        number_4 = int(input("To'rtinchi sonni kirgazing!: "))
        
        print(f"number-1: {number_1} ** {lvlNumber} = {number_1 ** lvlNumber}")
        print(f"number-2: {number_2} ** {lvlNumber} = {number_2 ** lvlNumber}")
        print(f"number-3: {number_3} ** {lvlNumber} = {number_3 ** lvlNumber}")
        print(f"number-4: {number_4} ** {lvlNumber} = {number_4 ** lvlNumber}")

    elif hbnumber == '5':
        number_1 = int(input("Birinchi sonni kirgazing!: "))
        number_2 = int(input("Ikkinchi sonni kirgazing!: "))
        number_3 = int(input("Uchinchi sonni kirgazing!: "))
        number_4 = int(input("To'rtinchi sonni kirgazing!: "))
        number_5 = int(input("Beshinchi sonni kirgazing!: "))
        
        print(f"number-1: {number_1} ** {lvlNumber} = {number_1 ** lvlNumber}")
        print(f"number-2: {number_2} ** {lvlNumber} = {number_2 ** lvlNumber}")
        print(f"number-3: {number_3} ** {lvlNumber} = {number_3 ** lvlNumber}")
        print(f"number-4: {number_4} ** {lvlNumber} = {number_4 ** lvlNumber}")
        print(f"number-5: {number_5} ** {lvlNumber} = {number_5 ** lvlNumber}")

    else : 
        print("""
    Hozirda sonlar cheklovi: 1 dan 5 gacha.
    """)
        
elif calcType == "3":
    print("""
    BMI ishlamoqda...""")

    weight = int(input("Vazningizni kirgazing (67): "))
    height = float(input("Bo'yingiz balandligini kirgazing (1.73): "))

    bmi = int( weight / (height * 2));

    if bmi < 18.5:
        print("Umumiy ball:",bmi, "!Sizda ozg'inlik aniqlandi!");
    elif bmi >= 18.5 and bmi <= 30:
        print("Umumiy ball:",bmi, '!Siz Normal vaznga egasiz!');
    elif bmi > 30:
        print("Umumiy ball:",bmi, "!Sizda Semizlik mavjud!");
    else :
        print("Qiymat berishda xatolik bor!!!")
