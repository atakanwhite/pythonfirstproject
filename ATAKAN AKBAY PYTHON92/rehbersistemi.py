import re, json, ast
def menu():
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║      CONTACTS       ║" )
    print("║═════════════════════║")
    print("║                     ║")
    print("║  1-Add a number     ║")
    print("║  2-Contact List     ║")
    print("║  3-Search           ║")
    print("║  4-Edit             ║")
    print("║  5-Delete           ║")
    print("║                     ║")
    print("║  Insert one of the  ║")
    print("║  numbers to choose  ║")
    print("╚═════════════════════╝")
    # 201 ╔ 187 ╗ 200 ╚  # 188 ╝
    choice = input("")
    if choice=="1":
        list(); addnumber()
        list(); menu()
    if choice=="2":
        list(); menu()
    if choice=="3":
        search(); menu()
    if choice=="4":
        edit(); list()
        menu()
    if choice=="5":
        delete(); list(); menu()
def addnumber():

    # kayitSayisi = dosya.read()
    # kayitSayisi = ast.literal_eval(kayitSayisi)
    # dosya.close()

    dosya = open("contactmenu.txt","a")
    print("╠════════╣ ADD A NUMBER ╠════════╣")
    ad = input("Name and Surname :                       ")
    nu = input("Number:                           ")
    # veri = {"adi":ad,"num":nu}
    # dosya.write(f"{ad},{nu},")
    # ks = kayitSayisi+1
    # print(f"Veri {len(kayitSayisi)+1}.kayit olarak eklendi")
    dosya.write(str({"name":ad,"num":nu})+",")
    # dosya.write(str({"id":ks,"adi":ad,"num":nu})+",")
    dosya.close()

def list():
    try:
        with open("contactmenu.txt", "r") as dosya:
            okunan = dosya.read()
        print("╠═════╣ CONTACT LIST ╠═════╣")

        cevirilen = ast.literal_eval(okunan)
        print(cevirilen)

        # for a in cevirilen:
            # print (a)
    except :
        print("A problem has occurred.")          

def search():
    with open("contactmenu.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ SEARCH ╠════════════╣")
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Name?")
    for a in cevirilen:
        if a["adi"]==aranan: print(a)
def edit():
    with open("contactmenu.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ EDIT MENU ╠════════════╣")
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Name to be edited: ")
    dosya.close()
    with open("contactmenu.txt","w") as dosya:
        for a in cevirilen:
            if a["adi"]==aranan:
                print(a)
                yeniAd = input("Name: ")
                yeniNo = input("Number: ")
                a["adi"]=yeniAd
                a["num"]=yeniNo
            dosya.write(f"{str(a)},")        
def delete():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ DELETE ╠════════════╣")
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Who do you want to delete? ")
    dosya.close()
    with open("rehber.txt","w") as dosya:
        for a in cevirilen:
            if a["adi"]!=aranan:
                dosya.write(f"{str(a)},")
menu()