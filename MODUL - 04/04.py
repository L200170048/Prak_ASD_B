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
    def cariuangkecil250k(self):
        terkecil = 250000
        d = []
        for i in self:
            if i.uangSaku < terkecil:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        for i in d:
            print (i)

c = buatArray()
c[0] = MhsTIF('Ika',10,'Sukoharjo',250002)
c[1] = MhsTIF('Eka',51,'solo',2000)
c[2] = MhsTIF('Eko',2,'pantai',22000)
c[3] = MhsTIF('Jona',18,'palung',252000)
c[4] = MhsTIF('Jono',4,'jambi',252100)
c[5] = MhsTIF('Bowo',31,'serang',260000)
c[6] = MhsTIF('Sopo',10,'klaten',2000)
c[7] = MhsTIF('Jarwo',5,'aceh',2524000)
c[8] = MhsTIF('Adit',23,'klaten',2223000)
c[9] = MhsTIF('Denis',64,'baru',2403600)
c[10] = MhsTIF('Shiva',29,'ambon',2445000)

#pengujian nomer 3
print ("Mahasiswa dengan uang saku kurang dari 250.000 adalah :")
c.cariuangkecil250k()
