#program operasi aritmetika
print("==========PROGRAM ARITMETIKA==========")
pilih = 1
while pilih :
    print("---------------")
    print("Pilihan Operasi Aritmetika\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Keluar")
    pilih = int(input("Silahkan masukkan pilihan : "))
    if(pilih == 1):
        print("Pertambahan")
        bilPertama = int(input("Silahkan masukkan Bilangan Pertama : "))
        bilKedua = int(input("Silahkan masukkan Bilangan Kedua   : "))
        hasil = bilPertama+bilKedua
        print("hasilnya adalah = ",hasil)
    elif(pilih == 2):
        print("Pengurangan")
        bilPertama = int(input("Silahkan masukkan Bilangan Pertama : "))
        bilKedua = int(input("Silahkan masukkan Bilangan Kedua   : "))
        hasil = bilPertama-bilKedua
        print("hasilnya adalah = ",hasil)
    elif(pilih == 3):
        print("Perkalian")
        bilPertama = int(input("Silahkan masukkan Bilangan Pertama : "))
        bilKedua = int(input("Silahkan masukkan Bilangan Kedua   : "))
        hasil = bilPertama*bilKedua
        print("hasilnya adalah = ",hasil)
    elif(pilih == 4):
        print("Pembagian")
        bilPertama = int(input("Silahkan masukkan Bilangan Pertama : "))
        bilKedua = int(input("Silahkan masukkan Bilangan Kedua   : "))
        hasil = bilPertama/bilKedua
        print("hasilnya adalah = ",hasil)
    elif(pilih == 5):
        exit(pilih)
    else:
        print("pilihan tidak tersedia")