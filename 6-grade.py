usr = input("Ismingizni kirganing!")
grade = int(input("Imtihon bagʻringizni kirganing!"))

if grade >= 85 and grade <= 100 :
    print(f"""Sizning balingiz: {grade} "A+",
{usr} , siz imtihonni 'muvaffaqiyatli' topshirdingi!""")

elif grade >= 75 and grade < 85 :
    print(f"""Sizning balingiz: {grade} "B",
{usr}, siz imtihonni 'yaxshi' topshirdingiz!""")

elif grade >= 65 and grade < 75 :
    print(f"""Sizning balingiz: {grade} "C",
{usr}, siz imtihonni 'qoniqarli' topshirdingi!""")

elif grade >= 55 and grade < 65 :
    print(f""" Sizning balingiZ: {grade} "D",
{usr}, siz imtihonni 'yomon' topshirdingi!!""")
    
elif grade >= 45 and grade < 55 :
    print(f"""Sizning umumiy balingiz: {grade} "F",
{usr} Afsuski siz imtihondan oʻta olmadingiz!""")
else : 
    print("E'tiborli bo'ling!!! Siz kiritgan amallar noto'g'ri bo'lishi mumkin!!!")