"""
                          ###             ATAMA OPERATÖRLERİ          ###
# normalde:
x = 5
y = 10
z = 20

 # tek satırda:
x,y,z = 5,10,20

 # degisiklik yapmak istenirse:
 x,y = y,x 
 
 # normalde:        #daha kısa : 
 x = x + 5         x += 5
 x = x * 5         x *= 5
 x = x / 5         x /= 5 
 x = x - 5         x -= 5
  
degerler = (1,2,3)

x,y,z = degerler #seklinde x = 1 , y = 2 , z = 3 olur.

# dikkat edilmelidir ki eleman sayıları eşit olmalıdır yoksa aktarım yapılmaz !!!


degerler1 = (1,2,3,4,5)


x,y, *z = degerler1

 
print(x,y,z) = # 1 2 [3,4,5]
""eğer elemanın başına bu şekilde * eklenirse 
geriye kalanları o elemana atar ve liste oluşturur.""


                           ###           KARŞILAŞTIRMA OPERATÖRLERİ           ###


    #sorgulama için " == " kullanılır ve eşit midir sorusuna denk gelir.
    #sorgulama için " != " kullanılır ve eşit değil midir sorusuna denk gelir.
    a,b,c,d = 5,5,10,4

    deger = (a == b) 
    print(deger) = # True
     
    deger = (a == c) 
    print(deger) = # False

    kullaniciAdi = 'erenSirin'

    sorgula = ('eren' == kullaniciAdi)
    print(sorgula) = # False

    sorgula2 = ('erenSirin' == kullaniciAdi)
    print(sorgula2) = # True

    sorgula3 = (a != b)
    print(sorgula3) = # False 


                        ###         MANTIKSAL OPERATÖRLER           ###

     and = koşulun her iki tarafıda True gönderirse ifade True olur
     or  = koşulda herhangi bir ifadenin True olması Yeterlidir
     not = koşulun cevabını tam tersi yapar True ise False , False ise True yapar.

    x = 5
    result = x > 5 and x < 10
    print(result) = # False


    # Identity Operator : is
        ## eğer iki değişkenin bellekteki yeri aynıysa bu ikisi aynı obje demektir
           ör x = y = [1,2,3]
           ile 
           x = [1,2,3]
           y = [1,2,3]
           farklı şeylerdir çünkü 
           ilk örnekte x veya y için yapılan append pop ya da benzeri değişiklikler hem x hem y yi etkileyecektir
           ama ikinci örnekte x e değişiklik ya da ekleme vs. yapılırsa bu y yi etkilemeyecek ve bozulacaktır.
        
        x = y = [1,2,3]
        z = [1,2,3]

        print(x==y) = # True
        print(x==z) = # True

        print(x is y) = # True
        print(x is z) = # False

        x = [1,2,3]
        y = [2,4]

        print(x is y) = # False
    # Membership Operator : in

        x = ['elma','muz']
        print('muz'in x) = # True
        print('elma' not in x) = #False
        
"""


