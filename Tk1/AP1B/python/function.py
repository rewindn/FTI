bilangan = int(input("masukan bilangan : "))

pangkat = int(input("masukan bilangan : "))

def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print("Hasil =",hasil)