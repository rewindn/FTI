#include <iostream>
using namespace std;

int main()
{
    int pilih;
    cout << "--------------------------Layout Keyboard------------------------------" << endl;
    cout << "1. Colemac Keyboard Layout" << endl;
    cout << "2. Dvorak Keyboard Layout" << endl;
    cout << "3. Qwerty Keyboard Layout" << endl;
    cout << "\n";
    cout << "Select New Layout Keyboard :";
    cin >> pilih;

    if (pilih == 1)
    {
        cout << "Anda Sedang Menggunakan Keyboard Colemac";
    }
    else if (pilih == 2)
    {
        cout << "Anda Sedang Menggunakan Keyboard Dvorak";
    }
    else if (pilih == 3)
    {
        cout << "Anda Sedang Menggunakan Keyboard Qwerty";
    }
    else
    {
        cout << "Out Of Option";
    }

    return 0;
}