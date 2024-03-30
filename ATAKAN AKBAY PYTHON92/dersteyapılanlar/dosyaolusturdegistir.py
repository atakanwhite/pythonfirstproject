# try :
#     okunan = open("deneme2.txt","r")
#     print(okunan)
#     okunan.close()

# except :
#     print("Bir hatayla karşılaşıldı.")

# not1=5
# with open ("sayılar.txt","a") as xx:
#     for a in range(10):
#         #xx.write(a) #dosyaya int yazılamaz
#         xx.write(f"{a}")
#         xx.write(f"\n{a}")

# try: 
#     okunan = open("dosyaornek.txt","r")
#     print(okunan.readline())
#     print(okunan.readline())
#     print(okunan.readline())
    

#     okunan.close()
# except:
#     print("Bir hata oluştu.")

# okunan= open("dosyaornek.txt","r")
# for a in okunan:
#     print(a)

# okunan.close()

# a = input("Sayı giriniz:")
# b = input("İkinci sayıyı giriniz:")
# c = a+b
# dosya = open("deneme4.txt","w")
# dosya.write(str(c))
# dosya.close()

# okunan = open("deneme4.txt")
# aa = okunan.read()
# print(aa)
# print(aa*2)
# print(int(aa)*2)
# okunan.close()

ad = input("Kaydedilecek kişi adı:               ")
no= input("Kaydedilecek kişi numarası:           ")
ogrenci ={
    "Adi" : ad,
    "Numarası" : no
}
dosya = open("dosyalar/rehber1.txt","a")
dosya.write(f"{str(ogrenci)}\n")
dosya.close()

okunan = open("dosyalar/rehber1.txt")
bb = okunan.readlines()
aa = bb
for a in aa:
    print(a)

okunan.close()
