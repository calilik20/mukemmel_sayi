sayı = int(input("Bir sayı giriniz:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i+=1

if (toplam==sayı):
    print("Mükemmel sayı.")

else:
    print("Mükemmel sayı değildir.")