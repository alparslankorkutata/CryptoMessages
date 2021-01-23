# Çeviri için kullandığım sözlük aşağıdaki gibidir: T=1 H=2 E=3 Q=4 U=5 I=6 C=7 K=8 B=9 R=10 O=11 W=12 N=13
# F=14 X=15 J=16 M=17 P=18 S=19 V=20 L=21 A=22 Z=23 Y=24 D=25 G=26

# Sifrele Fonksiyonu
def sifrele(text):
    code = {' ': ' ', 'a': '22 ', 'b': '9 ', 'c': '7 ', 'd': '25 ', 'e': '3 ', 'f': '14 ', 'g': '26 ', 'h': '2 ',
            'i': '6 ', 'j': '16 ', 'k': '8 ', 'l': '21 ', 'm': '17 ', 'n': '13 ', 'o': '11 ', 'p': '18 ', 'q': '4 ',
            'r': '10 ', 's': '19 ', 't': '1 ', 'u': '5 ', 'v': '20 ', 'w': '12 ', 'x': '15 ', 'y': '24 ', 'z': '23 '}

    sifrele = ""

    for x in text:
        sifrele += code[x.lower()]

    return sifrele


# Desifre Fonksiyonu
def desifre(number):
    code = {' ': ' ', '22': 'a', '9': 'b', '7': 'c', '25': 'd', '3': 'e', '14': 'f', '26': 'g', '2': 'h', '6': 'i',
            '16': 'j', '8': 'k', '21': 'l', '17': 'm', '13': 'n', '11': 'o', '18': 'p', '4': 'q', '10': 'r', '19': 's',
            '1': 't', '5': 'u', '20': 'v', '12': 'w', '15': 'x', '24': 'y', '23': 'z'}
    desifre = ""

    for y in number.split():
        desifre += code[y] + " "

    return desifre


# Giriş geçerli değilse kullanıcı girişini döngülemek(loop) için değişken sayısı
Loop = 1

while Loop == 1:
    # kullanıcı girisi
    Option = str.lower(input("Bir mesajı şifrelemek mi yoksa şifresini çözmek mi istiyorsunuz?: "))
    # sifrele
    if Option == "sifrele":
        Sifrele_Text: str = input("Şifrelemek istediğiniz mesaj nedir: ")
        print(sifrele(Sifrele_Text))
        Loop = 0
    # desifre
    elif Option == "desifre":
        desifre_Numarasi = input("Deşifre etmek istediğiniz mesaj nedir: ")
        print(desifre(desifre_Numarasi))
        Loop = 0
    # geçersiz kullanıcı girişi
    else:
        print("lütfen geçerli bir seçenek girin ...")
        Loop = 1