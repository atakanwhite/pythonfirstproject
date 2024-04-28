#///ÖRNEK 1///
# from PyQt5.QtWidgets import *
# app = QApplication([])
# pencere = QWidget()
# pencere.show()
# app.exec()

# 2 ve 3. satırdaki kodlar nesne sınıfı/// exec açılan tab in açık kalmasını sağlıyor.

#///ÖRNEK 2///
# import sys
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# #Event loop starts.
# app.exec()

# ///ÖRNEK 3///
# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QPushButton("Tıkla")
# window.show()
# app.exec()

# ///ÖRNEK 4///
# from PyQt6.QtWidgets import *
# # Uygulama oluşturma
# app = QApplication([])
# # buraya araçlar(widgets) ekleme
# label = QLabel('Merhaba!')
# label.show()
# # Uygulamayı çalıştırma
# app.exec()


# ÖRNEK 5
# import sys
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# pencere = QWidget()
# pencere.setWindowTitle("MERİT ROYAL DENEME BONUSU ALMAK İÇİN ŞİMDİ KATIL")
# window = QPushButton("BONUSU ALMAK İÇİN TIKLA")
# window.show()
# pencere.setFixedSize(300,300)
# pencere.show()
#app.exec()


# ÖRNEK 6
# from PyQt5.QtWidgets import *
# aa = QApplication([])
# ww = QWidget() #pencere
# icerik = QVBoxLayout()

# def icerikolustur(xx):
#     xx.addWidget(QPushButton("TIKLA"))
#     xx.addWidget(QPushButton("BONUSUNU AL"))
#     xx.addWidget(QLabel("Bilgi"))

# icerik = QVBoxLayout()
# icerikolustur(icerik)
# ww.setLayout(icerik)

# icerik2 = QVBoxLayout()
# icerikolustur(icerik2)
# ww.setLayout(icerik2)


# ww.show()
# aa.exec()


#ÖRNEK 7
# from PyQt5.QtWidgets import *
# aa = QApplication([])
# ww = QWidget()
# ww1 = QWidget() #pencereler ww olanlar

# def icerikolustur(xx):
#     xx.addWidget(QLabel("Kullanıcı Adı:"))
#     xx.addWidget(QLineEdit("Kullanıcı adınızı buraya girin."))
#     xx.addWidget(QLabel("Şifre:"))
#     xx.addWidget(QLineEdit())
#     xx.addWidget(QPushButton("Giriş Yap"))

# icerik = QVBoxLayout()
# icerikolustur(icerik)
# ww.setLayout(icerik)
# ww.show()

# icerik2 = QHBoxLayout()
# icerikolustur(icerik2)
# ww1.setLayout(icerik2)
# ww1.show()

# aa.exec()


#ÖRNEK 8

# from PyQt6.QtWidgets import *

# class loginPenceresi(QMainWindow):
# def __init__(self,xx="Başlıksız"):
# super().__init__()
# self.setWindowTitle(xx)

# icerik = QVBoxLayout()
# icerik.addWidget(QLabel('Kullanıcı adı:'))
# icerik.addWidget(QLineEdit('Kullanıcı adınız...'))
# icerik.addWidget(QLabel('Şifre:'))
# icerik.addWidget(QLineEdit())
# icerik.addWidget(QPushButton('Giriş yap'))

# araclar = QWidget()
# araclar.setLayout(icerik)
# self.setCentralWidget(araclar)

# uygulama = QApplication([])
# pencere = loginPenceresi("Giriş")
# pencere.show()
# uygulama.exec()

#ÖRNEK 8 
# Buton ekleyelim
# from PyQt5.QtWidgets import *
# aa = QApplication([])
# ww = QWidget() # pencere
# ww1 = QWidget() # pencere

# def icerikOlustur(xx):
#     xx.addWidget(QLabel('Kullanıcı adı:'))
#     xx.addWidget(QLineEdit('Kullanıcı adınız...'))
#     xx.addWidget(QLabel('Şifre:'))
#     xx.addWidget(QLineEdit())
#     xx.addWidget(QPushButton('Giriş yap'))

# icerik = QVBoxLayout()
# icerikOlustur(icerik)
# ww.setLayout(icerik)
# ww.show()

# icerik2 = QHBoxLayout()
# icerikOlustur(icerik2)
# ww1.setLayout(icerik2)
# ww1.show()

# aa.exec()


# # Tıklama algılama
# from PyQt6.QtWidgets import *

# app = QApplication([])
# button = QPushButton('Click')

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('Tıkladın!')
#     alert.exec()

# button.clicked.connect(on_button_clicked)
# button.show()
# app.exec()

#ÖRNEK 9 

from PyQt6.QtWidgets import *

dosya = open("rehberpwd.txt","w")
dosya.write("adm 123")
dosya.close


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
        print("Edit 1 içeriği:", t1)

uygulama = QApplication([])
pencere = loginPenceresi("Giriş")
pencere.show()
uygulama.exec() 

#ÖRNEKLER ERDINC DONMEZ PYQT SLAYTINDAN ALINMIŞ VE YAPILMIŞTIR.