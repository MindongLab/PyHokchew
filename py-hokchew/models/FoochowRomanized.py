import unicodedata

FR_INITIALS = ['l', 'b', 'g', 'k', 'd',
               'p', 't', 'c', 'n', 's',
               '' , 'm','ng','ch', 'h']
 
FR_FINALS  = {
    'ung':  ['ŭng',  'ūng', 'óng',  'ók',  'ùng',  'ông',  'ŭk'],  # 春
    'ua':   ['uă',   'uā',  'uá',   'uáh', 'uà',   'uâ',   'uăh'], # 花
    'iong': ['iŏng', 'iōng','ióng', 'iók', 'iòng', 'iông', 'iŏk'], # 香 
    'iu':   ['iŭ',   'iū',  'éu',   'éuh', 'iù',   'êu',   None],  # 秋
    'ang':  ['ăng',  'āng', 'áng',  'ák',  'àng',  'âng',  'ăk'],  # 山
    'ai':   ['ăi',   'āi',  'ái',   'áih', 'ài',   'âi',   'ăih'], # 開
    'a':    ['ă',    'ā',   'á',    'áh',  'à',    'â',    'ăh'],  # 嘉 
    'ing':  ['ĭng',  'īng', 'éng',  'ék',  'ìng',  'êng',  'ĭk'],  # 賓
    'uang': ['uăng', 'uāng','uáng', 'uák', 'uàng', 'uâng', 'uăk'], # 歡
    'o̤' :   ['ŏ̤',    'ō̤',   'ó̤',    'ó̤h',  'ò̤',    'ô̤',    'ŏ̤h'],  # 歌
    'ṳ':    ['ṳ̆',    'ṳ̄',   'é̤ṳ',   'é̤ṳh', 'ṳ̀',    'ê̤ṳ',   'ṳ̆h'],  # 須
    'uoi':  ['uŏi',  'uōi', 'uói',  'uóih','uòi',  'uôi',  None],  # 杯
    'u':    ['ŭ',    'ū',   'ó',    'óh',  'ù',    'ô',    'ŭh'],  # 孤
    'eng':  ['ĕng',  'ēng', 'áing', 'áik', 'èng',  'âing', 'ĕk'],  # 燈
    'uong': ['uŏng', 'uōng','uóng', 'uók', 'uòng', 'uông', 'uŏk'], # 光
    'ui':   ['ŭi',   'ūi',  'ói',   'óih', 'ùi',   'ôi',   'ŭih'], # 輝
    'ieu':  ['iĕu',  'iēu', 'iéu',  'iéuh','ièu',  'iêu',  None],  # 燒
    'ṳng':  ['ṳ̆ng',  'ṳ̄ng', 'é̤ṳng', 'é̤ṳk', 'ṳ̀ng',  'ê̤ṳng', 'ṳ̆k'],  # 銀
    'ong':  ['ŏng',  'ōng', 'áung', 'áuk', 'òng',  'âung', 'ŏk'],  # 缸
    'i':    ['ĭ',    'ī',   'é',    'éh',  'ì',    'ê',    'ĭh'],  # 之
    'e̤ng':  ['ĕ̤ng',  'ē̤ng', 'áe̤ng', 'áe̤k', 'è̤ng',  'âe̤ng', 'ĕ̤k'],  # 東
    'au':   ['ău',   'āu',  'áu',   'áuh' ,'àu',   'âu',   'ăuh'], # 郊
    'uo':   ['uŏ',   'uō',  'uó',   'uóh', 'uò',   'uô',   'uŏh'], # 過
    'a̤':    ['ă̤',    'ā̤',   'á̤',    'á̤h',  'à̤',    'â̤',    'ă̤h'],  # 西
    'io':   ['iŏ',   'iō',  'ió',   'ióh', 'iò',   'iô',   'iŏh'], # 橋
    'ie':   ['iĕ',   'iē',  'ié',   'iéh', 'iè',   'iê',   'iĕh'], # 鷄
    'iang': ['iăng', 'iāng','iáng', 'iák', 'iàng', 'iâng', 'iăk'], # 聲
    'oi':   ['ŏi',   'ōi',  'ó̤i',   'ó̤ih', 'òi',   'ô̤i',   'ŏih'], # 催
    'e̤':    ['ĕ̤',    'ē̤',   'áe̤',   'áe̤h', 'è̤',    'âe̤',   'ĕ̤h'],  # 初
    'ieng': ['iĕng', 'iēng','iéng', 'iék', 'ièng', 'iêng', 'iĕk'], # 天
    'ia':   ['iă',   'iā',  'iá',   'iáh', 'ià',   'iâ',   'iăh'], # 奇
    'uai':  ['uăi',  'uāi', 'uái',  'uáih','uài',  'uâi',  'uăih'],# 歪  
    'eu':   ['ĕu',   'ēu',  'áiu',  'áiuh','èu',   'âiu',  'ĕuh']  # 溝  
}

FR_FINALS_LIST = list(FR_FINALS.keys())

FR_FINALS_MAPPING = {}
for i, rime in enumerate(FR_FINALS_LIST):
    sub_rimes = FR_FINALS[rime]
    for j in range(0, len(sub_rimes)):
        if (sub_rimes[j] != None):
            if (sub_rimes[j] in FR_FINALS_MAPPING):
                raise Exception(sub_rimes[j]+"already exists")
            FR_FINALS_MAPPING[sub_rimes[j]] = (i,j)

#print(FR_FINALS_MAPPING)


def normalise_buc(s):
    return unicodedata.normalize('NFKC',s)

class FoochowRomanizedSyllable:
    TONE_MAPPING = [-1, 0, 1, 2, 3, 4, 1, 6, 7]
    TONE_MAPPING_REVERSE = [1,2,3,4,5,7,8]

    def __init__(self, initial, final, tone):
        if not (initial in range(len(FR_INITIALS)) and final in range(len(FR_FINALS_LIST)) and tone in self.TONE_MAPPING_REVERSE):
            raise ValueError("Invalid syllable arguments.")

        self.initial = initial
        self.final = final
        self.tone = tone

        pass

    def __str__(self):
        result = FR_INITIALS[self.initial] + FR_FINALS[FR_FINALS_LIST[self.final]][self.TONE_MAPPING[self.tone]]
        return "FR Syllable " + result + " [Initial=%d Final=%d Tone=%d]" % (self.initial, self.final, self.tone)


def parse_foochow_romanized(s):
    s = normalise_buc(s)
    # Try parse initial
    initials_list = sorted(FR_INITIALS, key = lambda x: len(x), reverse= True) # Longer matches first
    
    for i in initials_list:
        if (s.startswith(i)):
            initial = FR_INITIALS.index(i)
            remaining = s[len(i):]
            break
    
    # Try parse final
    if remaining in FR_FINALS_MAPPING:
        mapping = FR_FINALS_MAPPING[remaining]
        final = mapping[0]
        tone = FoochowRomanizedSyllable.TONE_MAPPING_REVERSE[mapping[1]]
    else:
        raise ValueError("%s is not a valid Foochow Romanized syllable: %s not found in finals. " % (s, remaining))
    
    return FoochowRomanizedSyllable(initial, final, tone)
