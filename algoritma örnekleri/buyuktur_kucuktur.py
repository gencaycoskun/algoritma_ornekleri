"""
adim1: Basla
adim2: Birinci sayıyı gir (a)
adim3: İkinci sayıyı gir (b)
adim4: eğer a<b ise "Birinci sayı ikinci sayıdan küçüktür" yazdır ve adim7'ye git
adim5: eğer a>b ise "Birinci sayı ikinci sayıdan büyüktür" yazdır ve adim7'ye git
adim6: eğer a=b ise "Birinci sayı ikinci sayıya eşittir" yazdır
adim7: bitir

"""

sayi1 = (input("Birinci sayıyı giriniz : "))
sayi2 = (input("İkinci sayıyı giriniz : "))
if(sayi1<sayi2):
    print("Birinci sayı ikinci sayıdan küçüktür ")
if(sayi1>sayi2):
    print("Birinci sayı ikinci sayıdan büyüktür ")
if(sayi1==sayi2):
    print("Birinci sayı ikinci sayıya eşittir ")