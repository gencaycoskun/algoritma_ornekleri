"""
adim1: Basla
adim2: yarıcapi gir
adim3: pi sayısını 3.14 al
adim4: yarıcapin karesini alıp pi ile çarp ve alan değişkenine ata
adim5: yarıçapla pi'yi çarpıp 2 katını al ve çevre değişkenine ata
adim6: çevre ve alan'ı yazdır
adim7: bitir

"""

yaricap = float(input("Yarıçapı giriniz: "))
pi = 3.14
cevre = 2 * pi * yaricap
alan = pi * yaricap**2

print("Alan : ",alan)
print("Çevre : ",cevre)

