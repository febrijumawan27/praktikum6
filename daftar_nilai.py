daftarnilai={}

def tambah_data(nama, nim, tugas,uts,uas):
	akhir = round((tugas)*30/100+(uts)*35/100+(uas)*35/100)
	daftarnilai[nama]=nim,tugas,uts,uas,akhir

def ubah_data(nama):
	if nama in daftarnilai.keys():
		del daftarnilai[nama]
		print("\n===Masukan Pembaruan Data===")
		from view.input_nilai import input_data
		input_data()
	else:
		print("=============================================")
		print("| Daftar Nilai {} tidak ditemukan |".format(nama))
		print("=============================================")

def cari_data():
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

def hapus_data(nama):
	if nama in daftarnilai.keys():
		del daftarnilai[nama]
		print("Daftar Nilai {} berhasil dihapus".format(nama))
		return True
	else:
		print("===========================")
		print("| Daftar Nilai {} tidak ditemukan |".format(nama))
		print("===========================")
		return False