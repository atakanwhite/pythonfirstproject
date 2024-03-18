def topla(aa,bb):
    return f"Toplam:{aa+bb}"

def carp(xx,yy):
    return f"Carpim:{xx*yy}"

sayi1 = int(input("Birinci sayı nedir?"))
sayi2 = int(input("İkinci sayı nedir?"))

#sayi1 = 3
#sayi2 = 9
#topla(4,6)
#topla(sayi1,sayi2)
#topla(sayi1,topla(sayi2,sayi2))
print (topla(sayi1,sayi2))
print (carp(sayi1,sayi2))

#yazdığımız fonk sayesinde f sonrasındaki değer sayı1,sayı2 yerine yazılmış oldu ve sonra returnle değer yerine döndü
#fonksiyonlarda geri dönüş için return kullan 