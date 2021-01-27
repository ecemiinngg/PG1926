# Sıralama algoritmaları programlamanın kaderini değiştiren algoritmalardır. Peki neler yapacağız ?
#
# Neler Yapacağız ? neler neler yapacağız
#
# 1. Kullanıcıdan bir sayı girdisi alacağız.
#
# 2. Daha sonra sayıların yerlerini değiştirmemiz gerekiyor. Fakat sadece 0 sayısını değiştireceğiz.
#
# 3. Sayıların sırasını bozmadan 0 sayılarını listenin başına taşımanız gerekmektedir.
#
# 4. Listenin son halini ekrana yazdırmalısınız.
#
# Kısıtlamalar
#
# Herhangi bir kısıtlama yoktur.
#
# Çıkış formatı
#
# [2,4,1,6,4,0,0]
#
# [0,0,1,2,4,4,6]

ls = list(map(int, input('Lütfen listeyi, her bir sayıyı boşluklarla ayırarak giriniz: ').split()))

for i in range(len(ls)):
    if ls[i] == 0:
        ls.insert(0, ls.pop(i))

print(ls)
