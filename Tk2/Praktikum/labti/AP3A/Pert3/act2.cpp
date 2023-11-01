#include <iostream>
using namespace std;
int main()
{
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    /* code */

    for (int i = 0; i < 3; i++)
    {
        cout << endl;
        for (int j = 0; j < 3; j++)
        {
            // cout << i;
            // cout << j << endl;
            if (j == 0)
            {
                cout << "{";
            }
            cout << " " << matrix[i][j] << " ";
            if (j == 2)
            {
                cout << "}" << endl;
            }
        }
    }

    return 0;
}
