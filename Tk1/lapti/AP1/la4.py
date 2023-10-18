from laFunction import *
pilih = 1
while pilih != '6' :
    try :
        #Program Utama
        print ("-------------------------------------------")
        print ("   Selamat Datang di Menu Pilihan Fungsi   ")
        print ("-------------------------------------------")
        menu()
        pilih = input("Masukkan pilihan : ")

        if pilih == ('1'): List_1_dimensi()
        elif pilih == ('2'): List_2_dimensi()
        elif pilih == ('3'): Method_pada_string()
        elif pilih == ('4'): Mengkonversi_bulan()
        elif pilih == ('5'): Palindrom()
        elif pilih == ('6'): Exit()
        else : print ("Maaf pilihan anda tidak tersedia")
    
    except:
        print("ngak boleh gitu bang")