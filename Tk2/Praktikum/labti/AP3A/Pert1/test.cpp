#include <iostream>
using namespace std;
int main()
{
    int angka1, angka2;
    cout << "Masukan Angka 1 : ";
    cin >> angka1;
    cout << "Masukan Angka 2 : ";
    cin >> angka2;

    cout << "------------------------------Hasil------------------------------" << endl;

    int tambah = angka1 + angka2;
    cout << angka1 << " tambah " << angka2 << " = " << tambah << endl;

    int kurang = angka1 - angka2;
    cout << angka1 << " kurang " << angka2 << " = " << kurang << endl;

    int kali = angka1 * angka2;
    cout << angka1 << " kali " << angka2 << " = " << kali << endl;

    int bagi = angka1 / angka2;
    cout << angka1 << " bagi " << angka2 << " = " << bagi << endl;

    return 0;
}