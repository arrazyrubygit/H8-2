import bentuk3D as _3D

ulang = "Y"
while ulang=="Y" or ulang=="y":
    print("Perhitungan 3 dimensi")
    print("1. balok")
    print("2. kubus")
    print("3. tabung")

    pilihan = int(input("Masukan pilihan anda: "))

    if pilihan==1:
        _3D.balok()

    elif pilihan==2:
        _3D.kubus()

    elif pilihan==3:
        _3D.tabung()

    else:
        print("Pilihan yang anda masukan salah! ")

    ulang = input("Apakah ingin input ulang? (Y/N): ")

    if ulang == "N" or ulang == "n" :
        print("Program selesai")
        break
    elif ulang=="Y" or ulang=="y":
        continue
    else:
        break