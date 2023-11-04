#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node *prev;
    struct node *next;
    int data;
};

struct node *head = NULL;

void tambahDataAwal();
void tambahDataAkhir();
void tampil();

int main() {
    int pilih = 0;
    while (pilih != 9) {
        printf("\n****** Main Menu ******\n");
        printf("\nPilihlah opsi manasaja dari pilihan dibawah ini: \n");
        printf("\n******************\n");
        printf("\n1. Masukkan data di awal\n2. Masukkan data di akhir\n3. Tampilkan data");
        printf("\nMasukan Pilihan Anda: ");
        scanf("%d", &pilih);
        switch (pilih) {
        case 1:
            tambahDataAwal();
            break;
        case 2:
            tambahDataAkhir();
            break;
        case 3:
            tampil();
            break;
        default:
            printf("Tolong masukkan pilihan yang sesuai ");
        }
    }
    return 0;
}

void tambahDataAwal() {
    struct node *ptr;
    int item;
    ptr = (struct node *)malloc(sizeof(struct node));
    if (ptr == NULL) {
        printf("\nAlokasi memori gagal");
    } else {
        printf("\nMasukkan data berupa angka: ");
        scanf("%d", &item);
        ptr->data = item;
        if (head == NULL) {
            ptr->next = NULL;
            ptr->prev = NULL;
            head = ptr;
        } else {
            ptr->next = head;
            ptr->prev = NULL;
            head->prev = ptr;
            head = ptr;
        }
        printf("\nData Berhasil dimasukkan\n");
    }
}

void tambahDataAkhir() {
    struct node *ptr, *temp;
    int item;
    ptr = (struct node *)malloc(sizeof(struct node));
    if (ptr == NULL) {
        printf("\nAlokasi memori gagal");
    } else {
        printf("\nMasukkan data berupa angka: ");
        scanf("%d", &item);
        ptr->data = item;
        if (head == NULL) {
            ptr->next = NULL;
            ptr->prev = NULL;
            head = ptr;
        } else {
            temp = head;
            while (temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->prev = temp;
            ptr->next = NULL;
        }
        printf("\nData berhasil dimasukkan\n");
    }
}

void tampil() {
    struct node *ptr;
    printf("\nList: \n");
    ptr = head;
    while (ptr != NULL) {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
}