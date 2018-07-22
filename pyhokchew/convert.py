from .models.CikLinSyllable import CikLinSyllable
from .models.FoochowRomanized import FoochowRomanizedSyllable


def foochow_romanized_to_ciklin(f):
    ciklin_syllable = CikLinSyllable(f.initial,f.final,f.tone)
    return ciklin_syllable

def ciklin_to_foochow_romanized(c):
    fr_syllable = FoochowRomanizedSyllable(c.initial, c.final, c.tone)
    return fr_syllable

def ciklin_to_foochow_romanized_string(cInitial, cFinal, cTone):
    """Converts a QiLinBaYin Fanqie character to Foochow Romanized
    :param cInitial: The initial (反切上字). E.g. 柳. Only Traditional Chinese characters are supported.
    :param cFinal: The final (反切下字). E.g. 春. Only Traditional Chinese characters are supported.
    :param cTone: The tone name in QiLinBaYin. E.g. 上平, 下去.
    :return: The converted Foochow Romanized string.
    """
    return ciklin_to_foochow_romanized(CikLinSyllable.from_ciklin_string(cInitial+cFinal,cTone)).get_string()
