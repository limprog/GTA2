text = "ручное короткоствольное стрелковое оружие, предназначенное для поражения целей (живой силы и других) на дальности до 25-50 метров."
splitted = text.split()
for i, s in enumerate(splitted):
    if i%3==0 and i>0:
        splitted[i] = splitted[i]+'\n'
result = " ".join(splitted)
print(repr(result))
