#NESNE YONELIMLI PROGRAMLAMA

class VeriBilimci():
    print("Bu bir sınıftır")

#Sinif Ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
#Siniflarin ozelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

#siniflarin ozelliklerini degistirmek
VeriBilimci.sql = "Hayir"
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

kulter = VeriBilimci()

kulter.sql
kulter.deneyim_yili
kulter.bolum
kulter.bildigi_diller.append("Python")
kulter.bildigi_diller

zeynep = VeriBilimci()
zeynep.sql

zeynep.bildigi_diller

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

kulter = VeriBilimci()
kulter.bildigi_diller

zeynep = VeriBilimci()
zeynep.bildigi_diller

kulter.bildigi_diller.append("Python")
kulter.bildigi_diller

zeynep.bildigi_diller
zeynep.bildigi_diller.append("R")
zeynep.bildigi_diller

VeriBilimci.bildigi_diller
kulter.bolum

VeriBilimci.bolum
kulter.bolum = "istatistik"
VeriBilimci.bolum
zeynep.bolum
zeynep.bolum = "end_muh"
zeynep.bolum
kulter.bolum
VeriBilimci.bolum

#Ornek Metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)


kulter = VeriBilimci()
kulter.bildigi_diller
kulter.bolum

zeynep = VeriBilimci()
zeynep.bildigi_diller
zeynep.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R")

kulter.dil_ekle("R")
kulter.bildigi_diller

zeynep.dil_ekle("Python")
zeynep.bildigi_diller











