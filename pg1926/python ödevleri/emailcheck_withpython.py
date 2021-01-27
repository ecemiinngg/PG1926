import re

def validity_check(email): # e-mail'in doğruluğunu test etmek
    try:
        domain_adi = email.split('@')[1] # adresi @'den ikiye ayırdık eğer @ yoksa hata verecektir o yüzden false
    except:
        return False
    if len(domain_adi) < 1: # domain adı yoksa false
        return False
    elif len(domain_adi.split('.')) > 3: # eğer @'den sonraki noktalı kısımlar 3 den fazla ise false
        return False

    if re.match(r'[a-zA-Z0-9\-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', email): # regex kullanarak email adresinin doğru formatta olduğunu onaylıyoruz.
        return True
    else:
        return False



# domain adının uzunluğunu ve adresi alırız
len_domain = int(input('Lütfen E-Mail adresinin domain adının uzunluğunu giriniz: '))
email = input('Lütfen E-Mail adresinizi giriniz: ')

if validity_check(email):
    print('Mail adresiniz doğrudur.')
else:
    print('Mail adresiniz yanlıştır.')
