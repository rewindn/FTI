

#include <iostream>
using namespace std;

int main()
{

    /* code */

    int a = 5;
    for (int i = 1; i < a; i++)
    {
        cout << "*" << endl;
        /* code */
        for (int x = 0; x < i; x++)
        {
            cout << "*";
            cout << "2";
            /* code */
        }
    }

    // for (int j = 1; j < a; j++)
    // {
    //     cout << "*" << endl;
    //     /* code */
    //     for (int x = 0; x < j; x++)
    //     {
    //         cout << "2";
    //         /* code */
    //     }
    // }

    return 0;
}
