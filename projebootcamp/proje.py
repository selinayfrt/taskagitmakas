import random # bilgisayar secenekler arasında seçim yapabilsin diye radom kütüphanesini import ettim

def rock_paper_scissors_selinay_firat(): #istenen şekilde fonksiyon tanımladım
    print("Taş Kağıt Makas oyununa hoşgeldiniz..") #karşılama mesajları
    print("Öncelikle Taş Kağıt Makas arasından bir seçim yapınız")
    print("Kağıt taşı yener, taş makası yener, makas kağıdı yener")
    print("Oyun birden fazla tur olacak ve 2 turu kazanan oyunun galibi olacaktır")
    print("İyi eğlenceler dileriz..")

    secenekler = ["taş", "kağıt", "makas"] # seçeneklerden oluşan liste oluşturdum

    while True: #oyun döngüsünü başlattım
        oyuncu_skoru = 0 # skor başlangıcını 0 atadım
        bilgisayar_skoru = 0

        while oyuncu_skoru < 2 and bilgisayar_skoru < 2: #skor 2 olana kadar döngü devam
            oyuncu_secimi = input("Seçiminizi yapınız (taş, kağıt, makas): ").lower() #oyuncudan girdi aldım herhangi harf sorunu yaşamasın diye lower ile küçük harfe getirdim
            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Geçersiz seçim, tekrar seçiniz (taş, kağıt, makas): ").lower()

            bilgisayar_secimi = random.choice(secenekler) #bilgisayara seçeneklerden radom seçim yaptırdım
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:#skorlara göre oyun durumunu bildirdim
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Tebrikler, turu kazandınız!")
                oyuncu_skoru += 1 #skor 1 artırıldı
            else: #bilgisayarın kazanma durumunu else ile ifade ettim
                print("Maalesef, turu kaybettiniz.")
                bilgisayar_skoru += 1

            print(f"Skor: Oyuncu {oyuncu_skoru} - {bilgisayar_skoru} Bilgisayar\n") #skor durumu 

        if oyuncu_skoru == 2:
            print("Tebrikler, oyunu kazandınız!")
        elif bilgisayar_skoru == 2:
            print("Maalesef, oyunu kaybettiniz. Bilgisayar kazandı.")

        tekrar_oyna = input("Tekrar oynamak ister misiniz? (evet/hayır): ").lower()#oyuncuya tekrar oynayıp oynamayacağını sordum
        if tekrar_oyna != "evet":
            print("Oyun bitti.")
            break

rock_paper_scissors_selinay_firat() #fonksiyonu çalıştırmak için

#proje için teşekkürler <3

