def menu():
                print ("Menu Pilihan")
                print ("")
                print ("1. List 1 Dimensi")
                print ("2. List 2 Dimensi")
                print ("3. Method pada string")
                print ("4. Mengkonversi bulan")
                print ("5. Palindrom")
                print ("6. Keluar")

def List_1_dimensi () :
            batas = int(input("Masukkan Batas Anda : "))
            list = []
        
            i = 0
            while i < batas : 
                    angka = int(input('Masukkan Angka : '))
                    list.append(angka)
                    i += 1        
            print(list)


def List_2_dimensi() :
            kolom = int(input("Masukkan Batas Kolom: "))
            baris = int(input("Masukkan Batas Baris: "))
        
            list = []
            i = 0
            while i < baris :
                j = 0
                if kolom != 1:
                    list.append([])
                
                while j < kolom :        
                    angka = int(input(f'index ke - [{i}][{j}] : '))
                    if kolom == 1 :
                        list.append(angka)
                    else:
                        list[i].append(angka)
                    j += 1
                i += 1;
            print(list)

def Method_pada_string () :
    kalimat = input("masukan kalimat : ")
    print("contoh penggunaan capitalize()   : ",kalimat.capitalize())
    print("contoh penggunaan title()        : ",kalimat.title())
    print("contoh penggunaan upper()        : ",kalimat.upper())
    print("contoh penggunaan lower()        : ",kalimat.lower())
    print("contoh penggunaan casefold()     : ",kalimat.casefold())
    print("contoh penggunaan swapcase()     : ",kalimat.swapcase())
    print("contoh penggunaan split()        : ",kalimat.split())
    print("contoh penggunaan encode()       : ",kalimat.encode())

def Mengkonversi_bulan () :
                bulan =  ["tidak ada","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
                pilihan_bulan = int(input("masukan no bulan [1 - 12] : "))
                print("bulan ke",pilihan_bulan,"adalah bulan",bulan[pilihan_bulan])

def Palindrom () :
        kata = input("masukan kata Palindrom : ")
        while kata != kata[::-1]:
            print(kata,"bukan termasuk Palindrom")
            kata = input("masukan kata Palindrom : ")    
        print(kata,"termasuk Palndrom")

def Exit () :
                print ("Terimakasih ^-^")