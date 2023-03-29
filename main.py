from transliterate import translit


def input_text() -> str:
    return input("'ж-zh | ё-e | ф-f | ы-y | ю-ju | ю-ju | я-ja | й-j | ш-sh | щ-sch | х-h | э-e |"
                 " ч-ch | ь-' | ъ-' |'\n--> ")


def my_translit(in_text: str) -> str:
    pass


if __name__ == '__main__':
    in_text = input_text()
    print(in_text)
    # ttt = 'жёфыююяйшщхэчьъ'
    # for _ in ttt:
    #     print(f'{_}-{translit(_, "ru", reversed=True)}', end=' | ')
    # ttte = 'zhopa fil\'my zhan-ljuk Godar'
    # print(translit(ttt, 'ru', reversed=True))
    # print(translit(ttte, 'ru'))
