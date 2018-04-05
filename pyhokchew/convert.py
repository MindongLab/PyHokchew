from .models.CikLinSyllable import CikLinSyllable
from .models.FoochowRomanized import FoochowRomanizedSyllable

def foochow_romanized_to_ciklin(f):
    ciklin_syllable = CikLinSyllable(f.initial,f.final,f.tone)
    return ciklin_syllable


def ciklin_to_foochow_romanized(c):
    fr_syllable = FoochowRomanizedSyllable(c.initial, c.final, c.tone)
    return fr_syllable
