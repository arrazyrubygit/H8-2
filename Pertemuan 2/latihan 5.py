#Contoh penggunaan percabangan dan pengulangan
print('Konversi Suhu')
temp = input("Ketikan temperatur yang ingin dikonversi, eg. 45F, 120C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result1 = int(round((9 * degree) / 5 + 32))
    result2 = int(round(degree + 273))
    result3 = int(round((4 * degree) / 5))
    print("%s in Fahrenheit  is %s in Kelvin and %s in Reamur." % (result1, result2, result3))
elif i_convertion == "F":
    result1 = int(round((degree - 32) * 5 / 9))
    result2 = int(round((degree - 32) * 5 / 9 +273))
    result3 = int(round((degree - 32) * 4 / 9))
    print("%s in Celcius  is %s in Kelvin and %s in Reamur." % (result1, result2, result3))

elif i_convertion == "K":
    result1 = int(round(degree - 273))
    result2 = int(round((degree - 273) * 9 / 5 + 32))
    result3 = int(round((degree - 273) * 4 / 5))
    print("%s in Celcius  is %s in Fahrenheit and %s in Reamur." % (result1, result2, result3))

elif i_convertion == "R":
    result1 = int(round((degree * 5) / 4))
    result2 = int(round((degree * 9) / 4 + 32))
    result3 = int(round((degree - 5) / 4 + 273))
    print("%s in Celcius  is %s in Fahrenheit and %s in Kelvin." % (result1, result2, result3))

else:
    print("Masukan input yang benar")

