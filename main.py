from transliterate import translit
import pyperclip as pc


def input_text() -> str:
    return input("ж-zh | ё-e | ф-f | ы-y | ю-ju | ю-ju | я-ja | й-j | ш-sh | щ-sch | х-h | э-e |"
                 " ч-ch | ь-'\nType your text tnd press 'Enter':\n ")


def my_translit(in_txt: str) -> str:
    return translit(in_txt, 'ru')


if __name__ == '__main__':
    while True:
        in_text = input_text()
        out_text = my_translit(in_text)
        pc.copy(out_text)
        print(out_text)
        cont_exit = input("Press 'Q' to exit, any key to continue\n").lower()
        if cont_exit == 'q':
            break
