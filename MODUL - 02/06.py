class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
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
    def hapusKuliah(self, hapus):
        self.listKuliah.remove(hapus)

class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) \
            +'NISN      : ' + str(self.nisn) \
            +'Alamat    : ' + str(self.alamat) \
            +'Uang Saku : ' + str(self.uangSaku)
        return a
    def ambilNama(self):
        return self.nama
    def ambilNisn(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self,stringbaru):
        self.kotaTinggal = stringbaru

    def tambahUangSaku(self,tambah):
        self.uangSaku += tambah
