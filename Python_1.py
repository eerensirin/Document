"""

# En baba fonksiyon olsun sana print()
  print fonksiyonu içine yazılan şeyi çıktı olarak yansıtır örneğin 
  print("merhaba dünya")
  yazdığımız zaman çıktımız 
  merhaba dünya
  şeklinde olacaktır.
                ###                     DEĞİŞKENLER                 ###
 = değer atamak için kullanılır örneğin ali = 500 yani böylelikle
 ali ifadesi 500 e eşit oldu
 Değişkenler arasında boşluk olamaz fakat _ veya Büyük küçük harf olabilir.
 değişken ifadeleri _ ile başlayabilir fakat sayıyla başlayamaz!
 büyük küçük harf duyarlılığı vardır.

 a = 10 
 b = 20  
 print(a+b) = 30 fakat
 a ='10' ve b = '20' olursa makine str yani string olarak algılar
 print(a+b)= 1020 çıkar string toplaması yapılır.

                     ###       VERİ TİPİ DÖNÜŞÜMLERİ-CONVERSİON       ###

  x = input(' 1.Sayı : ')
  y = input(' 2.Sayı : ')
  toplam = x + y
  print(toplam)
  eğer input ifadesinin başına int yaparsak input u int e çeviricektir.
  ör: int(input('1.Sayı: ')) dediğimizde input içine yazıcağımız ifade int e çevrilicektir.
  x = 5              #int
  y = 2,5            #float
  name = "çınar"     #str
  isOnline = True    #bool

  print(type(....)) dediğimzde değişkenin tipini söyler.
  # type conversation 
  int to float 
  x = float(x)
  type(x) = #float
  float to int 
  y = int(y)
 type(y) = #int
   bool to str

  degisken1 = True 
  degisken1 = str(degisken1)
  type(degisken1) = #str
    
   bool to int
  degisken1 = True
  degisken1 = int(degisken1)
  type(degisken1) = #int


                        ###            KARAKTER DİZİSİ         ###


 name = 'Eren'
 surname = 'Şirin'
 age = 18

i =  print('my name is' + name ' ' + surname + ' and   \ni am '+ str(age) + 'years old'   )
print(i)
<<< ESCAPE CODES >>>
# \n aşağı satıra kaymasını sağlar diğer cümleyle bitişik yazılmalıdır çünkü boşlukla cümle başlatmaz.
# \t tab space ekler eğer solda olursa left tab space - sona konursa right tab space olur
# \b öncesindeki karakteri siler
# \r escape kodlarının çalışmamasını sağlar
: kullanımı için 
http://www.java2s.com/Code/Python/String/EscapeCodesbtnar.htm
# len kaç karakter olduğunu gösteren fonksiyondur "print(len(defname))" şeklinde çalışır.



print(degisken1[x:y]) seklinde calısırsa indexin x. numaradan başlar ve y ye kadar
                      aradaki tum indeksleri çıktı olarak verir.
        eğer y yazılmazsa x ten başlar ve sona kadar gelir ========> [x:]
        aynı şekilde x yazılmazsa baştan başlar ve y ye gider ====> [:y]



              ###                         FORMATLAMA                      ###

    name = "eren"
    surname = "şirin"
    print("my name is {} {} ".format(name,surname))

    print("...{}".format(name)
    #açıklaması format ile alınan inputu printe yazdırabiliriz böylece dinamik bir printe sahip oluruz.

  

    result = 200/700
    print('the result is {r:1.4}'.format(r=result))

    #formatlarda değişkenler kısaltılabilir ve x.y dediğimiz zaman 
    #virgülden sonraki kısım y kadar virgülden önceki kısım 
    # x kadar yazılır virgül fazlalığından kurtulmak için

  #slicing işlemi [] ile yapılır. 'Seçme'

                ###                       STRING METOTLARI                 ###
.upper() = Karakterleri Büyük Harfe Çevirir
.lower() = Karakterleri Küçük Harfe Çevirir
.title() = Her kelimenin ilk karakterini büyük harfe Çevirir
.capitalize() = Sadece ilk harfi büyük yapar. 
.strip() = Baştaki ve Sondaki karakterleri siler
.split() = Her kelimeyi bir dizide gösterir. # eğer karakter uzunluğu len() hesaplanırsa boşlukların sayılmadığı gözükecektir.
.count() = içindeki karakter miktarını hesaplar 
  mesaj = 'Merhabalar ben eren '

  mesaj.upper()=  # MERHABALAR BEN EREN
  mesaj.lower()= # merhabalar ben eren 
  mesaj.title()= # Merhabalar Ben Eren
  mesaj.capitalize() = # Merhabalar ben eren
  mesaj.strip() = # erhabalar ben eren
  mesaj.count('a') = # 4


diğer string methodlarını dökümantasyonlara bakarak ulaşabilirsiniz.                 python.org


                   ###                      LİSTELER                    ### 

 BenimListem = [1,2,3]
 print(BenimListem) = # [1,2,3]

 # Liste elemanlarının türü farklı olabilir  

 BenimListem2 = [0,1,2.54,True,'a']
 print(BenimListem2) = #[0,1,2.54,True,'a']

 # Listelerin toplama özelliği vardır

 list1 = ['bir','iki','üç']
 list2 = ['dört','beş','altı']

 numaralar = list1 + list2 
 print(numaralar) = # ['bir','iki','üç','dört','beş','altı']
 print(len(numaralar)) = # 6 

 #listeleri birbirlerine ekleyerek yeni liste oluşturulabilir.
 kullanıcıA = ['Eren',18]
 kullanıcıB = ['Ali',25]

 kullanıcılar =  [kullanıcıA, kullanıcıB]
 print(kullanıcılar) = # [['Eren',18],['Ali',25]]


 YeniListe = [0,1,2,3]
 YeniListe[x] = # size listedeki x. eleman ı sorar

 sonuc = i in YeniListe 
 print(sonuc) = # eğer Listenizde i diye bir eleman varsa sonuç True, yoksa False olarak bir çıktı alırısınız.


 #listelere ekleme yapabilirsiniz

 YeniListe = YeniListe + [4,5,6,7]

 print(YeniListe) = # [0,1,2,3,4,5,6,7]

  max() = maksimum değeri verir
  min() = minimum değeri verir
  .append() = değer ekler ve en sona ekler 
  .insert(x,y) = x. index e değer ekler o indexteki eleman bir sağa kayar.
  .pop() = içine yazılan indexteki değeri siler yazılmazsa en sondaki elemanı siler
  .remove() = içine yazılan karakterleri indexte tarar ve siler 
  .sort() = liste sayısal büyüklük olarak sıralanır.(alfabetik olarak ta yapılabilir.)
  .reverse() = sort işlemini tersine yapar.
  .index() = index numarasını gösterir.

  #eğer max min string değerlerle kullanılırsa alfabetik sıraya göre sayılır örneğin a:1 b:2 c:3

   sayilarim = [1,2,3,8,9,15,6,78,45]
   harflerim = ['a','b','s','p','g','j','k','c','z']
   val = min(sayilarim) 
   print(val) = # 1
   val = max(sayilarim) 
   print(val) = # 78
   val = min(harflerim) 
   print(val) = # 'a'
   val = max(harflerim) 
   print(val) = # 'z'
   val= sayilarim.append(40)
   print(val) = # [1,2,3,8,9,15,6,78,45,40]
   val = sayilarim.insert(2,50)
   print(val) = # [1,2,50,3,8,9,15,6,78,45]
   val = sayilarim.pop(2)
   print(val) = # [1,2,3,8,9,15,6,78,45]
   val = harflerim.remove(a)
   print(val) = # ['b','s','p','g','j','k','c','z']
   val = sayilarim.sort()
   print(val) = # [1,2,3,6,8,9,15,45,78]
   val = harflerim.sort()
   print(val) = # ['a','b','c','g','k','p','s','z']


                
              ###                          TUPLE               ###
 
    tuple = (0,1,2,3)
    #tuple ların listelerden farkı eleman değişimine izin vermez

    tuple[0] = [85] # dediğimiz zaman aşağıdaki hatayı vericektir.  
    #TypeError: 'tuple' object does not support item assignment
              



              
              
              ###             DICTIONARY                    ###

    #key - value şeklinde çalışır 
    #41 => kocaeli
    #34 => istanbul

    sehirler = ['kocaeli','istabnul']
    plakalar = [41,34]

    print(plakalar[sehirler.index('kocaeli')])
    

    plakalar = { 'kocaeli' : 41 , 'istanbul' : 34}
    print(plakalar['kocaeli']) = # 41 
    print(plakalar['istanbul']) = # 34
    
    #ekleme yapılabilir 

    plakalar['ankara'] = 6
    plakalar['mersin'] = 33
    print(plakalar('mersin')) = # 33

    kullanıcılar = { 
          'ErenSirin': {
              'yas':18,
              'roller': ['yonetici','kullanıcı']
              'adres': 'istanbul'
              'telefon numarası': 123456789
            

          }
            'AhmetYılmaz' : {
                   'yas':20
                   'roller': ['kullanıcı']
                   'adres':'ankara'
                   'telefon numarası' : 456123789

            }
            'ErayGuler' : {
                     'yas':18
                     'roller' : ['paspas kenarı','kullanıcı']
                     'adres' : 'bursa'
                     'telefon numarası': 16154852

                     


            }
              'HasanBasriUzun' : {
                        'yas': 19
                        'roller': ['vasıfısız işçi','kullanıcı']
                        'adres' : 'tekirdağ'
                        'telefon numarası': 65978451




              }
          
    }
    print(kullanıcılar['ErenSirin']) = #  'yas':18,
                                          'roller': ['yonetici','kullanıcı']
                                          'adres': 'istanbul'
                                          'telefon numarası': 123456789

    print(kullanıcılar['ErenSirin']['roller']) = # ['Yonetici','kullanıcı']


"""
 
    