section .data
    nilA db 55
    nilB db 45

    kat0 db 'nilai a lebih kecil dari nilai b\%', 0
    kat1 db 'nilai a sama dengan nilai b%%', 0
    kat2 db 'nilai a lebih besar dari nilai b\%', 0

section .text
global main

main:
    mov al, byte [nilA]
    mov bl, byte [nilB]

    cmp al, bl
    jl Akecil
    je sama
    ja Abesar

Akecil:
    mov edx, kat0
    jmp cetak

sama:
    mov edx, kat1
    jmp cetak

Abesar:
    mov edx, kat2
    jmp cetak

cetak:
    mov eax, 4       ; Syscall untuk menampilkan string
    mov ebx, 1       ; File descriptor (stdout)
    mov ecx, edx     ; Alamat string
    mov edx, 30      ; Panjang string
    int 0x80

    mov eax, 1       ; Syscall untuk exit
    int 0x80
