#library untuk GUI di python
import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button

jendela = tkinter.Tk()
jendela.title("KALKULATOR GUI DENGAN TKINTER")
jendela.geometry('370x200')
jendela.configure(background="#cbcbcb")

labela = Label(jendela, font=("roboto",12,"bold"),bg="#cbcbcb", text="Angka Pertama : ",anchor="center", width=20)
labela.grid(column=0, row=1)
angkaa = Entry(jendela, font=("roboto",12,"bold"),width=15)
angkaa.grid(column=1,row=1)

labelb = Label(jendela, font=("roboto",12,"bold"), bg="#cbcbcb", text="Angka Kedua : ",anchor="center", width=20)
labelb.grid(column=0, row=2)
angkab = Entry(jendela, font=("roboto",12,"bold"),width=15)
angkab.grid(column=1, row=2)

labelc = Label(jendela, font=("roboto",12,"bold"), bg="#cbcbcb",text="Hasil : ",anchor="center", width=20)
labelc.grid(column=0, row=3)

hasil = Label(jendela, font=("roboto",12,"bold"), bg="#b0a6a6",text="0",anchor="center", width=15)
hasil.grid(column=1, row=3)

def penjumlahan():
    hasil.configure(text=(int(angkaa.get())+int(angkab.get())))

def pengurangan():
    hasil.configure(text=(int(angkaa.get())-int(angkab.get())))

def perkalian():
    hasil.configure(text=(int(angkaa.get())*int(angkab.get())))

def pembagian():
    hasil.configure(text=(int(angkaa.get())/int(angkab.get())))

tombol = Button(jendela, font=("roboto",10,"bold"), cursor="circle", bg="#86b7bc", text="TAMBAH", command=penjumlahan)
tombol.grid(column=0, row=4)

tombol = Button(jendela, font=("roboto",10,"bold"), cursor="circle", bg="#86b7bc", text="KURANG", command=pengurangan)
tombol.grid(column=0, row=5)

tombol = Button(jendela, font=("roboto",10,"bold"), cursor="circle", bg="#86b7bc", text="KALI", command=perkalian)
tombol.grid(column=1, row=4)

tombol = Button(jendela, font=("roboto",10,"bold"), cursor="circle", bg="#86b7bc", text="BAGI", command=pembagian)
tombol.grid(column=1, row=5)

jendela.mainloop()