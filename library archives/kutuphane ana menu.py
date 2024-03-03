import newyork.newbest
import fambook.famousbooks
import magazines.magg
def anamenu():
    print("╔═════════════════╔════════════════╗═════════════════╗")
    print("║═════════════════╚LIBRARY ARCHIVES╝═════════════════║")
    print("║         1-  Famous Books                           ║ ")
    print("║         2-  New York Best Sellers                  ║ ")
    print("║         3-   Magazines                             ║ ")                            
    print("║         4-   News                                  ║ ")
    print("║         5-   Cooking Books                         ║ ")
    print("║         6-   Art Books                             ║ ")
    print("║                                                    ║ ")
    print("╚════════════════════════════════════════════════════╝ ")

    print(" What's your choice? ")

    choice = input()

    if choice == "1" :
        fambook.famousbooks.fmmenu()
        anamenu()

    if choice == "2" :
         newyork.newbest.bsmenu()
         anamenu()
         
    if choice == "3" :
         magazines.magg.mgmenu()
         anamenu()

anamenu()

# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
#https://drive.google.com/drive/folders/1fzxnG68VzCvC4HIsVslMmQc7IHDtXt3c
