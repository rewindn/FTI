//Ahmad Zaky Humami
//50422138
//2IA27
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
      string nama, npm, kelas, matkul, produk;
      int harga, jumlah;
      double diskon = 0.25;

      cout <<"----------------------------------"<< endl;
      cout <<"   PROGRAM MAHASISWA BAHASA C++   "<< endl;
      cout <<"----------------------------------"<< endl;
      cout <<"         BIODATA MAHASISWA        "<< endl;
      cout <<"----------------------------------"<< endl;
      cout <<"Masukkan Nama : ";
      getline (cin, nama);
      cout <<"Masukkan NPM  : ";
      getline (cin, npm);
      cout <<"Masukkan Kelas: ";
      getline (cin, kelas);
      cout << endl;

      cout <<"---------------------------------"<< endl;
      cout <<"          DATA MAHASIWA          "<< endl;
      cout <<"---------------------------------"<< endl;
      cout <<"Nama      : "<<nama<<endl;
      cout <<"NPM       : "<<npm<<endl;
      cout <<"Kelas     : "<<kelas<<endl;
      cout << endl;
      
      cout <<"---------------------------------"<< endl;
      cout <<"    SERBA DISKON PRODUK 25%      "<< endl;
      cout <<"---------------------------------"<< endl;
      cout <<"Produk          : ";
      getline (cin, produk);
      cout <<"Harga Normal    : ";
      cin >>harga;
      cout << endl;

      int total = harga - (harga * diskon);

      cout <<"--------------------------------"<< endl;
      cout <<"          DATA PRODUK           "<< endl;
      cout <<"--------------------------------"<< endl;
      cout <<"Produk            : "<<produk<<endl;
      cout <<"Harga Normal      : "<<harga<<endl;
      cout <<"Total Harga Promo : "<<total<<endl;

      return 0;
}
