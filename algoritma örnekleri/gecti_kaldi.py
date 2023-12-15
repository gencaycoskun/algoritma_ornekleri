"""
adim1: Basla
adim2: vize ve final degiskenlerini ata
adim3: vize ve final ağırlıklarını ata // ağırlıklar da dışarıdan girilsin istedim.
adim4: vize ile vize ağırlığını, final ile final ağırlığını çarpıp topladıktan sonra sonucu ortalama değişkenine ata
adim5: ortalamayı yazdır
adim6: Eğer ortalama 50'den büyük eşitse  "Dersten Geçtiniz ! " yazdır ve adim8'e git
adim7: değilse " Dersten Kaldınız. " yazdır
adim8: bitir

"""

vize = input("Vize notunuzu giriniz :")
final = input("Final notunuzu giriniz:")
vizeAgirligi = float(input("Vize ağirligini giriniz :"))
finalAgirligi = float(input("Final ağirligini giriniz : "))
ortalama = vize * vizeAgirligi + final * finalAgirligi
if(ortalama >=50):
    print("Dersten Geçtiniz ! ")
else:
    print("Dersten Kaldınız. ")
