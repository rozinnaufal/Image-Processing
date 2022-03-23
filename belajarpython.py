#a = 10, a adalah variabel dengan nilai 10
"""tipe data : angka satuan yang nggak ada 
komanya integer"""
data_integer = 11
print ('data :', data_integer)
print ('--bertipe', type(data_integer))

# tipe data : angka dengan koma (float)
data_float = 1.5
print ("data :", data_float)
print ("--bertipe", type(data_float))

#tipe data : kumpulan karakter (string)
data_string = "ucup"
print ("data :", data_string)
print ("bertipe", type(data_string))

#tipe data : biner true or false (boolean)
data_bool = True
print ("data :", data_bool)
print ("bertipe", type(data_bool))

#tipe data khusus 
#bilangan kompleks
data_complex = complex(5,6)
print ("data :", data_complex)
print ("bertipe", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.6)
print ("data :", data_c_double)
print ("bertipe", type(data_c_double))

#casting tipe data 
#merubah dari satu tipe ke tipe lainnya
#tipe data = int, float, str, bool
data_int = 9;
print("data =", data_int,"tipe data =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))#akan false jika nilainya 0

#input user
data = input("masukkan data : ")

print("data =", data, ",type =", type(data))

#jika kita ingin mengambil int, maka
angka_float = float(input("masukkan angka :"))
angka_int = int(input("masukkan angka :"))

print("data = ", angka_float, ",type = ",(angka_float))
print("data = ", angka_int, ",type = ",(angka_int))

"""#bagaimana dengan boolean 
biner = bool(int(input("masukkan nilai boolean :")))

print("data =", biner,",type =",type(biner))"""

print("====Operasi Aritmatika====")
v = 10
y = 7

print("====Operasi Tambah====")
hasil = v + y
print(v,"+",y,"=",hasil)

print("====Operasi Pengurangan====")
hasil = v - y
print(v,"-",y,"=",hasil)

print("====Operasi Perkalian====")
hasil = v * y
print(v,"*",y,"=",hasil)

print("====Operasi Pembagian====")
hasil = v / y
print(v,"/",y,"=",hasil)

#pangkat
print("====Operasi Eksponensial====")
hasil = v ** y
print(v,"**",y,"=",hasil)

#mencari sisa pembagian
print("====Operasi Modulus====")
hasil = v % y
print(v,"%",y,"=",hasil)

#membulatkan Pembagian ke bawah
print("====Operasi Floor Division====")
hasil = v // y
print(v,"//",y,"=",hasil)

#Prioritas Operasi, Operational Precedence
#pertama dalam kurung, eksponen, perkalian, pertambahan
f = 1
g = 2
h = 1

hasil_op = f ** g * h - f + 1 // g % h
print(f, "**", g ,"*", h ,"-", f ,"+", 1 ,"//", g ,"%", h, "=", hasil_op)

#latihan konversi satuan temperature
#program konversi celcius ke satuan lain
print("\n===Program Konversi Temperature===\n")

#Program Celcius
celcius = float(input('masukkan nilai suhu dalam celcius:'))
print("suhu adalah :", celcius, "celcius")

#Program Fahrenheit
fahrenheit = ((9/5) * celcius) +32
print("suhu dalam fahrenheit :", fahrenheit, "fahrenheit")

#Program Reamur
reamur = (4/5) * celcius
print("suhu dala reamur :", reamur, "reamur")

#program kelvin
kelvin = celcius + 273
print("suhu dalam kelvin :", kelvin, "kelvin")

#Operasi Komparasi
