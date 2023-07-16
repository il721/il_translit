language_code = None
language_name = None
character_ranges = None
reversed_specific_mapping = None

reversed_pre_processor_mapping_keys = []

reversed_specific_pre_processor_mapping = None
reversed_specific_pre_processor_mapping_keys = []

pre_processor_mapping_keys = ["zh", "ts"]

detectable = False
characters = None
reversed_characters = None

# Creating a translation table from the mapping set.
translation_table = {}

mapping = (
    "abvgdezijklmnoprstufhcC~y'wABVGDEZIJKLMNOPRSTUFHYW",
    "абвгдезийклмнопрстуфхцЦъыьъАБВГДЕЗИЙКЛМНОПРСТУФХЫЪ",
)

pre_processor_mapping = {
    "zh": u"ж",
    "ts": u"ц",
    "ch": u"ч",
    "sh": u"ш",
    "sss": u"щ",
    "ju": u"ю",
    "ja": u"я",
    "joo": u"ё",
    "Zh": u"Ж",
    "Ts": u"Ц",
    "Ch": u"Ч",
    "Sh": u"Ш",
    "Sss": u"Щ",
    "Ju": u"Ю",
    "Ja": u"Я",
    "Joo": u"Ё"
}

for key, val in zip(*mapping):
    translation_table.update({ord(key): ord(val)})


def translit(value):
    for rule in pre_processor_mapping.keys():
        value = value.replace(rule, pre_processor_mapping[rule])
    res = value.translate(translation_table)

    return res


if __name__ == '__main__':
    print(translit('zhopa'))
