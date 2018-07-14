from ..utils import normalise

# All possible initials of Foochow Romanized
# 所有可能的福州話羅馬字聲母
FR_INITIALS = ['l', 'b', 'g', 'k', 'd',
               'p', 't', 'c', 'n', 's',
               '' , 'm','ng','ch', 'h']

# All possible finals of Foochow Romanized
# 所有可能的福州話羅馬字韻母
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

# List of all possible finals in Foochow Romanized, without tonal marks.
FR_FINALS_LIST = list(FR_FINALS.keys())

# Mapping of an final with tone to a tuple (final without tone, tone number)
FR_FINALS_MAPPING = {}
for i, rime in enumerate(FR_FINALS_LIST):
    sub_rimes = FR_FINALS[rime]       # 小韻
    for j in range(0, len(sub_rimes)):
        if (sub_rimes[j] != None):
            if (sub_rimes[j] in FR_FINALS_MAPPING):
                raise Exception(sub_rimes[j] + "already exists")
            FR_FINALS_MAPPING[sub_rimes[j]] = (i,j)


class FoochowRomanizedSyllable:
    """
    Representation of a Foochow Romanized syllable.
    代表一個福州話羅馬字音節.
    """
    TONE_MAPPING = [-1, 0, 1, 2, 3, 4, 1, 5, 6]
    TONE_MAPPING_REVERSE = [1,2,3,4,5,7,8]

    def __init__(self, initial, final, tone):
        if not (initial in range(len(FR_INITIALS)) and final in range(len(FR_FINALS_LIST)) \
                and tone in self.TONE_MAPPING_REVERSE):
            raise ValueError("Invalid syllable arguments.")

        self.initial = initial
        self.final = final
        self.tone = tone
        pass

    def __str__(self):
        return "FR Syllable " + self.get_string() + \
               " [Initial=%d Final=%d Tone=%d]" % (self.initial, self.final, self.tone)

    def __repr__(self):
        return self.__str__()

    def get_initial(self):
        """
        Gets the initial of the Foochow Romanized syllable.
        獲取該音節的聲母.
        :return:
        """
        return FR_INITIALS[self.initial]

    def get_final_without_tone(self):
        """
        Gets the final of the Foochow Romanized without tonal marks.
        獲取該音節的韻母, 不含調號.
        :return:
        """
        return FR_FINALS_LIST[self.final]

    def get_final_with_tone(self):
        """
        Gets the final of the Foochow Romanized with the tonal mark.
        獲取該音節的韻母, 帶調號.
        :return:
        """
        return FR_FINALS[FR_FINALS_LIST[self.final]][self.TONE_MAPPING[self.tone]]

    def get_tone(self):
        """
        Gets the tone number.
        獲取該音節的聲調.
        :return:
        """
        return self.tone

    def get_string(self):
        return FR_INITIALS[self.initial] + \
            FR_FINALS[
                FR_FINALS_LIST[self.final]
            ] \
            [
                self.TONE_MAPPING[self.tone]
            ]

    @classmethod
    def from_string(cls, s, allow_omit_ingbing = False):
        """
        Parse a Foochow Romanized syllable from a string.
        :param s: A single Foochow Romanized syllable string.
        :param allow_omit_ingbing: 允許上平聲調號省略。
            See: https://cdo.wikipedia.org/wiki/%E5%B9%AB%E5%8A%A9:Ci%C5%8Fng-i%C3%B4ng_t%C4%95%CC%A4k#%E5%B0%8D%E6
            %95%99%E6%9C%83%E5%B9%B3%E8%A9%B1%E5%AD%97%E6%94%B9%E9%80%B2%E7%9A%84%E6%84%8F%E8%A6%8B
        """
        s = normalise(s).strip().lower()

        # Try parse initial
        initials_list = sorted(FR_INITIALS, key = lambda x: len(x), reverse= True) # Longer matches first

        for i in initials_list:
            if s.startswith(i):
                initial = FR_INITIALS.index(i)
                remaining = s[len(i):]
                break

        # Try parse final
        if remaining in FR_FINALS_MAPPING:
            mapping = FR_FINALS_MAPPING[remaining]
            final = mapping[0]
            tone = FoochowRomanizedSyllable.TONE_MAPPING_REVERSE[mapping[1]]
        else:
            if (allow_omit_ingbing):
                # 允許上平調省略
                try:
                    final = FR_FINALS_LIST.index(remaining)
                    tone = 1
                except ValueError:
                    raise ValueError("%s is not a valid Foochow Romanized syllable: %s not found in finals. " \
                                     % (s, remaining))
            else:
                raise ValueError("%s is not a valid Foochow Romanized syllable: %s not found in finals. " \
                                 % (s, remaining))

        return FoochowRomanizedSyllable(initial, final, tone)
