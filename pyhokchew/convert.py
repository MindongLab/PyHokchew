from .models.historical.CikLinSyllable import CikLinSyllable
from .models.historical.FoochowRomanized import FoochowRomanizedSyllable
from .models.concurrent.matsu import WuyixingSyllable
from .models.concurrent.minjiang import MinjiangSyllable
from .models.yngping.YngPingTwo import YngPingSyllable

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


def wuyixing_to_yngping(s):
    """從烏衣行轉換爲榕拼方案
    """
    wyx = WuyixingSyllable.from_string(s)
    INITIAL_MAPPING = {
        'p': 'b',
        'ph':'p',
        't' :'d',
        'th':'t',
        'ts': 'z',
        'tsh': 'c',
        'k':'g',
        'kh':'k',
    }

    FINAL_MAPPING = {
        # TODO: 榕拼無?
        'ieu': 'iu'
    }
    
    return YngPingSyllable(
        INITIAL_MAPPING[wyx.initial] if wyx.initial in INITIAL_MAPPING.keys() else wyx.initial,
        FINAL_MAPPING[wyx.final] if wyx.final in FINAL_MAPPING.keys() else wyx.final, 
        wyx.tone).to_typing()


def minjiang_to_yngping(s):
    """從閩江學院轉換爲榕拼方案
    """
    mj = MinjiangSyllable.from_string(s)


    FINAL_MAPPING = {
        # TODO: 榕拼無?
        'ieu': 'iu'
    }

    VOWEL_MAPPING = {
        'ë': 'oe',
        'ü': 'y'
    }

    final = mj.final
    for v in VOWEL_MAPPING.keys():
        nv = VOWEL_MAPPING[v]
        final = final.replace(v,nv)
    
    return YngPingSyllable(
        mj.initial,
        final,
        mj.tone).to_typing()