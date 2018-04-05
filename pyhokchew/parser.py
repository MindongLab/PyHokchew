from .models.CikLinSyllable import CikLinSyllable
from .models.FoochowRomanized import parse_foochow_romanized

def parse_ciklin(fanqie,tone):
    return CikLinSyllable.parse_ciklin_string(fanqie, tone)