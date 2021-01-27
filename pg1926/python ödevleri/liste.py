# Listeyi oluşturuyoruz
ls = list()
while True:
    try:
        ls.append(int(input('Listeye eklemek sayı giriniz: (Bitirmek için Enter\'a bas.)')))
    except:
        break

# Listeden tek olan sayıları ayrı bir listeye topluyoruz
lstek = [x for x in ls if x % 2 == 1]

# Sıralayıp en sondaki elemanı yazdırıyoruz
lstek.sort()
print(lstek[-1])
