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

sifir_ls = list()

for i in ls:
        if i == 0:
            sifir_ls.append(i)

yeni_ls = sifir_ls + list(filter(lambda a: a != 0, ls))
print(yeni_ls)

# def sifir_mi(a):
#     return a != 0
