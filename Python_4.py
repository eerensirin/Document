"""

numbers = [1,2,3,4,5]

    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
    print(numbers[3])
    print(numbers[4])

    #normalde ekrana yazdırmak için tek tek böyle yazmamız gerekir.

                            #############                    FOR DÖNGÜSÜ                     ##############

    ##KULLANIMI:

    numaralar = [1,2,3,4,5]

    for num in numaralar:
        print(num)
    #çıktısı
    1                                burdaki amacımız bir değişken ismi seçip ( ör:
    2                                num isimli ) listedeki tüm elemanları değişkene 
    3                                atamak ve onları print komutuyla tek tek yazdırmak     
    4
    5

    # EGER LISTE OLURSA 


    isimler = ['eren','ali','mehmet'] 

    for isim in isimler:
        print(f'benim ismim : {isim} ')
    
    #çıktısı                                   
    benim ismim eren                    bu örnekte hem f (format) ı kullandık hemde 
    benim ismim ali                     for döngüsü içinde tüm elemanlarımızı döndürdük.
    benim ismim mehmet 



     # EGER STRING OLURSA:

        isim = 'Eren'


        for n in isim:
            print(n)
        # dediğimizdeki çıktımız : 
        E
        r 
        e
        n 


    # EGER TUPLE OLURSA:
    tuple = (1,2,3)

    for t in tuple:
        print(t)
    # çıktımız
    1
    2
    3


    tuple2 =[(1,2),(1,3),(3,5)]

    for a,b in tuple2:
        print(a,b)
    # çıktımız
    (1,2)
    (1,3)
    (3,5)


    # EGER DICTIONARY OLURSA:
    
    sozlugum = {'veri1' : 5, 'veri2': 6, 'veri3': 7'}

    for data in sozlugum.items() :
        print(data)
    # çıktımız                                    
    ('veri1',5)                                 eger:
    ('veri2',6)                                     for data in sozlugum:             
    ('veri3',7)                                         print(data)
                                                dersek çıktımız : 
                                                veri1 
                                                veri2
                                                veri3 
                                                seklinde olacaktı

    for key,value in sozlugum.items():
        print(key,value)
     # çıktımız                                  
    ('veri1',5)                                
    ('veri2',6)                                             
    ('veri3',7)  


                #############                   WHILE DÖNGÜSÜ                     ##############


    # 1 den 100 e kadar sayıları tanımlamak istersek : 
    
    x = 0
                                                         ### ACIKLAMA ###
    while x < 100:                                while ifadesi bir nevi koşul belirtir.
        print(x)                                  yanına yazılan ifade olana kadar döngü
        x += 1                                    devam eder ve genelde booleanlar kullanılır.

    # çıktımız
    1
    2
    3
    ...
    100


    x = int(input('Sayınızı Giriniz:'))


    while x <= 100:                                kullanıcıdan alınan input bir değişken 
        if x % 2 == 1:                             olarak kaydedilir ve değişken çift veya 
            print(f'sayınız tek {x}')              tek olmasına göre sınıflandırılır.
        else:
            print(f'sayınız çift {x}')


    isim = ' '               #False
    
    while not isim:                             burdaki not isim = True'ya denk gelir
        isim = input('isminizi giriniz: ')
        print(f'merhaba {isim}')
    
    <<< isminizi girene kadar döngü size ,
    isminizi giriniz: 
    çıktısını vermeye devam edecektir >>> 



    #############              BREAK CONTINUE IFADELERI                   ##############
   
    ## BREAK
    isim = 'Eren Sirin'

    for hece in isim:                                     << BREAK >>
        if hece == 'n':                                 koşulun sağlandığı yere kadar 
            break                                       çalışmasını sağlar. o noktadan
        print(hece)                                     sonrasıda çalışmaz 
    #çıktımız
    E
    r
    e 
       şeklinde olacaktır.

    isim2 = ' Alparslan'

    for hece in isim2 :
        if hece == 'r':
            continue 
        print(hece)

    #çıktımız
    A                                                   << CONTINUE >>
    l                                                koşulun sağlandığı yeri boş geçerek 
    p                                                devamını getirir örnekteki gibi
    a                                                string içindeki r harfini es geçerek
                                                     çalışacaktır kodumuz
    s 
    l 
    a 
    n  
     şeklinde olacaktır.


    #1 - 100 e kadar olan tek sayıların toplamı {n e kadar olan sayılar n*(n+1)/2}


    result = 0
    x = 1 

    while x <= 100:
        if x % 2 == 0:
             continue
        x+= 1
        result += x 
    
    #############              DONGU METOTLARI                 ##############

    ## RANGE

    for item in range(a,b,c):
        print(item)
    #çıktımız
     a dan b ye kadar olan sayıların arasında
     c kadar boşluk olacak şekilde seçilir.


    print(list(range(50,100,20)))
    ifadesi de yukarıdaki for döngüsüne eşittir ancak bu şekilde liste olarak çıktı alırız.



    ## ENUMERATE

    index = 0
    greeting = 'Hello There !'

    for letter in greeting:
        print(f'index : {index} letter: {letter} ')

        index += 1

            >>> bu şekilde index numarası bulabiliriz. <<<

    for index,letter in enumerate(greeting):
        print(f'index: {index} , letter : {letter}')
        index += 1 
            
             >>> bu şekilde index numarası bulabiliriz. <<<


    ## ZIP


    liste1 = [1,2,3,4,5]
    liste2 = ['a','b','c','d','e']
 
    print(list(zip(liste1,liste2)))                                          
    # çıktımız                                                              
    [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]                                                <<<< ZIP >>>>>>>
                                                                                            zip metotunun amacı farklı listeleri birbiriyle
                                                                                            index sayısına göre eşliyor ve yeni bir liste 
                                                                                            oluşturuyor.

## 1-100 arasında rastgele üretilicek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.



import random 

sayi = random.randint(1,100)


data1 = int(input('Sayıyı Tahmin etmeye çalışınız:'))

hak = 5
while hak > 0 :
    hak-=1
    if data1 > sayi:
        print('Tahmin ettiğiniz sayı gerçek sayıdan daha büyük tekrar değer giriniz.'
    elif data1 = sayi:
        print('Sayıyı Doğru tahmin ettiniz.')
    else : 
        print('Tahmin ettiğiniz sayı gerçek sayıdan daha küçük')
    if hak == 0 :
        print(f'tahmin hakkınız doldu sayı :  {sayi}')



"""