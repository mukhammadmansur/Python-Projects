weight = int(input("Vazningizni kirgazing (67): "))
height = float(input("Bo'yingiz balandligini kirgazing (1.73): "))

bmi = int( weight / (height * 2));

if (bmi < 18.5):
    print("Umumiy ball:",bmi, "!Sizda ozg'inlik aniqlandi!");
elif (bmi >= 18.5 and bmi <= 30):
    print("Umumiy ball:",bmi, '!Siz Normal vaznga egasiz!');
elif (bmi > 30):
    print("Umumiy ball:",bmi, "!Sizda Semizlik mavjud!");
else :
    print("Qiymat berishda xatolik bor!!!")
