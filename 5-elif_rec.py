ainame = "Elif-tavsiyaAi"
version = "1.0"
programmer = "Mukhammadmaqsud"

user = "Mukhammadmaqsud"

greet = f"Salom {user}, ahvollaringiz qanday?"
intr = f"""O'zimni tanishtirsam, Men {ainame} man.
Sizga sog'ligingiz bo'yicha tavsiya bera olaman"""
opps = f"""
Bizning hozirgi versiyamiz: {version}va imkoniyatlari
juda cheklanga. Hozirda bu "elif-tavsiya.ai" berayotgan imkoniyatlar:

    ~ Bosh og'rig'i
        - Boshning old qismi
        - Boshning ikkla yon qismi
        - Boshning orqa qismi
        - Qattiq og'riq
        
    ~ Qorin og'rig'i
        - Qorinnning burab og'rishi
        - Qorinning sanchib og'rishi
        - Ichaklardagi og'riq / ko'ngil aynishi
        - Noodatiy og'riq, qattiq og'riq
    
    ~ Mushaklardagi og'riq
        - Toliqish
        - Kuchsizlanish
        - Qattiq og'riq turishi

    ~ Holsizlanish - o'zini yomon his qilish
"""

sertype = input("""
======================
Sizga qanday yordam bera olaman? Qanday xizmat turi kerakligini tanlang:
    ~ AI bilan tanishish (tanishish | 1)
    ~ BMI ni o'lchash (bmi | 2)
    ~ Aqilli calculator dan foydalanish (calculator | 3)
    ~ Tavsiya AI dan foydalanish (tavsiya.ai | 4 )
======================
    """);

if sertype == "1" or sertype == "tanishish":
    print(f"""====================
          AI bilan tanishish...
        elif-tavsiya.ai {version} - bu boshlang'ich python dasturchisi tomonidan faqat if-elif-else mavzulari yordamida yozilgan juda cheklangan AI hisoblanadi. AI dagi ba'zi tavsiya real hayotga to'g'ri kelmasligi mumkin. Bu kichik dastur mavzularni chuqurroq tushunish uchun ishlab chiqilgan! 
        Dasturchi: {programmer}
====================
""")
    sertype = """
====================Yana boshqa amallardan foydalanmoqchi bo'lsangiz:?
    ~ AI bilan tanishish (tanishish | 1)
    ~ BMI ni o'lchash (bmi | 2)
    ~ Aqilli calculator dan foydalanish (calculator | 3)
    ~ Tavsiya AI dan foydalanish (tavsiya.ai | 4 )
====================
    """
    input(sertype)

elif sertype == "2" or sertype == "bmi":
    content = (f"""BMI ishlamoqda...
    Sizning BMI ko'rsatgichingizni ko'rish xisoblash uchun bizga avval
    vazn va bo'yingiz balandligini .sm da kirgazishingiz kerak!""")
    print(content.center(30, "-"))

    usrWeight = int(input('Vazningizni kirgazing(72): )'))
    usrHeight = int(input("Bo'yingiz balandligini kirgazing! (178): "))
    
    usrBMI = int(usrWeight / ((usrHeight / 100) ** 2))
    if usrBMI <= 18.5:
        bmicon = "Sizda ozg'inlik aniqlandi"
        print(f"Sizning BMI ko'rsatgichingiz: {usrBMI}, {bmicon}");
    elif usrBMI > 18.5 and usrBMI < 25 :
        bmicon = "Sizning vazningiz normal"
        print(f"Sizning BMI ko'rsatgichingiz: {usrBMI}, {bmicon}");

    elif usrBMI > 25  and usrBMI < 35:
        bmicon = "Sizda ortiqcha vazn bor"
        print(f"Sizning BMI ko'rsatgichingiz: {usrBMI}, {bmicon}");
    
    else:
        bmicon = "!!!Tizimda xatolik!!!"
        usrBMI = "Noto'g'ri amallar kiritdingiz!"
        print(f"{bmicon}, {usrBMI}");

    sertype = input("""
======================
Sizga yana qanday yordam bera olamiz?:
    ~ AI bilan tanishish (tanishish | 1)
    ~ BMI ni o'lchash (bmi | 2)
    ~ Aqilli calculator dan foydalanish (calculator | 3)
    ~ Tavsiya AI dan foydalanish (tavsiya.ai | 4 )
======================
    """);

elif sertype == "3" or sertype =="calculator": 
    print(f"""======================
Calculator ishlamoqda...""");
    
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

elif sertype == "4" or sertype == "tavsiya.ai":
    print(f"""elif-tavsiya.ai ishlamoqda...
{opps}""")
    input("""======================

    O'zingizni qanday his qilayapsiz?""")
    dgnstype = input("""
    Sizni nima bezovta qilayotganini aniq, men ko'rsatgan 
holatda kiriting!: 
    ~ Boshingiz og'riyotgan bo'lsa - bosh og'rishi | 1
    ~ Og'riq qorningizda bo'lsa - qorin og'rishi | 2
    ~ Mushaklar og'riyotgan bo'lsa  - mushaklar | 3
    ~ Holsizlanayotgan bo'lsangiz - holsizlanish | 4
    ~ Boshqa turdagi yordam kerak bo'lsa - boshqa | 0""")

    if dgnstype == "bosh og'rishi" or dgnstype == "1" :
        print("""Yanada aniqroq javob bera olasizmi, og'riq 
boshingizning qaysi qismida???
    ~ Og'riq boshning oldi qismida - old qism | 1;
    ~ Og'riq boshning ikkala yon qismida - yon qismlarda | 2;
    ~ O'griq boshning orqa qismida - orqasida | 3;
    ~ Og'riq qattiq&Noodatiy og'riq | qattiq og'riq | 4""")
        
        dgnshead = input("Qo'llanmaga qarab og'riq turini kirgazing!:")
        if dgnshead == "old qism" or dgnshead == "1": 
            print("""   Keling avvalo boshning old qismida og'riq turishining
sabablarini ko'rib chiqsak:
    ~ Stress;
    ~ Uyqusizlik;
    ~ Tanadagi suv yetishmovchiligi.

Bu holatlarda dori ichish tavsiya etilmaydi! Uning o'rniga: dam oling,
cofein iste'mol qiling, imkon bo'lsa sayr qilishga chiqing. Agar og'riq qolmasa
yengil dorilarni iste'mol qilishingiz mumkin: 
    ~ Parasetomol;
    ~ Kupen;
    ~ ***
""")            
        elif dgnshead == "yon qismlar" or dgnshead == "2":
            print("""   Boshning ikkala yon qismida og'riq turishi asosan
charchash, qattiq ishlash sababidan kelib chiqadi.
Sizga maslahatim: Kuchli bo'lmagan og'riq qoldiruvchi dori ichishingiz mumkin...
Ammo ehtiyot bo'ling, dorilar kuchli va shifokor tavsiyasisiz bo'lgan dorilar
iste'moli qat'iyan man etiladi!!!
""");
        
        elif dgnshead == "orqa qismda" or dgnshead == "3":
            print("""   Boshning orqa qismida og'riq turishining sabablari bir nechta:
~ Qon bosimining ortishi;
~ Umurtqa pog'onasi astexandrozi;
~ Noto'g'ri yotib qolish
Bu xolatlarda biror dori ichish emas, mutahasis ko'rigiga borish tavsiya qilinadi!""");
   
        elif dgnshead == "qattiq og'riq" or dgnshead == "4":
            print("!!!Har qanday noodatiy va qattiq og'riq turadigan bo'lsa shifokor ko'rigiga borish tavsiya qilinadi!!!")
        else :
            print(f"""E'tiborli bo'ling!!! {dgnshead} degan javob yo'q!
Qaytadan ishga tushiring!""")


    elif dgnstype ==  "qorin og'rishi" or dgnstype == "2":
        print("""Aniqroq javob bera olasizmi, qanday og'riq bezovta qilmoqda??
    ~ Qorinning buralib o'g'rishi -  buralib og'rish | 1;
    ~ Qorinning sanchib og'rishi - sanchishi | 2;
    ~ Ichaklardagi og'riq - ichaklarda | 3;
    ~ Noodatiy & Qattqi og'rishi -  qattiq og'riq | 4""")
        
        dgnstmch = input("Qo'llanmaga qarab og'riq turini kirgazing!:")
        if dgnstmch == "buralib og'rish" or dgnstmch == "1":
            print("""
    Qorin buralib og‘rishi (kramplar) ko‘pincha ovqat hazm qilish buzilishi
gaz yig‘ilishi, ichak infeksiyalari yoki noto‘g‘ri ovqatlanish natijasida
kelib chiqadi. Shuningdek, stress, ich qotishi, appenditsit, buyrak toshlari
yoki ayollarda ginekologik muammolar ham shunday og‘riqqa sabab bo‘lishi mumkin.

    Qachon shifokorga murojaat qilish kerak? Agar og‘riq juda kuchli bo‘lsa
    tana harorati ko‘tarilsa, qusish, ich ketishi to‘xtamasa yoki og‘riq o‘ng
    pastki qismga o‘tsa, zudlik bilan shifokorga murojaat qilish zarur.""")
        elif dgnstmch == "sanchib og'rish" or dgnstmch == "2": 
            print("""
    Qorin sanchib og'rishiko'pincha ovqat hazm qilish uchun, gaz to'p, ichak
spazmlari yoki o't pufagi/pankreatit kabi yallig'lanishli yordam beradi..
sekin, apenditsit, churra, erta toshlari yoki ginekologik muammolar(ayollarda) 
ham o'tkir sanchiqqa sabab bo'lishi mumkin.
    Qachonga murojaat qilish kerak? Agar og'riq juda kuchli bo'lsa, tan
harorati ko'tarilsa, qusish, ichakda qon bo'lishi yoki og'riq harakatlanganda,
aksirganda kuchaysa, zudlik bilan yordamga (tez yordamga) murojaat qilish kerak.
""")
        elif dgnstmch == "ichaklardagi og'rishi" or dgnstmch == "3":
            print("""
Ichaklardagi og'riqlar (kolikalar, spazmlar)ko'pincha ovqat qilish tizimidagi
kasalliklar, kasalliklar, kasallik'lanishlar yoki shikastlanishlar (kolit,
enterit) zarar keltiradi.. asosiy sabablar orasida meteorizm (gaz yig'ilishi),
zaharlanish, ich qotishi yoki parazitlar bo'lishi mumkin. Kuchli va davom yuk
og'riqlarda qaytaga murojaat qilish shart.
                  
Qachonga murojaat qilish kerak?
~ Og'riq juda kuchli va to'satdan boshlansa.
~ Tana harorati ko'tarilsa.
~ Qonli ich ketishi yoki to'xtovsiz qusish bo'lsa.
~ Og'riq bir necha soatdan ortiq davom etsa.""")
        else : 
            print(f"""E'tiborli bo'ling siz {dgnstmch} deb yozdingiz!!!
Ammo qo'llanmada undan tanlov yo'q!""")
    
    elif dgnstype == "mushaklardagi og'riq" or dgnstype == "3":
        print("""Agar sizni mushaklardagi og'riqlar be'zovta qilayotgan bo'lsa,
ko'rsatma bo'yicha qandayligini tanlang
    ~ Mushaklarda toliqishni his qilish -  toliqish | 1
    ~ Mushaklarda kuchsizlanishni his qilish - kuchsizlanish | 2;
    ~ Mushaklarda qattiq o'g'riq turishi - qattiq og'riq turishi | 3;
""")
    
    elif dgnstype == "holsizlanish" or dgnstype == "4":
        print("""   Bu holatda sizga tashxis qo'yish biroz qiyin. 
Ammo maslahat bera olaman. Maslahatim shuki zudlik bilan mutahasis ko'rigiga boring!!! Og'riq qoldiruvchi ichish yoki boshqa tanlovlar o'zini oqlamaydi""")
        
    else: 
        print(f"Etiborli bo'ling, siz {dgnstype} deb yozdingiz, ammo bunday tanlov yo'q!")
else : print(f"""eEeeey, E'tibor bering!! Siz {sertype} dedingiz ammo, bunday tanlov yo'q""");