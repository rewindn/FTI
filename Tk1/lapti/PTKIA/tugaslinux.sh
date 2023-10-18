#!/bin/bash
al=1 
while [ $al -eq 1 ]
do

echo "=======================================";
echo "            BIOSKOP MAIHARSA           ";
echo "=======================================";
echo "1. Ultraman";
echo "2. Qodrat";
echo "3. Black Panther";
echo "4. Spiderman No Way Home"
echo "5. Miracle In Cell"
echo "6. Exit";
echo "=======================================";
echo -n "Pilih Film [1-5] = ";
read pil
echo "=======================================";
case $pil in
1)
	film='Ultraman'
	echo -n "Masukkan Jumlah Tiket	    :";
	read jum
	echo "Harga 1 Tiket		:Rp.45.000,-";		
	let bayar=jum*45000
;;
2)
	film='Qodrat'
	echo -n "Masukkan Jumlah Tiket	    :";
	read jum
	echo "Harga 1 Tiket		: Rp. 50.000,-";
	let bayar=jum*55000

;;
3)
	film='Black Panther'
	echo -n "Masukkan Jumlah Tiket		:"
	read jum
	echo "Harga 1 Tiket	      	: Rp. 35.000,-";
	let bayar=jum*35000

;;
4)
	film='Spiderman No Way Home'
	echo -n "Masukkan Jumlah Tiket		:"
	read jum
	echo "Harga 1 Tiket	      	: Rp. 45.000,-";
	let bayar=jum*95000

;;
5)
	film="Miracle In Cell"
	echo -n "Masukkan Jumlah Tiket		:"
	read jum
	echo "Harga 1 Tiket	      	: Rp. 40.000,-";
	let bayar=jum*35000

;;
6)
	echo "Terima Kasih^-^"
	exit
;;
*)
	echo "Pilihan Tidak Tersedia!"; 
	exit
;;
esac

echo "***************************************";
echo "           TIKET NONTON FILM           ";
echo "***************************************";
echo "Judul Film	: $film";
echo "Jumlah Tiket	: $jum";
echo "Total Bayar	: Rp.$bayar";
echo "***************************************";

done
