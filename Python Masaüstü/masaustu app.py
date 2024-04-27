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

import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
pencere = QWidget()
pencere.setWindowTitle("MERİT ROYAL DENEME BONUSU ALMAK İÇİN ŞİMDİ KATIL")
window = QPushButton("BONUSU ALMAK İÇİN TIKLA")
window.show()
pencere.setFixedSize(300,300)
pencere.show()



app.exec()



#ÖRNEKLER PYQT SLAYTINDAN ALINMIŞ VE YAPILMIŞTIR.