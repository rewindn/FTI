import string
import openpyxl
import pandas

openpyxl
pandas
file = open("file.txt","r")
isi = file.readline()


file.close()

file2 = open("file.txt","w")

nama = input("masukan nama :")
kelas = input("masukan kelas :")

teks = str("nama : ",nama,"\nnumur:",kelas,"\n")
print(teks)

