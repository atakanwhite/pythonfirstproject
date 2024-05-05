from PyQt6.QtWidgets import *

def sifreOlustur():
    kullaniciAdi = "adm"
    sifre = "123"
    dosya = open("rhbpwd.txt","w")
    dosya.write(f"{kullaniciAdi} {sifre}")
    dosya.close()

class anaEkran(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)
        icerik = QVBoxLayout()
        self.dugme1 = QPushButton('Ekle')
        icerik.addWidget(self.dugme1)
        self.dugme2 = QPushButton('Listele')
        icerik.addWidget(self.dugme2)
        self.dugme3 = QPushButton('Sil')
        icerik.addWidget(self.dugme3)
        self.dugme1.clicked.connect(self.ekle)
        self.dugme2.clicked.connect(self.listele)
        self.dugme3.clicked.connect(self.sil)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def ekle(self):
        self.close()
        self.ekleme = EkleEkrani('Kayıt Ekleme')
        self.ekleme.show()

    def listele(self):
        self.close()
        self.listeleme = VeriListeEkrani('Kayıt Ekleme')
        self.listeleme.show()

    def sil(self):
        self.close()
        self.silme = SilmeEkrani('Kayıt Silme')
        self.silme.show()

class loginPenceresi(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel('Kullanıcı adı:'))
        self.edit1 = QLineEdit('Kullanıcı adınız...')
        icerik.addWidget(self.edit1)
        icerik.addWidget(QLabel('Şifre:'))
        self.edit2 = QLineEdit()
        self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.edit2)
        self.dugme1 = QPushButton('Giriş yap')
        icerik.addWidget(self.dugme1)
        self.dugme1.clicked.connect(self.kontrolEt)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kontrolEt(self):
        print("Düğmeye tıklandı..")
        t1 = self.edit1.text()
        t2 = self.edit2.text()
        print("Edit 1 içeriği:", t1)
        print("Edit 2 içeriği:", t2)
        dosya = open("rhbgirilenpwd.txt","w")
        dosya.write(f"{t1} {t2}")
        dosya.close()
        if t1=="q" and t2 == "q" :
            print("Giriş ok")
            self.close()
            self.ap = anaEkran()
            self.ap.show()
        else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()

class EkleEkrani(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel('Ad soyad:'))
        self.edit1 = QLineEdit('')
        icerik.addWidget(self.edit1)
        icerik.addWidget(QLabel('Numara'))
        self.edit2 = QLineEdit()
        icerik.addWidget(self.edit2)
        self.dugme1 = QPushButton('Kaydet')
        icerik.addWidget(self.dugme1)
        self.dugme1.clicked.connect(self.kaydet)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kaydet(self):
        t1 = self.edit1.text()
        t2 = self.edit2.text()
        print("Edit 1 içeriği:", t1)
        print("Edit 2 içeriği:", t2)
        import sqlite3
        vt = sqlite3.connect('rehber.db')
        svt = vt.cursor()
        svt.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,nu)")
        svt.execute(f"INSERT INTO isimler(ad,nu) VALUES ('{t1}','{t2}')")
        vt.commit()
        vt.close()
        self.close()
        self.ae = anaEkran()
        self.ae.show()

class VeriListeEkrani(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)
        import sqlite3
        vt = sqlite3.connect('rehber.db')
        svt = vt.cursor()
        liste = svt.execute(f"SELECT * FROM isimler")
        icerik = QGridLayout()
        x = 1
        icerik.addWidget(QLabel('Adı'),0,1)
        icerik.addWidget(QLabel('Numarası'),0,2)
        for a in liste:
            print (a[1],a[2])
            icerik.addWidget(QLabel(a[1]),x,1)
            icerik.addWidget(QLabel(a[2]),x,2)
            x+=1
        self.d1 = QPushButton('Ana ekrana dön')
        icerik.addWidget(self.d1,x,1)
        self.d1.clicked.connect(self.anaEkranaDon)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
        vt.close()

    def anaEkranaDon(self):
        self.close()
        self.ae = anaEkran('Ana ekran')
        self.ae.show()

class SilmeEkrani(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)
        import sqlite3
        vt = sqlite3.connect('rehber.db')
        svt = vt.cursor()
        icerik = QGridLayout()
        silinecek = QLineEdit()
        icerik.addWidget(silinecek,0,0)
        silinecekVeri = silinecek.text()
        getirB = QPushButton('Getir')
        icerik.addWidget(getirB,1,0)
        icerik.addWidget(QLabel('Adı'),0,1)
        icerik.addWidget(QLabel('Numarası'),0,2)
        adL = QLabel('...')
        nuL = QLabel('...')
        icerik.addWidget(adL,1,1)
        icerik.addWidget(nuL,1,2)

        def getir():
            gelen = svt.execute(f"SELECT * FROM isimler")
            self.d1 = QPushButton('Ana ekrana dön')
           