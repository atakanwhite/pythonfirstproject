# try :
#     okunan = open("deneme2.txt","r")
#     print(okunan)
#     okunan.close()

# except :
#     print("Bir hatayla karşılaşıldı.")

not1=5
with open ("sayılar.txt","a") as xx:
    for a in range(10):
        #xx.write(a) #dosyaya int yazılamaz
        xx.write(f"{a}")
        xx.write(f"\n{a}")
