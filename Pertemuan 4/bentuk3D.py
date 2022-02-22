def balok():
    #"Fungsi menghitung balok"
    panjang=int(input("Masukan nilai panjang: "))
    lebar=int(input("Masukan nilai lebar: "))
    tinggi=int(input("Masukan nilai tinggi: "))
    keliling_balok = 4*(panjang+lebar+tinggi)
    volume_balok = panjang * lebar * tinggi
    print("Panjang balok - ", panjang)
    print("Lebar balok - ", lebar)
    print("tinggi balok- ", tinggi)
    print("Keliling balok - ", keliling_balok)
    print("volume balok - ", volume_balok)

def kubus():
    #"Fungsi menghitung kubus"
    sisi=int(input("Masukkan nilai sisi: "))
    keliling_kubus = 12 * sisi
    volume_kubus = sisi * sisi * sisi
    print("sisi kubus - ", sisi)
    print("keliling kubus - ", keliling_kubus)
    print("volume kubus - ", volume_kubus)

def tabung():
    r=int(input("Masukan nilai jari-jari: "))
    phi=float(input("Masukan nilai phi: "))
    tinggi=int(input("Masukan nilai tinggi: "))
    #"Fungsi menghitung tabung"
    keliling_alas_tabung = 2*phi*r
    volume_tabung = phi*r*r*tinggi
    luas = 2*phi*r*r
    print("Keliling alas - ", keliling_alas_tabung)
    print("volume tabung - ", volume_tabung)
    print("luas - ", luas)
