from .models.historical.CikLinSyllable import CikLinSyllable
from .models.historical.FoochowRomanized import FoochowRomanizedSyllable
from .models.historical.HectorScheme import HectorSyllable
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

def foochow_romanized_to_yngping(f: FoochowRomanizedSyllable):
    INITIAL_MAPPING = ['l', 'b', 'g', 'k', 'd',
                       'p', 't', 'z', 'n', 's',
                       '' , 'm','ng','c', 'h']
    FINAL_MAPPING  = [
        #   1       2      3       4      5       7      8     FR
        #  55       33    212     23     53      242     5     YP
        ['ung',  'ung', 'oung', 'ouk', 'ung',  'oung', 'uk'],  # 春
        ['ua',   'ua',  'ua',   'uah', 'ua',   'ua',   'uah'], # 花
        ['yong', 'yong','yong', 'yok', 'yong', 'yong', 'yok'], # 香 
        ['iu',   'iu',  'iu',   'iuh', 'iu',   'iu',   None],  # 秋
        ['ang',  'ang', 'ang',  'ak',  'ang',  'ang',  'ak'],  # 山
        ['ai',   'ai',  'ai',   'aih', 'ai',   'ai',   'aih'], # 開
        ['a',    'a',   'a',    'ah',  'a',    'a',    'ah'],  # 嘉 
        ['ing',  'ing', 'eing', 'eik', 'ing',  'eing', 'ik'],  # 賓
        ['uang', 'uang','uang', 'uak', 'uang', 'uang', 'uak'], # 歡
        ['o',    'o',   'o',    'oh',  'o',    'o',    'oh'],  # 歌
        ['y',    'y',   'oey',  'oeyk','y',    'oey',  'yk'],  # 須
        ['ui',   'ui',  'ui',   'uih', 'ui',   'ui',   None],  # 杯
        ['u',    'u',   'ou',   'ouh', 'u',    'ou',   'uh'],  # 孤
        ['eing', 'eing','aing', 'aik', 'eing', 'aing', 'eik'], # 燈
        ['uong', 'uong','uong', 'uok', 'uong', 'uong', 'uok'], # 光
        ['ui',   'ui',  'ui',   'uih', 'ui',   'ui',   'uih'], # 輝
        ['iu',   'iu',  'iu',   'iuh', 'iu',   'iu',   None],  # 燒
        ['yng',  'yng', 'oeyng','oeyk','yng',  'oeyng','yk'],  # 銀
        ['oung', 'oung','aung', 'auk', 'oung', 'aung', 'ouk'], # 缸
        ['i',    'i',   'ei',   'eih', 'i',    'ei',   'ih'],  # 之
        ['oeyng','oeyng','oyng','oyk', 'oeyng','oyng', 'oeyk'],# 東
        ['au',   'au',  'au',   'auh' ,'au',   'au',   'auh'], # 郊
        ['uo',   'uo',  'uo',   'uoh', 'uo',   'uo',   'uoh'], # 過
        ['e',    'e',   'a',    'ah',  'e',    'a',    'eh'],  # 西
        ['yo',   'yo',  'yo',   'yoh', 'yo',   'yo',   'yoh'], # 橋
        ['ie',   'ie',  'ie',   'ieh', 'ie',   'ie',   'ieh'], # 鷄
        ['iang', 'iang','iang', 'iak', 'iang', 'iang', 'iak'], # 聲
        ['oey',  'oey',  'oy',  'oyh', 'oey',  'oy',   'oeyh'],# 催
        ['oe',   'oe',   'o',   'oeh', 'oe',   'o',    'oeh'], # 初
        ['ieng', 'ieng','ieng', 'iek', 'ieng', 'ieng', 'iek'], # 天
        ['ia',   'ia',  'ia',   'ieh', 'ia',   'ia',   'ieh'], # 奇
        ['uai',  'uai', 'uai',  'uaih','uai',  'uai',  'uaih'],# 歪  
        ['eu',   'eu',  'au',   'auh', 'eu',   'au',   'euh']  # 溝  
    ]
    FINAL_MAPPING_IO_UO = {
        24: ['uo',   'uo',  'uo',   'uoh', 'uo',   'uo',   'uoh'],
        2:  ['uong', 'uong','uong', 'uok', 'uong', 'uong', 'uok']
    }
    TONE_MAPPING = {
        1: "55",
        2: "33",
        3: "212",
        4: "23",
        5: "53",
        6: "33",
        7: "242",
        8: "5"
    }
    ypInitial = INITIAL_MAPPING[f.initial]
    toneIndex = FoochowRomanizedSyllable.TONE_MAPPING[f.tone]
    if ypInitial not in ['','g','k','h','ng'] and f.final in [2, 24]: #香 / 橋
        # 漳泉亂 
        ypFinal = FINAL_MAPPING_IO_UO[f.final][toneIndex]
    else:
        ypFinal = FINAL_MAPPING[f.final][toneIndex]
    ypTone = TONE_MAPPING[f.tone]
    return YngPingSyllable(ypInitial, ypFinal, ypTone)

def hector_to_foochow_romanized(s):
    h = HectorSyllable.from_string(s)
    return FoochowRomanizedSyllable(h.initial,h.final,h.tone)

def hector_to_foochow_romanized_string(s):
    return hector_to_foochow_romanized(s).get_string()

def hector_to_yngping(s):
    f = hector_to_foochow_romanized(s)
    return foochow_romanized_to_yngping(f).to_typing()

def foochow_romanized_to_yngping_string(s, allow_omit_ingbing=False):
    return foochow_romanized_to_yngping(FoochowRomanizedSyllable.from_string(s,allow_omit_ingbing)).to_typing()

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

