#pertama
"""for i in range(1,9):
    if i == 5:
        #break
        continue
    print(i)
else : 
    print("loop selesai")"""

#kedua
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))
try :
    c=a/b
    print(c)
except:
    print("terjadi error")
finally:
    print("kode selanjutnya")