men = float(input("доходы мужа"))
women = float(input("доходы жены"))
summa=men+women
na_otpusk_rubl = int(summa * 10 /100)
na_otpusk_kop = int(summa % 10)
na_edu_rubl = int(summa * 30 /100)
na_edu_kop = int(summa % 30)
kom_platej_rubl = int(summa * 5 / 100)
kom_platej_kop = int(summa % 5)
vihodnoy_dosug_rubl = int(summa * 15 / 100)
vihodnoy_dosug_kop = int(summa % 15)
nakopleniya_rubl = int(summa * 40 / 100)
nakopleniya_kop = int(summa % 40)
print("Отпуск:", na_otpusk_rubl ,"руб.",na_otpusk_kop ,"коп.")
print("Пропитание и еда:", na_edu_rubl ,"руб.",na_edu_kop ,"коп.")
print("Коммунальные платежи:", kom_platej_rubl ,"руб.",kom_platej_kop ,"коп.")
print("Досуг:", vihodnoy_dosug_rubl ,"руб.",vihodnoy_dosug_kop ,"коп.")
print("Накопления:", nakopleniya_rubl ,"руб.",vihodnoy_dosug_kop ,"коп.")

# men = float(input())
# women = float(input())
#
# total_kop = round((men + women) * 100)  # весь доход в копейках
#
# otpusk = total_kop * 10 // 100
# eda = total_kop * 30 // 100
# kom = total_kop * 5 // 100
# dosug = total_kop * 15 // 100
# nakop = total_kop - otpusk - eda - kom - dosug
#
# def fmt(kop):
#     return f"{kop // 100} руб. {kop % 100} коп."
#
# print("Отпуск:", fmt(otpusk))
# print("Пропитание и еда:", fmt(eda))
# print("Коммунальные платежи:", fmt(kom))
# print("Досуг:", fmt(dosug))
# print("Накопления:", fmt(nakop))