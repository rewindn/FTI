#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    /* code */

    FILE *file;

    file = fopen("file_Data.txt", "w");
    int pilih;

    cout << "berapa data yang akan kamu masukan ? ";
    cin >> pilih;
    for (int i = 1; i <= pilih; i++)
    {
        /* code */
        string nama;
        cout << "Masukan Input : ";

        cin >> nama;

        fprintf(file, "%s\n", nama.c_str());
    }

    fclose(file);

    file = fopen("file_Data.txt", "r");

    char line[100];

    while (fgets(line, sizeof(line), file) != NULL)
    {
        cout << line;
    }

    fclose(file);
    return 0;
}
