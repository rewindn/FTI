package main

import "fmt"
 
func main() {
    var nama = map[string]int{
        "pert6": 7523,
        // Tambahkan key = nama dan value = NPM
        "faris": 5142241,
    }
 
    fmt.Println(len(nama))
    fmt.Println("Sebelum dihapus ", nama)
 
    // Kerjakan Di Sini
    delete(nama,"pert6")
    fmt.Println(len(nama))
    fmt.Println("Sesudah dihapus", nama)
}
//Muhammad Faris Rasyid Raharjo