class Mahasiswa(object):
    """Class yang dibangun ari class manusia."""
    def __init__(self):
        self.nama = input("Nama   : ")
        self.nim = input("Nim   : ")
        self.kotaTinggal= input("Kota Tinggal   : ")
        self.uangSaku= input("Uang Saku   : ")
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

    #2a
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    #2b
    def perbaruiKotaTinggal(self,stringbaru):
        self.kotaTinggal = stringbaru

    #2c
    def tambahUangSaku(self,tambah):
        self.uangSaku += tambah
