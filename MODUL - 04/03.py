class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

class buatArray(object):
    #membuat list
    internalData = 11*[None]

    #mengambil data di list
    def __getitem__(self, item):
        return self.internalData[item]

    #mengatur posisi data dan index-nya pada list
    def __setitem__(self, key, value):
        self.internalData[key] = value

    #03
    def cariuangkecil(self):
        terkecil = self[0].uangSaku
        d = []
        for i in self:
            if i.uangSaku < terkecil:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        return d

c = buatArray()
c[0] = MhsTIF('Ika',10,'Sukoharjo',2700)
c[1] = MhsTIF('Eka',51,'solo',2000)
c[2] = MhsTIF('Eko',2,'pantai',22000)
c[3] = MhsTIF('Jona',18,'palung',222000)
c[4] = MhsTIF('Jono',4,'jambi',222000)
c[5] = MhsTIF('Bowo',31,'serang',260000)
c[6] = MhsTIF('Sopo',10,'klaten',2000)
c[7] = MhsTIF('Jarwo',5,'aceh',222000)
c[8] = MhsTIF('Adit',23,'klaten',223000)
c[9] = MhsTIF('Denis',64,'baru',240600)
c[10] = MhsTIF('Shiva',29,'ambon',245000)

#pengujian nomer 3
print ("Nomer 3")
print("Uang saku yang terkecil adalah ", c.cariuangkecil())
