mins = int(input(""))
sekund = int(input(""))
days = int(input(""))
obshaya_sekunda = (mins*60+sekund) * days
chasi = int(obshaya_sekunda / 60 // 60)
sekund = obshaya_sekunda % 60
minuta = obshaya_sekunda // 60 % 60
print(chasi,minuta,sekund)
