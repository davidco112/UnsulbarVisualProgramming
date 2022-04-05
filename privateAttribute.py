class Identitas():
    namaJurusan = "Informatika"
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim        

na = Identitas("David", "D0219003")
print("Nama     : "+na.nama)
print("Nim      : "+na.nim)
print("Jurusan  : "+na.namaJurusan)