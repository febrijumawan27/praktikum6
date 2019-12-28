from model.daftar_nilai import daftarnilai

def menu():
    print("==============Program Input Nilai Mahasiswa================")
    print("===========================================================")
    print("[ (T)ambah, (L)ihat, (U)bah, (H)apus, (Cari), (K)eluar ] : ")

def lihat_data():
    if daftarnilai.items():
        print("Lihat Daftar Nilai Mahasiswa")
        print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
        print("=================================================================")
        print("| No |       NAMA       |    NIM    | Tugas | UTS | UAS | Akhir |")
        print("=================================================================")
        i = 0
        for x in daftarnilai.items():
            i += 1
            print("| {6:2d} | {0:16s} | {1:9} | {2:5} | {3:3} | {4:3} | {5:2.2f} |" \
                  .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("=================================================================")
        print("")
    else:
        print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
        print("=================================================================")
        print("| No |       NAMA       |    NIM    | Tugas | UTS | UAS | Akhir |")
        print("=================================================================")
        print("|                  Tidak Ada Daftar Nilai                       |")
        print("=================================================================")
        print("")

def salah():
    print("")
    print("Pilih menu yang tersedia")
    print("")

def hasil_pencarian():
    print("Cari Daftar Nilai Mahasiswa")
    nama = input("Nama Mahasiswa : ")
    if nama in daftarnilai.keys():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("====================================================================================================")
        print("Daftar Nilai {0} adalah ('Nim',Tugas,UTS,UAS,Akhir) => {1}" \
              .format(nama, daftarnilai[nama]))
        print("====================================================================================================")
        print("")
    else:
        print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
        print("=================================================================")
        print("               Daftar Nilai {0} tidak ada                      " \
              .format(nama))
        print("=================================================================")
        print("")