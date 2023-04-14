adminler = [["emiremir", "9999"]]
kullanicilar = [["emir", "4545"], ["ayse", "1234"], ["ali", "9876"]]
print("Sisteme Hoşgeldiniz")
giris = int(input("Kullanıcı olarak giriş yapmak için: 1'i\nAdmin olarak giriş yapmak için: 2'yi tuşlayınız: "))

if giris == 1:
    print("Kullanıcı sekmesine hoşgeldiniz")
    Kgiris = int(input("Sisteme Üye olmak için: 1'i\nSisteme giriş yapmak için: 2'yi\nŞifremi unuttum/Yeni şifre almak için: 3'ü tuşlayınız: "))

    if Kgiris == 1:
        yenikullanici = input("Kullanici adı giriniz: ")
        yeniparola = input("Parola giriniz: ")
        kullanicilar.append([yenikullanici, yeniparola])
    elif Kgiris == 2:
        kullaniciadi = input("Kullanıcı adınızı giriniz: ")
        parola = input("Parolanızı giriniz: ")

        for kullanici in kullanicilar:
            if kullanici[0] == kullaniciadi and kullanici[1] == parola:
                print("Hosgeldin ", kullaniciadi)
                break
        else:
            print("Kullanıcı adı veya şifre yanlış")

elif giris == 2:
    print("Admin sekmesine hoşgeldiz")
    adminkullaniciadi = input("Kullanıcı adınızı giriniz: ")
    adminparola = input("Parolanızı giriniz: ")
    if [adminkullaniciadi, adminparola] in adminler:
        print("Hoşgeldiniz")
    else:
        print("Hatalı kullanıcı adı veya şifre")
else:
    print("Geçersiz tuşlama")