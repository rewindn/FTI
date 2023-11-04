#include <stdio.h>
#include <stdlib.h>

struct simpul {
    int data;
    struct simpul *rantai;
};

int main() {
   struct simpul *head = (struct simpul *)malloc(sizeof(struct simpul));
head->data = 514;
head->rantai = NULL;

struct simpul *record = (struct simpul *)malloc(sizeof(struct simpul));
record->data = 220;
record->rantai = NULL;
head->rantai = record;

record = (struct simpul *)malloc(sizeof(struct simpul));
record->data = 41;
record->rantai = NULL;
head->rantai->rantai = record;


    int c;
    printf("\n================================================\n"
           "            PROGRAM LINKED LIST\n"
           "================================================\n\n");
    printf("1. Hitung Simpul");
    printf("\n2. Cetak Data");
    printf("\n================================================\n");

    while (1) { 
        printf("\nMasukkan Pilihan (1/2, or any other number to exit): ");
        scanf("%d", &c);

        if (c == 1) {
            int hitung = 0;
            struct simpul *tunjuk = head;
            while (tunjuk != NULL) {
                hitung++;
                tunjuk = tunjuk->rantai;
            }
            printf("\nJumlah Data = %d", hitung);
        } else if (c == 2) {
            struct simpul *tunjuk = head;
            if (tunjuk == NULL) {
                printf("Linked list Kosong");
            } else {
                while (tunjuk != NULL) {
                    printf("\nData pada linked List adalah %d ", tunjuk->data);
                    tunjuk = tunjuk->rantai;
                }
            }
        } else {
            printf("Exiting the program.\n");
            break; 
        }
    }

    struct simpul *current = head;
    while (current != NULL) {
        struct simpul *next = current->rantai;
        free(current);
        current = next;
    }

    return 0;
}
