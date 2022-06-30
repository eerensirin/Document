"""
            ###         PYTHONDA METOTLAR           ###

    #METHOD

from re import X
from syslog import LOG_EMERG
from typing import Hashable


liste = [1,2,3,4,5]

.append(num1) = Listeye ekleme yapmanızı sağlar. Paantez içine yazılan num1 listeye eklenir 
.pop() = Listeden kaldırma işlemidir. parantez içine bir şey yazılmazsa en son yazılırsa yazılan index 


<<< pythonun kendi sitesinden gerekli dökümantasyonalara bakılabilir. >>>

ör : 
liste.append(8)
print(liste)
# çıktımız 
[1,2,3,4,5,8]   şeklinde olacaktır.

liste.pop()
print(liste)
#çıktımız
[1,2,3,4,5]     <<< şeklinde olacaktır. >>> 

    #FONKSİYONLAR !!!!  (DEF)
<<< def kullanımı >>>

def FonksiyonunIsmi():
    Yapılacak işlem
    .
    .
    . 
    . 


ör : 
     def MerhabaFonksiyonu():
         print("Merhaba!")

                                            fonksiyonumuzun tanımlamasını ve ne işlem 
                                            yapılamsı gerektiğini tanımladık 
MerhabaFonksiyonu()   Yazıldığında ;
#çıktımız

---   Merhaba!  ---  olucaktır.


def MerhabaFonksiyonu(name):                parantez içine yazdığımız parametre 
     print("Merhaba" + name)                 sayesinde fonksiyonumuz gerekli parametreyi
                                             aldığı zaman çalışıcak ve parametreyi 
    MerhabaFonksiyonu(Eren)                  kullanıcaktır.
    # çıktımız 
-- Merhaba! Eren  --     olucaktır.



                ::: Fonksiyonları değişkenlere atayabiliyoruz :::

def MerhabaFonksiyonu(name):
    return "Merhaba"+ name 


msg = MerhabaFonksiyonu("Eren")

print(msg)     Yazıldığında;
# çıktımız
--   Merhaba! Eren   --   olucaktır.


def total(num1,num2):
    return num1 + num2 

toplama = total(10,20)
print(toplama)
# çıktımız 
30 olucaktır.

def YasHesapla(DogumYili):                                     #bu fonksiyonumuzda yaş hesaplaması yapmak için parametreye doğum yılı yazılır 
    return 2022 - DogumYili                                    #ardından şuanki seneden çıkartılır ve bu sonucun                                      
                                                               #fonksiyon içinde tutulması ve sonra kullanılması için return ifadesi kullanılır . 


HasanBasininYasi = YasHesapla(2002)
print(HasanBasininYasi) 

# çıktımız 
2022 - 2002 = 20 olucaktır.


def EmekliligeNeKadarVar(DogumYili, isim):                                                          
    yas=YasHesapla(DogumYili)
    emeklilik = 65 - yas 

    if emeklilik > 0 :
        print(f"emekliliğinize {emeklilik} kadar yıl kaldı")
    elif emeklilik == 0 :
        print("Emekli olmadıysanız bu sene içinde emekli olucaksınız. ")
    else : 
        print("Zaten Emekli olmuşsun :d")



############################################################################################
###  bu fonksiyonumuzda dogumyili inputu(girilen bilgi- veri(data) ) alarak				 ### 
###  emeklilik yaşından çıkardık böylelikle kaç sene kaldığını bulup sonuca göre		 ### 
###  if ile sınıflandırmasını ve output(çıkışımızı) yaptık							     ### 
############################################################################################

def IsımDegistirme(isim):
    isim = "Hasan Basri"

YeniIsim = "Eren"

IsımDegistirme(YeniIsim)

print(YeniIsim)                            >>>>>            fonksiyonun parametresini () kısmı değiştirerek 
# çıktımız                                 
 'Eren'   olucaktır.                                        çıktı alınan veriyi değiştirme imkanımız var.        <<<<<<


def Degisiklik(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"]

Degisiklik(sehirler)

print(sehirler)                         Açıklama : fonksiyonumuzun işlevi belirtilen
# çıktımız                                         
["istanbul","izmir"]                                herhangi bir listenin 0. index(ilk)
                                                    ini istanbul ile değiştirmek.

def toplama(a,b):
    return sum((a,b))


print(toplama(10,20))
#çıktımız
30 olucaktır.   

toplama yapılıcak sayıyı yandaki gibi :             def toplamaOrnek(a,b,c,d)
seklinde arttırabiliriz.

def KullaniciBilgisi(**args):
    for key, value in  args.items():
        print(' {} is {}'.format(key,value))

                                                                                Açıklama :  args = Keyword Arguments
KullaniciBilgisi(isim= "Armagan" , yas = 20 , sehir = 'Istanbul')                                  anahtar şifre sayesinde kullanıcı bilgilerini           
KullaniciBilgisi(isim= "Hasan" , yas = 19 , sehir = 'Tekirdağ')                                    kişiye özel şekilde görebiliyoruz.
KullaniciBilgisi(isim= "Eren" , yas = 18 , sehir = 'Hatay')

 # çıktımız 
isim is Armagan 
yas is 20 
şehir is Istanbul 

isim is Hasan 
yas is = 19
şehir is Tekirdağ

isim is Eren 
yas is 18
şehir is Hatay 


## LAMBDA

def square(num): return num ** 2 
result= square(2)
print(result)

# çıktımız 
4 olucaktır 


sayilar = [1,3,5,9]


result = list(map(square, sayilar))

print(result)                    map in amacı fonksiyonu bir liste içerisinde 
# çıktımız                         for döngüsü olmadan kullanabilmektir.
[1,29,25,81]
olucaktır.

                         map fonksiyonun kullanımı : map(fonksiyon ismi , liste ismi )
                            bu şekilde çalıştırdığımız zaman muhtemelen 
                                     < map object at 0x0213A84 >
                            şeklinde bir çıktı alırız
                             bu bellekte yapılan işlemin tutulduğu yeri gösterir
                             bunu list(map(fonksiyon ismi , liste ismi )) şekline kullanıp bunu bir değişkene eşitlersek
                             (örnekte olduğu gibi) manıtklı bir sonuç elde edebiliriz    



<<<< alternatif >>>

for item in map(square, sayilar):
    print(item)

# çıktımız 
[1,9,25,81]


                         lambdanın açıklaması :
                         aslında tek kullanımlık 
                         fonksiyonun tanımlanması gibi düşünülebilir.
sayilarim = [1,2,3,4]
result = list(map(lambda : num = num ** 2 , sayilarim ))

dediğimizde herhangi bir fonksiyona ihtiyaç duymadan tek seferlik bir 
işlem yazabildik.



square = lambda num: num ** 2                             lambda fonksiyonu isimsiz fonk olarak ta geçer.
                                                          örnekte gösterildiği gibidir. 
numbers = [2,4,6,8]

result = list(map(square,numbers))

#çıktımız 
[4,16,36,64]



#FILTER

numbers = [1,2,3,4,5,6,7]

def check_even(num): return num%2 == 0 

sonuc = list(filter(check_even, numbers))
print(sonuc)
# çıktımız 
[2,4,6]





#GLOBAL - LOCAL DEĞİŞKENLER
                                      
x = 'x global'                            fonksiyon için tanımmlanan değişkenler 
                                          dışarıyı etkilemez dışarısı global içerisi local olur.

def function():
    x = 'local x'

function()
print(x)
# çıktımız

global x 



def function():
    local scope 
    x = 'local x'
    print(x)


#çıktımız
global x 



name = 'global string'
def greeting():
    name = 'Çınar'
    
    def hello():
        print('hello'+name)

    hello()

greeting()


###########################

x = 50
def test(x):
    global x
    print(f"x"+ {x} )

    x = 100
    print(f'changed x to ' + {x} )

test()
print(x) 


#çıktımız
x: 50
changed x to 100
"""