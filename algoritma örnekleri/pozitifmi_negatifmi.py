"""
adim1: Basla
adim2: a sayisini gir
adim3: Eğer sayı 0'dan büyükse "Pozitif Sayıdır" yazdır ve adim6'ya geç
adim4: Eğer sayı 0'dan küçükse "Negatif Sayıdır" yazdır ve adim6'ya geç
adim5: Eğer sayı 0'a eşitse "Sayı Sıfırdır" yazdır ve adım6'ya geç
adim6: Bitir

"""

sayi = input("Bir sayı giriniz : ")
if(int(sayi)>0):
    print(sayi + " sayısı Pozitiftir ")
if(int(sayi<0)):
    print(sayi + "sayısı Negatiftir ")
if(int(sayi=0)):
    print(sayi + " sayısı Sıfırdır ")
    