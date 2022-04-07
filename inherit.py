class Orang():
  def __init__(self, nama, jenisK, alamat, status, tinggi, berat):
    self.nama = nama
    self.jenisK = jenisK
    self.alamat = alamat
    self.status = status
    self.tinggi = tinggi
    self.berat = berat
  def cek_id_orang(self):
    self.bmi = self.berat/(self.tinggi**2)
    print('\nnama     : '+self.nama,'\njenKel   : '+self.jenisK,'\nalamat   : '+self.alamat,'\nstatus   : '+self.status,"\ntinggi   : ",self.tinggi,"\nberat    : ",self.berat)
    print("BMI      : ",round(self.bmi, 2))
    if 18.5 <= self.bmi <= 22.9 :
      print("Normal")
    # Jika nilai BMI berada lebih dari 22.9
    elif self.bmi > 22.9 :
      print("Obesitas")
    # Jika nilai BMI berada kurang dari 22.9
    else :
       print("Kurus")
print("****************************** PROGRAM INHERIT (BMI) ***************************")
orang1 = Orang('david','laki','sepakuan','sudah ada yang punya',1.70,55.0)
orang1.cek_id_orang() 
