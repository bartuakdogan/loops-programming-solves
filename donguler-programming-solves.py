
# Problem 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

# num = int(input("Bir sayı giriniz: "))
# toplam = 0

# for i in range(1,num):
#     if (num % i == 0):
#         toplam += i
# if (toplam == num):
#     print(f"Girdiğiniz sayı olan {num}, bir mükemmel sayıdır.")
# else:
#     print(f"Girdiğiniz sayı olan {num}, bir mükemmel sayı değildir.")
    

# Problem 2
# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

# Problem 3
# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
# *İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*


# for i in range(1,11):
#     print("******************")
#     for j in range(1,11):

#         print(f"{i} x {j} = {i * j}")


# Problem 4
# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
# *İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*

print("Programımızdan Çıkmak için Lütfen 'q' ya Basınız !")

toplam = 0

while True:
    sayi = input("Sayı: ")

    if (sayi == "q"):
        break
    sayi = int(sayi)
    toplam += sayi

print("Girdiğiniz Sayılar Toplamı: ", toplam)
