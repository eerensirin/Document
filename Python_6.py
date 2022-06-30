

        ###         OBJECT ORIENTED PROGRAMMING ( OOP )             ###


 başlamadan önce : 
         oop, obje yönelimli programlama ya da nesne yönelimli programlamada (bu isimlerin hepsi aynı anlama gelmektedir)
        ilk kez duyacağımız çok fazla terim veya daha önce karşılaşmadığımız çok fazla komut-fonksiyon olacaktır bununla ilgili
        stackoverflow dan ya da yazılan kodlardan yararlanabilirsiniz.
                ör:     
                __init__ ya da self. yapıları oop konusunda bizimle neredeyse sürekli beraber olacaklar bu yüzden konuya başlamadan önce
                __init__ ve self. hakkında kısa bir bilgi vermek istiyorum


                        __init__ nedir ? 
                                pythonda yapıcı fonksiyon olarak belirlenen __init__ bir nesne çağrıldığında otomatik olarak çalışır ve 
                                sadece nesneyi ilk oluştururken çağıran bir fonksiyon olarak tanımlayabiliriz.
                                        kısaca özetlemek gerekirse bir classtan nesne üreteceksek içinde __init__ olmak zorunda. 
                        self. nedir ? 
                                __init__ le beraber gelen oop de sıkça karşılaştığımız self fonksiyonu da class içinde ürettiğimiz nesnelere 
                                ulaşmamızı sağlayan bir araç gibi düşünebiliriz ve karışıklık olmaması adında classlarda genelde tanımlamak istediğimiz 
                                kelimenin yerine (örneğin o kelime keyword_x olsun )
                                self.keyword_x = keyword_x diyerek class içindeki türettiğimiz keyword_x nesenesine ulaşırken karışıklık olmaması adına değiştirdik 
                                yapılamsı zorunlu değildir fakat
#CLASS  
>> instance (object)

liste = [1,2,3,4]

result = type(liste)

print(result)                                   
#çıktımız
<class 'list' >                            # yani list classından gelen bir instance .
şeklinde olucaktır. 



class tanımlama şekli 
ör : 


class Person ():
        #attributes
        #methods


#object (instance)
p1 = Person() 

böylelikle Person classının fonksiyonlarına p1 üzerinden ulaşılabilir kılınır.

print(p1)
#çıktımız 
<__main__.Person object at 0x184729141B1>
olucaktır burdan anlaşıldığı üzere Person türünde bir class olduğunu
ve bunun tutulduğu adresi verdiği gözüküyor.

print(type(p1))
#çıktımız
<class '__main__.Person'>
şeklinde olucaktır.


#class attributes
address = 'bilgi yok '
#constructor (Yapıcı method)

def __init__(self, name, year):          selfin açıklaması;class tan türetilen objeleri temsil ediyor
        #object attributes
        self.name = name
        self.year = year
        print("init çağırıldı")           init methodu oluşturulan her obje için çalıştırılır 


p1 = Person('eren', 2003)
p2 = Person('ali, 2000)

print(f'name : {p1.name} year : {p1.year} address : {p1.address}')
print(f'name : {p2.name} year : {p2.year} address : {p2.address}')
#çıktımız
name : eren year : 2003 address: bilgi yok
name ali year : 2000  address : bilgi yok 
olucaktır. 
burdkai class attributes ta yer alan address in p1.address olarak çalışmasını görebiliyoruz 
aynı Person classının içinde çünkü 

#instance methods 
def intro(self):
        print('hello There i am ' + self.name)

def calculateAge(self):
        return 2022 - self.year 


>> eğer
 p1.intro() dersek ; 
 #çıktımız
hello There i am eren 
şeklinde olucaktır.

>> eğer
print(f'yaşım:{p1.calculateAge}')
yazacak olursak 
#çıktımız
19
olucaktır 

class Circle():
        pi = 3.14
        def __init__(self,yaricap = 1):                   # yaricap = 1 dediğimizde yariçap bilgisi girilmezse 1 olarak alması gerektiğini söyledik 
                self.yaricap = yaricap
        
        def AlanHesapla(self):
                return self.pi * (self.yaricap ** 2)

        def CevreHesapla(self):
                return 2 * self.pi * self.yaricap

c1 = Circle() # yaricap belirtilmedi 1 
c2 = Circle(5) 

print(f'c1 Çemberinizin Alanı : {c1.AlanHesapla()}\n c1 Çemberinizin Çevresi :{c1.CevreHesapla()}')
print(f'c2 Çemberinizin Alanı : {c2.AlanHesapla()}\n c2 Çemberinizin Çevresi :{c2.CevreHesapla()}')
#çıktımız
c1 Çemberinizin Alanı : 3.14
c1 Çemberinizin çevresi : 6.28
c2 Çemberinizin Alanı : 78.50
c2 Çemberinizin Çevresi : 11.2800000000000000001

şeklinde olucaktır.

## Inheritance (kalıtım): Miras Alma

Kisi => isim, soyisim , yas , yeme() , kosma() , icme()

kisi classımız olsun ve bu classta yukardaki objeleri ve fonksiyonları tanımladık diyelim
eger biz bu objeleri ve fonksiyonları  farklı classlarda kullanabiliriz 

class Ogrenci():

eğer böyle bir class oluşturduktan sonra classın içine 


class Student(kisi):

yazarsak kisi classının sahip olduğu her şeyi Ogrenci class ında kullanabiliriz. 

class Kisi():
        def __init__(self):
                print("kişi oluşturuldu")

class Ogrenci(Kisi):
        pass


# pass hiçbir etki etmiyor - çalışmasına hiçbir şey olmamış gibi devam ettiriyor-  içinin boş kalmaması için yazılabilir 

p1 = Kisi()
print(p1)
#çıktımız
kişi oluşturuldu 
p2 = Ogrenci()
print(p2),
#çıktımız 
kişi oluşturuldu 

eger :::

class Ogrenci(kisi):
        def __init__(self):
                Person.__init__(self)
                print("ogrenci yaratıldı ")

şeklinde düzenlersek

s1 = Ogrenci()
print(s1)
#çıktımız 
kişi yaratıldı >>>> Burdaki ilk kisi classından geliyor
kişi yaratıldı  >>>> Burdaki Ogrenci classına tanımladıgımız person.__init__ ten geliyor
öğrenci yaratıldı >>>Burdaki Ogrenci classında def __init__ ten geliyor 









