from PySide2 import QtWidgets
import inistack
import projek

queee = [] #variabel queee yang menyimpan data dalam bentuk list 
class PriorityQueue(object): # membuat kelas PriorityQueue
    def __init__(self):
        self.qlist = queee 

    def __len__(self):
        return len(queee)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self,na, id, al, ant): #methode untuk menyimpan data ke list queee
        entry = _PriorityQEntry(na, id, al, ant) 
        self.qlist.append(entry)

    def dequeue(self): #methode untuk mengeluarkan data dari list
        n = []
        for i in self.qlist:
            n.append(i.antrian)
        print (queee.pop(n.index(min(n))).nama)

class _PriorityQEntry(object):
    def __init__(self,na, id, al, ant):
        self.nama = na
        self.id = id
        self.alamat = al
        self.antrian = ant

class cucubude(projek.Ui_daftar_pengunjung, QtWidgets.QMainWindow): #kelas untuk me-load UI dari PySide2
    def __init__(self):
        super(cucubude, self).__init__() 
        self.setupUi(self)
        
        self.btn_tambah.clicked.connect(self.menambahkan)
        self.btn_tampilkan.clicked.connect(self.menampilkan)
        self.btn_urut.clicked.connect(self.mengurutkan)
        self.btn_cari.clicked.connect(self.mencari)
        self.btn_queue.clicked.connect(self.antrian)
        self.btn_stack.clicked.connect(self.stackk)

    def menambahkan(self):
            #mengambil nilai inputan dari GUI dan disimpan ke variabel (getText) untuk disimpan di queee
        na = self.txt_nama.text()
        id = self.txt_id.text()
        al = self.txt_alamat.text()
        ant = self.txt_antrian.text()

            #menambhakan ke list queee
        klm = PriorityQueue() #memanggil kelas PriorityQueue
        klm.enqueue(na, id, al, ant) #menjalankan methode enqueue pada kelas PriorityQueue


    def menampilkan(self):
            #membersihkan tabel
        self.tree_data.clear()

            #menampilkan isi list ke dalam tabel
        for q in queee:
            namaa = (q.nama)
            id = (q.id)
            alamatt = (q.alamat)
            antriann = (q.antrian)

            item = QtWidgets.QTreeWidgetItem(self.tree_data)
            item.setText(0, str(namaa))
            item.setText(1, 'D'+str(id))
            item.setText(2, str(alamatt))
            item.setText(3, str(antriann))

    def mengurutkan(self):
        self.tree_hasil.clear() #menghapus isi tabel

        def swap(O, p, q):
            temp = O[p]
            O[p] = O[q]
            O[q] = temp

        def bubblesort(O):
            
            n = len(O)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if O[j].id > O[j + 1].id:
                        swap(O, j, j + 1)

        def tampilkan(O):
            for b in queee:
                nam = (b.nama)
                id = (b.id)
                al = (b.alamat)
                ant = (b.antrian)

                item = QtWidgets.QTreeWidgetItem(self.tree_hasil)
                item.setText(0, str(nam))
                item.setText(1, 'D'+str(id))
                item.setText(2, str(al))
                item.setText(3, str(ant))

        bubblesort(queee)
        tampilkan(queee)

    def mencari(self):
        self.tree_hasil.clear()
        
        target = self.txt_cari.text()   #mencari
        for i in queee:                 #data
            if i.id == target:          #dari list

                #menampilkan data ke tabel
                nam = (i.nama)
                id = (i.id)
                al = (i.alamat)
                ant = (i.antrian)

                item = QtWidgets.QTreeWidgetItem(self.tree_hasil)
                item.setText(0, str(nam))
                item.setText(1, 'D' + str(id))
                item.setText(2, str(al))
                item.setText(3, str(ant))

    def stackk(self):
        idnya = self.txt_stack.text()
        hasill = inistack.cetakHexa(int(idnya))
        self.txt_hasilstack.setText(hasill)

    def antrian(self):
        self.tree_queue.clear()
        for q in queee:
            namaa = (q.nama)
            id = (q.id)
            alamatt = (q.alamat)

            item = QtWidgets.QTreeWidgetItem(self.tree_queue)
            item.setText(0, str(namaa))
            item.setText(1, 'D'+str(id))
            item.setText(2, str(alamatt))
        keluarr = PriorityQueue()
        keluarr.dequeue()

      

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = cucubude()
    qt_app.show()
    app.exec_()
