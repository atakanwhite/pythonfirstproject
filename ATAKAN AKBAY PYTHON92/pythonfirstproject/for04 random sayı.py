import random
bas = 1 
son = 100
tutulan = random.randint(bas,son)
print(f"Ben {bas} ile {son} arası bir sayı tuttum.")
print(tutulan)


import random
bas = 1
son = 100
hak = 5
tutulan = random.randint(bas,son)
print(tutulan)
print(f"Ben {bas} ile {son} arası bir sayı tuttum.")
print(f"{hak} hakkın var.")

for xx in range(hak):
    tahmin = int(input("tahminin nedir?"))
    if tahmin == tutulan:
        print("Bildin.")
        break
    elif tahmin > tutulan:
        print("Tahminin büyük.")
        tahmin = int(input("Tahminin nedir?"))
    elif tahmin < tutulan:
        print("Tahminin küçük.")
        tahmin = int(input("Tahminin nedir?"))