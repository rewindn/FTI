create table pasien (
    no_pasien VARCHAR(15) PRIMARY KEY,
    nama VARCHAR(15),
    no_kamar VARCHAR(20),
    usia VARCHAR(12),
    tgl_lahir VARCHAR(12));

ALTER TABLE pasien Modify tgl_lahir Date;

ALTER TABLE pasien DROP PRIMARY KEY;

INSERT INTO `pasien_51422041`(`no_pasien`, `nama`, `no_kamar`, `usia`, `tgl_lahir`) VALUES 
('123','Ridho','12','20','12/1/1992'),('125','Sania','13','21','13/1/1991'),("126",'Zaki','12','20','14/1/1991'),('127','Mulyadi','12','19','16/1/1991'),('128','Ruth','15','20','17/1/1991')
