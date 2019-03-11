class Mahasiswa(object):
    """Class yang dibangun ari class manusia."""
    def __init__(self, nama, nim, kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal=kota
        self.uangSaku=us
    def __str__(self):
        s = self.nama + ',NIM '+ str(self.nim) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s," Sambil velajar.")
        self.keadaan= "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self,stringbaru):
        self.kotaTinggal = stringbaru

    def tambahUangSaku(self,tambah):
        self.uangSaku += tambah

    listKuliah=[]
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
