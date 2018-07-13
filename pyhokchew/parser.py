from .models.CikLinSyllable import CikLinSyllable
from .models.FoochowRomanized import FoochowRomanizedSyllable

def parse_ciklin(fanqie, tone):
    return CikLinSyllable.from_ciklin_string(fanqie, tone)

def parse_foochow_romanized_phrase(phrase, allow_omit_ingbing = True):
    """Parse a dash-separated phrase / word in Foochow Romanized."""
    syllables = phrase.strip().split('-')

    result = []
    for syllable in syllables:
        try:
            parsed = FoochowRomanizedSyllable.from_string(syllable, allow_omit_ingbing)
            result.append(parsed)
        except:
            raise ValueError("%s is not a valid Foochow Romanized syllable.", syllable)
    return result
