bilangan = int(input("masukan bilangan : "))

def faktorial(bilangan):
  if bilangan > 1:
    return bilangan * faktorial(bilangan - 1)

  return bilangan

hasil = faktorial(bilangan)
print(f'Hasil dari {bilangan}! = {hasil}')