from view.view_nilai import menu, lihat_data, hasil_pencarian, salah
from view.input_nilai import input_data, ubah, hapus

while True:
    menu()
    m = input("\nPilih Menu :")
    if m.lower() == 'k':
        break

    elif m.lower() == 't':
        input_data()

    elif m.lower() == 'u':
        ubah()

    elif m.lower() == 'h':
        hapus()

    elif m.lower() == 'c':
        hasil_pencarian()

    elif m.lower() == 'l':
        lihat_data()

    else:
        salah()