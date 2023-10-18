panjang = int(input('Masukkan panjang deret:'))

def fibonacci (n):
  if n < 1:
    return [n]
  
  SebelumN = fibonacci(n - 1)


  angka1 = SebelumN[-2] if len(SebelumN) > 2 else 0
  angka2 = SebelumN[-1] if len(SebelumN) > 2 else 1
  
  return SebelumN + [angka1 + angka2]


# kita kurangin satu agar tidak kelebihan :D
print(fibonacci(panjang - 1))
