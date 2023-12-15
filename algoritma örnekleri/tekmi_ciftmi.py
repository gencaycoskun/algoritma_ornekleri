"""
adim1: Basla
adim2: a sayisini gir
adim3: a sayisinin 2'ye gore modunu al ve mod degiskenine ata
adim4: a%2 = 0 ise a cift sayidir yazdir ve adim6'ya gec
adim5: a%2 != 0 ise a tek sayidir yazdir
adim6: bitir

"""
sayi = input("Bir sayı giriniz :")
if(int(sayi)%2==0):
    print("Sayı çifttir")
else:
    print("Sayı tektir")
    