def translit(value, language_code=None, reversed=False, strict=False):
    """Transliterate the text for the language given.

    Language code is optional in case of reversed translations (from some
    script to latin).

    :param str value:
    :param str language_code:
    :param bool reversed: If set to True, reversed translation is made.
    :param bool strict: If given, all that are not found in the
        transliteration pack, are simply stripped out.
    :return str:
    """
    ensure_autodiscover()

    if language_code is None and reversed is False:
        raise LanguageCodeError(
            _("``language_code`` is optional with ``reversed`` set to True "
              "only.")
        )

    if language_code is None:
        language_code = detect_language(value, fail_silently=False)

    cls = registry.get(language_code)

    if cls is None:
        raise LanguagePackNotFound(
            _("Language pack for code %s is not found." % language_code)
        )

    language_pack = cls()
    return language_pack.translit(value, reversed=reversed, strict=strict)
