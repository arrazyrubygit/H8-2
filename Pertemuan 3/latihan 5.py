print("Perhitungan 2 dimensi")
print("1. Segi Empat")
print("2. Segitiga:")
print("3. Persegi: ")
print("4. Lingkaran ")

ulang = "Y"

while ulang =="Y":
    tipe_perhitungan =input("Masukan tipe perhitungan: ")

    if tipe_perhitungan == "1":
        panjang = input("Masukan variable panjang: ")
        lebar = input("Masukan variable lebar: ")
        keliling_segiempat = 2*int(panjang) + 2*int(lebar)
        luas_segiempat = int(panjang) * int(lebar)
        print("Panjang segi empat - ", panjang)
        print("Lebar segi empat - ", lebar)
        print("Keliling segi empat - ", keliling_segiempat)
        print("Luas segi empat - ", luas_segiempat)

    elif tipe_perhitungan == "2":
        alas = input("Masukan variable alas: ")
        tinggi = input("Masukan variable tinggi: ")
        luas_segitiga = (int(alas) * int(tinggi))/2
        print("alas segitiga - ", alas)
        print("tinggi segitiga - ", tinggi)
        print("Luas segi empat - ", luas_segitiga)

    elif tipe_perhitungan == "3":
        sisi = input("Masukan variable sisi: ")
        luas_persegi = int(sisi)*int(sisi)
        keliling_persegi = int(sisi) * 4
        print("luas persegi - ", luas_persegi)
        print("Keliling persegi - ", keliling_persegi)

    elif tipe_perhitungan == "4":
        pie = 3.14
        jari_jari = int(input("Masukan jari-jari: "))
        luas_lingkaran = float(pie) * jari_jari * 2
        keliling_lingkaran = float(pie)

    else:
        print("Pilihan yang anda masukan salah! ")

    ulang = input("Apakah ingin input ulang? (Y/N): ")

else:
    print("Program selesai")