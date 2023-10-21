/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
// Online C compiler to run C program online
#include <stdio.h>

typedef struct{
    char *nama;
    char *npm;
    char *kelas;
    int nilai;
    
}mahasiswa;

int main()
{
mahasiswa mhs;

mhs.nama    = "Muhammad Faris Rasyid Raharjo";
mhs.npm     = "51422041";
mhs.kelas   = "2IA22";
mhs.nilai   = 99;

printf("%s \n", mhs.nama);
printf("%s \n", mhs.npm);
printf("%s \n", mhs.kelas);
printf("%i", mhs.nilai);

}
