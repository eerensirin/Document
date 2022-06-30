  """  
                    ###             IF VE ELSE BLOKLARI               ###

    if True:
        print('hosgeldiniz !')


degisken = True:


if degisken:
    print('Hosgeldin')

    # çıktısı Hoşgeldin! olacaktır çünkü if bloğunun yanına yazılan 'True' ifadesi 
    # doğru oldukça çalışacaktır ve değiken i True boolean ına eşitledik

KullaniciAdi = 'Eren Şirin'
şifre = '1234'

if (KullaniciAdi == 'Eren Şirin' ) and (şifre == '1234'):
    print('girdiğiniz bilgiler doğrudur!')

#çıktı 'girdiğiniz bilgiler doğrudur! olucaktır.

if (KullaniciAdi == 'Eren Şirin' ) and (şifre == '1234'):
    print('girdiğiniz bilgiler doğrudur!')
else:
    print('kullanıcı adınız ya da parolanız yanlış.')

    #burdaki else ifadesi if in olmadığı kısımlarda çalışır bir nevi ' if not '




############################################################################################
###                                                                                      ###
###  if = eğer                                                                           ### 
###  else = eğer değilse                                                                 ### 
###  elif = if ve else arasındaki kalan durumları gösterir                               ### 
###  if 1 ve else 0 olarak düşünülürse                                                   ### 
###  elif aradaki 1/2 olarak düşünülebilir.                                              ###    
###  yazılan satırlar çok önemlidir if,elif ve else ifadelerinin sonuna : koyulmalı!     ### 
###                                                                                      ###   
###                                                                                      ### 
###                                                                                      ### 
############################################################################################


x = 10
y = 20 

if x > y :
    print('x y den büyük')
elif x == y :
    print('birbirine eşit ifadeler.')
else:
    print('y x den daha büyük ') 

    # x 10 y 5 için = x, y den daha büyük
    # x 10 y 10 için x, y ye eşit
    # x 10 y 15 için = y, x den daha büyük



    """