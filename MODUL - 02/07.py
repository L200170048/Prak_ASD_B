import LatOOP4            # Atau apapun file-nya yang kamu buat tadi

class MhsTIF(LatOOP4.Mahasiswa):    # perhatikan class induknya : Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool.')

# Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?

#Metode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
#Karena MhsTIF yang merupakan anak class dari Mahasiswa, sedangkan Mahasiswa itu sendiri merupakan anak kelas dari kelas Manusia
#Serta pada kelas MhsTIF itu juga mengandung metode milik MhsTIF itu sendiri
#Jadi MhsTIF mewarisi sifat Manusia dan Mahasiswa
