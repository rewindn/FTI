package main

import "fmt"

// Lengkapilah program berikut sehingga dapat berjalan dengan baik!
 
func deretAngka() (int,int,int) {
    return 5, 2, 1
}
 
func main() {
    angka1, angka2, angka3 := deretAngka()
    
    penjumlahan := angka1 + angka2 + angka3
    pengurangan := angka1 - angka2 - angka3
 
    fmt.Println("Hasil dari penjumlahan adalah ", penjumlahan)
    fmt.Println("Hasil dari pengurangan adalah ", pengurangan)
}

//Muhammad Faris Rasyid Raharjo