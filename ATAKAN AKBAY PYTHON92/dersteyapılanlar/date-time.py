import random
import datetime
#from datetime import datetime
#print("Bugün",datetime.now())
#import datetime
#print("Şimdi =",datetime.datetime.now())
#from datetime import datetime
#for a in range (100000):
    #from datetime import datetime
    #print("Şimdi=",datetime.now())

#import datetime
#print("Tarih saat =", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
#a = datetime.datetime.now().strftime("%Y")

a = datetime.datetime.now().strftime("%Y")
a = int(a) + random.randint(1,10)

b = datetime.datetime.now().strftime("%m")
b = int(b) + random.randint(-2,9)

c = datetime.datetime.now().strftime("%d")
c = int(c) + random.randint(-22,7)

#print(c,b,a)


# Bekle
import time
print ("Bekledim.", time.sleep(3))
