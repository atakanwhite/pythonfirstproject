from PyQt6.QtWidgets import *

#PROJE 3 VEKTOREL BILISIM TELEFON REHBERI KAYDETME SISTEMI 
class loginPenceresi(QMainWindow):
  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Username'))
    self.edit1 = QLineEdit('Insert username')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Password:'))
    self.edit2 = QLineEdit()
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Log In')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kontrolEt)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kontrolEt(self):
    print("Button clicked!")
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 :", t1)
    print("Edit 2 :", t2)
    dosya = open("rhbgirilenpwd.txt","w")
    dosya.write(f"{t1} {t2}")
    dosya.close()

    if t1=="adm" and t2 == "123" :
      print("Successfully logged in.")
      self.close()
      self.ap = anaEkran()
      self.ap.show()
    else:
      print("İzin yok")
      dlg = QMessageBox(self)
      dlg.setWindowTitle("IMPORTANT!")
      dlg.setText("Permission denied.")
      dlg.exec()


def sifreOlustur():
  kullaniciAdi = "adm"
  sifre = "123"
  dosya = open("rhbpwd.txt","w")
  dosya.write(f"{kullaniciAdi} {sifre}")
  dosya.close()

class anaEkran(QMainWindow):
  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    self.dugme1 = QPushButton('Add')
    icerik.addWidget(self.dugme1)
    self.dugme2 = QPushButton('List')
    icerik.addWidget(self.dugme2)
    self.dugme3 = QPushButton('Search')
    icerik.addWidget(self.dugme3)
    self.dugme4 = QPushButton('Delete')
    icerik.addWidget(self.dugme4)
    self.dugme5 = QPushButton('Edit')
    icerik.addWidget(self.dugme5)

    self.dugme1.clicked.connect(self.ekle)
    self.dugme2.clicked.connect(self.listele)
    self.dugme3.clicked.connect(self.ara)
    self.dugme4.clicked.connect(self.sil)
    self.dugme5.clicked.connect(self.duzelt)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def ekle(self):
    self.close()
    self.ekleme = EkleEkrani('Add Menu')
    self.ekleme.show()

  def listele(self):
    self.close()
    self.listeleme = VeriListeEkrani('List Menu')
    self.listeleme.show()

  def ara(self):
    self.close()
    self.arama = AramaEkrani('Search Menu')
    self.arama.show()

  def sil(self):
    self.close()
    self.silme = SilmeEkrani('Delete Menu')
    self.silme.show()

  def duzelt(self):
    self.close()
    self.duzeltme = DuzeltmeEkrani('Edit Menu')
    self.duzeltme.show()



class loginPenceresi(QMainWindow):
  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Usernamee:'))
    self.edit1 = QLineEdit('Enter username')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Password:'))
    self.edit2 = QLineEdit()
    self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Log In')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kontrolEt)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kontrolEt(self):
    print("Button clicked!")
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 :", t1)
    print("Edit 2 :", t2)
    dosya = open("rhbgirilenpwd.txt","w")
    dosya.write(f"{t1} {t2}")
    dosya.close()

    if t1=="adm" and t2 == "123" :
      print("Permission granted.")
      self.close()
      self.ap = anaEkran()
      self.ap.show()
    else:
      print("No permission for the action.")
      dlg = QMessageBox(self)
      dlg.setWindowTitle("IMPORTANT!")
      dlg.setText("No permission for the action.")
      dlg.exec()

class EkleEkrani(QMainWindow):
  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Name/Surname:'))
    self.edit1 = QLineEdit('')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Number'))
    self.edit2 = QLineEdit()
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Save')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kaydet)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kaydet(self):
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 :", t1)
    print("Edit 2 :", t2)
    
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    svt.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,nu)")
    svt.execute(f"INSERT INTO isimler(ad,nu) VALUES ('{t1}','{t2}')")
    vt.commit()
    vt.close()

    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran() # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

class VeriListeEkrani(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    liste = svt.execute(f"SELECT * FROM isimler")
    
    # icerik = QVBoxLayout()
    icerik = QGridLayout()
    x = 1
    icerik.addWidget(QLabel('Name:'),0,1)
    icerik.addWidget(QLabel('Number:'),0,2)
    for a in liste: 
        print (a[1],a[2])
        icerik.addWidget(QLabel(a[1]),x,1) # gridLayout taki x.satır ve 1.sütuna QLable yerleştir.
        icerik.addWidget(QLabel(a[2]),x,2)
        x+=1

    # icerik.setColumnStretch(0, 2) # buna benzer bir şey ile hücre birleştirmesi yapılabilir.
    self.d1 = QPushButton('Return to main page')
    icerik.addWidget(self.d1,x,1) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata
    vt.close()

  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Main Page') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

class AramaEkrani(QMainWindow):
  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Main Page') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)
   
    # icerik = QVBoxLayout()
    self.icerik = QGridLayout()
    self.silinecek = QLineEdit()
    self.icerik.addWidget(self.silinecek,0,0)
    getirB = QPushButton('Get')
    self.icerik.addWidget(getirB,1,0)
    self.bulunanlar = []
    getirB.clicked.connect(self.getir)
    print("found:",self.bulunanlar)
    self.icerik.addWidget(QLabel('Id'),0,1)
    self.icerik.addWidget(QLabel('Name'),0,2)
    self.icerik.addWidget(QLabel('Number'),0,3)
    # adL = QLabel('...')
    # nuL = QLabel('...')

 
    # self.icerik.setColumnStretch(0, 2) # buna benzer bir şey ile hücre birleştirmesi yapılabilir.
    self.d1 = QPushButton('Return to main page')
    self.icerik.addWidget(self.d1,3,1) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata

  def getir(self):
    silinecekVeri = self.silinecek.text()
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
    x=1
    for a in gelen:
      print(a[0],a[1],a[2])
      self.icerik.addWidget(QLabel(str(a[0])),x,1)
      self.icerik.addWidget(QLabel(str(a[1])),x,2)
      self.icerik.addWidget(QLabel(str(a[2])),x,3)
      x+=1

    vt.close()

class SilmeEkrani(QMainWindow):
  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Ana ekran') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)
   
    # icerik = QVBoxLayout()
    self.icerik = QGridLayout()
    self.silinecek = QLineEdit()
    self.icerik.addWidget(self.silinecek,0,0)
    getirB = QPushButton('Get')
    self.icerik.addWidget(getirB,1,0)
    self.bulunanlar = []
    getirB.clicked.connect(self.getir)
    print("bulunanlar:",self.bulunanlar)
    self.icerik.addWidget(QLabel('Id'),0,1)
    self.icerik.addWidget(QLabel('Name'),0,2)
    self.icerik.addWidget(QLabel('Number'),0,3)
    # adL = QLabel('...')
    # nuL = QLabel('...')

    self.silinecekId = QLineEdit()
    self.icerik.addWidget(self.silinecekId,3,0)
    self.silB = QPushButton('Delete')
    self.icerik.addWidget(self.silB,4,0)
    self.silB.clicked.connect(self.sil)

 
    # self.icerik.setColumnStretch(0, 2) # buna benzer bir şey ile hücre birleştirmesi yapılabilir.
    self.d1 = QPushButton('Return to main page')
    self.icerik.addWidget(self.d1,5,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata

  def getir(self):
    silinecekVeri = self.silinecek.text()
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
    x=1
    silinecek = []
    for a in gelen:
      print(a[0],a[1],a[2])
      self.icerik.addWidget(QLabel(str(a[0])),x,1)
      self.icerik.addWidget(QLabel(str(a[1])),x,2)
      self.icerik.addWidget(QLabel(str(a[2])),x,3)
      silinecek.append(str(a[0]))
      x+=1
  
    vt.close()

  def sil(self):
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    print("self.silinecekId.text()",self.silinecekId.text())
    svt.execute(f"DELETE FROM isimler WHERE id='{self.silinecekId.text()}'")
    vt.commit()
    vt.close()
    self.close()
    self.liste = VeriListeEkrani()
    self.liste.show()
        
class DuzeltmeEkrani(QMainWindow):
  def anaEkranaDon(self):
    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran('Main Page') # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

  def __init__(self,xx="Unnamed"):
    super().__init__()
    self.setWindowTitle(xx)
   
    # icerik = QVBoxLayout()
    self.icerik = QGridLayout()
    self.silinecek = QLineEdit()
    self.icerik.addWidget(self.silinecek,0,0)
    getirB = QPushButton('Get')
    self.icerik.addWidget(getirB,1,0)

    getirB.clicked.connect(self.getir)
    # print("bulunanlar:",self.bulunanlar)
    self.icerik.addWidget(QLabel('Id'),0,1)
    self.icerik.addWidget(QLabel('Name'),0,2)
    self.icerik.addWidget(QLabel('Number'),0,3)
    self.duzelecekId = QLineEdit("id to be edited")
    self.icerik.addWidget(self.duzelecekId,3,0)

    self.yeniAd = QLineEdit("new name")
    self.icerik.addWidget(self.yeniAd,4,0)
    self.yeniNumara = QLineEdit("new number")
    self.icerik.addWidget(self.yeniNumara,5,0)

    self.silB = QPushButton('Edit')
    self.icerik.addWidget(self.silB,6,0)
    self.silB.clicked.connect(self.duzelt)

    self.d1 = QPushButton('Return to main page')
    self.icerik.addWidget(self.d1,7,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
    self.d1.clicked.connect(self.anaEkranaDon)

    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata

  def getir(self):
    silinecekVeri = self.silinecek.text()
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
    x=1
    silinecek = []
    for a in gelen:
      print(a[0],a[1],a[2])
      self.icerik.addWidget(QLabel(str(a[0])),x,1)
      self.icerik.addWidget(QLabel(str(a[1])),x,2)
      self.icerik.addWidget(QLabel(str(a[2])),x,3)
      silinecek.append(str(a[0]))
      x+=1
  
    vt.close()

  def duzelt(self):
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    print("self.duzelecekId.text()",self.duzelecekId.text())
    # svt.execute(f"DELETE FROM isimler WHERE id='{self.duzelecekId.text()}'")
    svt.execute(f"UPDATE isimler SET ad = '{self.yeniAd.text()}', nu = '{self.yeniNumara.text()}' WHERE id = '{self.duzelecekId.text()}'")
    vt.commit()
    vt.close()
    self.close()
    self.liste = VeriListeEkrani()
    self.liste.show()
        
sifreOlustur()
uygulama = QApplication([])
# pencere = loginPenceresi("Giriş1")
pencere = loginPenceresi("Giriş1")
pencere.show()
# anaPencere = anaEkran("MENU")
# anaPencere.show()
uygulama.exec() 
# self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
