from transliterate import translit
import pyperclip as pc


def input_text() -> str:
    """Print some small help and return input text"""
    return input("\n| ж-zh | ё-e | ф-f | ы-y | ю-ju | ю-ju | я-ja | й-j | ш-sh | щ-sch | х-h | "
                 " ч-ch | ь-' |\n\nType your text end press 'Enter':\n\n-> ")


def my_translit(in_txt: str) -> str:
    """Transliterate input text and return"""
    return translit(in_txt, 'ru')


if __name__ == '__main__':
    while True:
        in_text = input_text()
        out_text = my_translit(in_text)
        pc.copy(out_text)
        print(f'\n--> "{out_text}" copied to clipboard\n')
        cont_exit = input("Press 'Q' then 'Enter' to exit, any key to continue\n").lower()
        if cont_exit == 'q':
            break
