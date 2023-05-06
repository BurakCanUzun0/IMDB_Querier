import requests
from bs4 import BeautifulSoup
import os
import sys
from PyQt5.QtWidgets import QAction,qApp,QMainWindow,QWidget,QApplication,QTextEdit,QLabel,QPushButton,QHBoxLayout,QFileDialog,QVBoxLayout

class IMDB(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QLabel('''This program can query for 4 categories. Top 250 Movies/Shows and Most Popular Movies/TV Shows''')
        self.sorgula = QPushButton("Query")
        self.d_url = QTextEdit("https://www.imdb.com/chart/top/")
        self.sec = QTextEdit("10")
        self.save = QPushButton("Save")
        v_box = QVBoxLayout()
        v_box.addWidget(self.d_url)
        v_box.addWidget(self.sec)
        v_box.addWidget(self.sorgula)
        v_box.addWidget(self.save)

        h_box =QVBoxLayout()
        h_box.addLayout(v_box)
        h_box.addWidget(self.yazi_alani)
        self.sorgula.clicked.connect(self.url_sorgula)
        self.save.clicked.connect(self.save_text)
        self.setLayout(h_box)
        self.show()
    def save_text(self):
        dosageyou, _ = QFileDialog.getSaveFileName(self, 'Txt Dosyası Oluştur', 'Text', 'Text Files (*.txt)')
        import_text = self.yazi_alani.text()
        if dosageyou:
            with open(dosageyou,"w") as file:
                file.write(import_text)
    def url_sorgula(self):
        self.str = self.d_url.toPlainText()
        self.islem()
    def islem(self):
        response = requests.get(self.str)
        html_icerigi = response.content
        soap = BeautifulSoup(html_icerigi,"html.parser")
        liste1=[]
        liste2=[]
        text = ""
        try:
            A = self.sec.toPlainText()
            A = int(A)
            for i in soap.find_all("strong"):
                liste1.append((i.get("title")))
            for i in soap.find_all("img"):
                liste2.append((i.get("alt")))
            for i in range(A):
                a = str(liste2[i])
                b = str(liste1[i])
                text +="{} - {}\n".format(a,b)
            self.yazi_alani.setText(text)
        except:
            self.yazi_alani.setText("Please try another IMDB-URL or enter the entries as in the example ")
app = QApplication(sys.argv)
imdb = IMDB()
sys.exit(app.exec_())


#Uygulamanın diğer kaynaklardaki işleyişi hankkında tekrardan bir çalışma yap.