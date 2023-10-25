#include <iostream>
using namespace std;
int pilih, bks;
void film(int pilih)
{

    cout << "--------------------------Daftar Film Hari Ini------------------------------" << endl;
    cout << "1. Guardian Of Tanah Abang" << endl;
    cout << "2. Laki Laki Besi" << endl;
    cout << "3. Petualangan Slenderina" << endl;
    cout << "4. Pamali Pocong Beranak Tuyul" << endl;
    cout << "5. Jokowi Shippuden" << endl;
    cout << "\n";
}
int main()

{

    cout << "--------------------------Daftar Film Hari Ini------------------------------" << endl;
    cout << "1. XXI" << endl;
    cout << "1. CGV" << endl;
    cout << "Masukan Film : ";
    cin >> bks;

    if (bks == 1)
    {
        cout << "Anda Memesan Tiket Dati XXI";
        film(pilih);
        cout << "Pilih Film :";
        cin >> pilih;
    }

    else if (bks == 2)
    {
        cout << "Anda Memesan Tiket Dati CGV";
        film(pilih);
        cout << "Pilih Film :";
        cin >> pilih;
    }
}