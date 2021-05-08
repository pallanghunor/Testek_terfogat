
def terfogat():
    terfogat: int = 0
    print('=====================================================')
    print('Térfogatszámítás')
    print('Melyik síkidommal akarja végrehajtani a számítást?')
    print('1. Kocka')
    print('2. Téglatest')
    valasztott: int = 0
    while valasztott <= 0 or valasztott > 2:
        print('')
        valasztott: int = int(input('Írd le mit választottál: '))
        if valasztott <= 0:
            print('')
            print('Az adat nem megfelelő.')
            continue
        if valasztott > 2:
            print('')
            print('Az adat nem megfelelő.')
            continue
    print('')
    print('=====================================================')

    if valasztott == 1:
        print('')
        print('Kocka térfogatszámítása')
        a: int = 0
        while a <= 0:
            print('')
            a: int = int(input('Írd le a kocka oldalát cm-ben: '))
            if a <= 0:
                print('')
                print('Az adat nem megfelelő a számoláshoz.')
                continue
            terfogat = a * a * a
            print('')
            print(f'A kocka felszíne: {terfogat}cm3 ')
            print('')

    if valasztott == 2:
        print('')
        print('Téglatest térfogatszámítás')
        print('')
        a: int = 0
        b: int = 0
        c: int = 0
        while a <= 0 or b <= 0 or c <= 0:
            a: int = int(input('Írdd le a téglatest a oldalát: '))
            if a <= 0:
                print('Az a adat nem megfelelő a számoláshoz.')
                continue
            b: int = int(input('Írd le a téglatest b oldalát: '))
            if b <= 0:
                print('A b adat nem megfelelő a számoláshoz.')
                continue
            c: int = int(input('Írd le a téglatest c oldalát: '))
            if c <= 0:
                print('A c adat nem megfelelő a számoláshoz.')
                continue
        terfogat = a * b * c
        print('')
        print(f'A téglatest területe: {terfogat}cm3')
        print('=====================================================')


def main():
    terfogat()


if __name__ == "__main__":
    main()
