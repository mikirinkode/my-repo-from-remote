
class mahasiswa:
    def __init__(self, nama_depan, nama_belakang, npm, prodi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.prodi = prodi
        self.npm = npm

    def cetak_biodata(self):
        print("Name :", self.nama_depan, self.nama_belakang)
        print("NPM :", self.npm)
        print("Program Studi :", self.prodi)

mahasiswa1 = mahasiswa("Muhammad", "Wafa", 2015061057, "Teknik Informatik")
mahasiswa1.cetak_biodata()