# -*- coding: utf-8 -*-

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.ru import data


class RussianLanguagePack(TranslitLanguagePack):
    """Language pack for Russian language.

    See `http://en.wikipedia.org/wiki/Russian_alphabet` for details.
    """
    language_code = "il_ru"
    language_name = "Russian"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = data.mapping
    reversed_specific_mapping = data.reversed_specific_mapping
    pre_processor_mapping = data.pre_processor_mapping
    detectable = True


registry.register(RussianLanguagePack)
