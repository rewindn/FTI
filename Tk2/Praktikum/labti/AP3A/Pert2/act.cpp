#include <iostream>
using namespace std;

int main()
{
    int pilih;
    cout << "--------------------------Daftar Film Hari Ini------------------------------" << endl;
    cout << "1. Guardian Of Tanah Abang" << endl;
    cout << "2. Laki Laki Besi" << endl;
    cout << "3. Petualangan Slenderina" << endl;
    cout << "4. Pamali Pocong Beranak Tuyul" << endl;
    cout << "5. Jokowi Shippuden" << endl;
    cout << "\n";
    cout << "Pilih Film :";
    cin >> pilih;

    switch (pilih)
    {
    case 1:
        cout << "Tiket Guardian Of Tanah Abang Tercetak Selamat Menonton" << endl;
        break;
    case 2:
        cout << "Tiket Laki Laki Besi Telah Tercetak Selamat Menonton" << endl;
        break;
    case 3:
        cout << "Tiket Petualangan Slenderina Telah Tercetak Terima Kasih" << endl;
        break;
    case 4:
        cout << "Tiket Pamali Pocong Beranak Tuyul Telah Tercetak Selamat Menonton" << endl;
        break;
    case 5:
        cout << "Tiket Jokowi Shippuden Telah Tercetak Selamat Menonton" << endl;
        break;
    default:
        cout << "tidak ada";
        break;
    }
}