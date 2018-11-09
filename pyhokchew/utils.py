import unicodedata


def normalise(s) -> str:
    """
    Normalise the Foochow Romanized string, by replacing combining characters with a combined character.
     ['e', '̤', '́', 'u', '̤', 'k'] normalize ---> ['é', '̤', 'ṳ', 'k']
    :param s: The original string to be normalized.
    :return: string
    """
    return unicodedata.normalize('NFKC', s)


def denormalise(s) -> str:
    return unicodedata.normalize('NFKD', s)

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')