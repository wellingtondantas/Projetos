#Libs
from mtranslate import translate


def main():
    to_translate = 'Bonjour comment allez vous?'
    print(translate(to_translate))
    print(translate(to_translate, 'it'))
    print(translate(to_translate, 'pt'))


if __name__ == '__main__':
    main()