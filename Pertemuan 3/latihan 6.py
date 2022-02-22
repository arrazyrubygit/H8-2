def segiempat(panjang, lebar):
    "Fungsi menghitung segi empat"
    keliling_segiempat = 2*panjang + 2*lebar
    luas_segiempat = panjang *lebar
    print("Panjang segi empat - ", panjang)
    print("Lebar segi empat - ", lebar)
    print("Keliling segi empat - ", keliling_segiempat)
    print("Luas segi empat - ", luas_segiempat)

def segitiga(alas, tinggi):
    luas_segitiga = (alas*tinggi) / 2
    print("alas segitiga : ", alas)
    print("tinggi segitiga : ", tinggi)
    print("Luas segitiga : ", luas_segitiga)

print("Perhitungan 2 dimensi")
print("1. Segiempat")
print("2. Segitiga")

pilihan = int(input("Masukan pilihan anda: "))

if pilihan==1:
    p=int(input("Masukan nilai panjang: "))
    l=int(input("Masukan nilai lebar: "))
    segiempat(p,l)

elif pilihan==2:
    a=int(input("Masukkan nilai alas: "))
    t=int(input("Masukkan nilai tinggi: "))
    segitiga(a,t)

else:
    print("pilihan anda salah")
