import os
def dosyaYaz(veri):
    f = open("metin.txt", "a+")
    f.write(veri+"\n")
    f.close()

def dosyaOku():
    f = open("metin.txt", "r")
    print(f.read())
    f.close()

def dosyaSil(belge):
    os.remove(belge)

txtEkle = input("Txt Yazılacak Veri : ")
dosyaYaz(txtEkle)

dosyaOku()

sil = input("Silinecek Belge İsim : ")
dosyaSil(sil)
import os
def dosyaYaz(veri):
    f = open("metin.txt", "a+")
    f.write(veri+"\n")
    f.close()

def dosyaOku():
    f = open("metin.txt", "r")
    print(f.read())
    f.close()

def dosyaSil(belge):
    os.remove(belge)

txtEkle = input("Txt Yazılacak Veri : ")
dosyaYaz(txtEkle)

dosyaOku()

sil = input("Silinecek Belge İsim : ")
dosyaSil(sil)
