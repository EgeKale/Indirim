

def indirim(price, discount):
    print('Indirimli Fiyat:')
    print(price - (price / 100 * discount))

while True:
    try:
        p = int(input('Fiyat:'))

        d = int(input('Indirim Yuzdesi:'))

        indirim(p, d)
    except:
        print('Lutfen Sayi Giriniz!!!')
        break








