calcType = input("""    Qanday hisobni amalga oshirmoqchisiz?
(darajaga oshirish, kubga oshirish, calculator | 1, 2, 3)""")

if (calcType == "darajaga oshirish" or calcType == "1"):
    inpNumber = int(input("Darajaga oshirish kerak bo'lgan sonni kirgazing!: "));
    numberLvl = int(input("Orttirmoqchi bo'lgan darajangizni kiriting: "))
    print(inpNumber ** numberLvl)

elif (calcType == "kubga oshirish" or calcType == "2"):
    inpNumber = int(input("Kubga oshirish kerak bo'lgan sonni kirgazing!"))
    print(inpNumber * inpNumber * inpNumber);

elif (calcType == "calculator" or calcType == "3"):
    
    print("""
          Calculator ishlamoqda...
          """)
    
    x = int(input("Birinchi sonni kirgazing!: "))
    b = input("Amalni kirgazing (+, -, *, /, **): ")     
    y = int(input("Ikkinchi sonni kirgazing!: "))
    if (b == "+"):
        print(x + y)
    elif (b == "-"):
        print(x - y)
    elif ( b == "*" ):
        print(x * y)
    elif ( b == "/" ):
        print(x / y)
    elif ( b == "**" ):
        print ( x ** y )
    else : 
        print("""  Noto'g'ri a'malni tanladingiz!""")

else : 
    print("""
    Nimadur Xato Ketdi,
Noto'g'ri xisob-kitob turini tanladingiz!""");