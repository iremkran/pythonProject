"""Bir konsol üzerinden kullanıcı girişi olacak.Kullanıcıdan koordinat düzleminde bir noktanın x ve y noktaları istenecek.
Her kullanıcı girişi yapıldığında arkada yeni bir rastgele noktalarda bir üçgen üretilecek ve kullanıcıdan alınan nokta
bu üretilen üçgenin içinde mi değil mi diye kontrol edecek. Ve her döngünün sonunda kullanıcıya devam mı bitir mi diye sorulacak.
Eğer bitir denirse program sonlanacak."""
#İrem Kıran

import random

def random_ucgen_olustur():
    ucgen = (
        (random.randint(a=0, b=10), random.randint(a=0, b=10)),
        (random.randint(a=0, b=10), random.randint(a=0, b=10)),
        (random.randint(a=0, b=10), random.randint(a=0, b=10))
    )
    return ucgen

def nokta_konum_dugrulama(nokta, ucgen):
    x, y = nokta
    x1, y1 = ucgen[0] #A noktası
    x2, y2 = ucgen[1] #B noktası
    x3, y3 = ucgen[2] #C noktası

    # Barycentric Coordinate System: Üçgen içerisinde belirli bir noktanın konumunu belirlemek için kullanılır.
    detT = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3) #Üçgenin alanı
    #Alpha, Beta ve Gamma değerleri, üçgenin içindeki bir noktanın barycentric koordinatlarıdır.
    #Bu değerler üçgenin köşelerine olan uzaklıklarını belirler.
    alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / detT
    beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / detT
    gamma = 1 - alpha - beta #Bu değerlerin toplamı her zaman 1'e eşittir

    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1 #Değerler 0 ve 1 arasında değilse üçgen dışarısındadır.

def main():
    while True:
        ucgen = random_ucgen_olustur()

        x = float(input("Nokta için x koordinatını giriniz:"))
        y = float(input("Nokta için y koordinatını giriniz:"))
        nokta = (x, y)

        if nokta_konum_dugrulama(nokta, ucgen):
            print("Nokta üçgenin içinde.")
        else:
            print("Nokta üçgenin dışında.")

        print(f"Random üçgen koordinatları : {ucgen}")


        devam = input("Devam etmek istiyor musunuz? Devam etmek için 'e' bitirmek için 'h' yazınız:")
        if devam != 'e':
            break

if __name__ == "__main__":
    main()