from ...utils import normalise


YP_CONSONANTS = ['b', 'p', 'm', 'd', 't', 'n', 'l', 'z', 'c', 's', 'g', 'k', 'ng', 'h',
                 'w', 'j', 'nj']     # 連讀特有聲母, 不含 r (併入 l)

YP_VOWELS = ['a', 'o', 'e', 'oe', 'i', 'u', 'y']

YP_CODAS = ['ng', 'h', 'k', '']

YP_INITIALS = YP_CONSONANTS + ['']

# 韻母總表
# 甲類:
# 乙類: 不與 ng / 入聲結合的
# 丙類: 有變韻的
YP_FINALS = [
    # 陰聲韻 甲類
    'a', 'e', 'o', 'oe', 'ia', 'ie', 'ua', 'uo', 'yo',
    # 陰聲韻 乙類
    'au', 'ai', 'iau', 'uai', 'eu', 'ui', 'iu',
    # 陰聲韻 乙類 (不含和甲類重合的)
    'i', 'ei', 'u', 'ou', 'y', 'oey', 'oy',
    # 入聲韻 甲類
    'ah', 'ak', 'eh', 'oh', 'oeh', 'iah', 'iak', 'ieh', 'iek', 'uah', 'uak', 'uoh', 'uok', 'yoh', 'yok',
    # 入聲韻 丙類
    'ik', 'eik', 'ih', 'eih', 'aik', 'uk', 'ouk', 'auk', 'yk', 'oeyk', 'oyk',
    # 陽聲韻 甲類
    'ang', 'iang', 'ieng', 'uang', 'uong', 'yong',
    # 陽聲韻 丙類
    'ing', 'eing', 'aing', 'ung', 'oung', 'aung', 'yng', 'oeyng', 'oyng'
]

YP_TONES = [
    '55',    # 陰平
    '53',    # 陽平
    '33',    # 上聲
    '212',   # 陰去
    '242',   # 陽去
    '23',    # 陰入
    '5',     # 陽入
    '21',    # 半陰去
    '24'     # 半陽去
]


class YngPingSyllable:
    """
    新榕拼方案的音節. 根據 2/07/2018 子善發的使用手冊.
    """

    def __init__(self, initial, final, tone):
        """
        Constructor.
        :param initial:
        :param final:
        :param tone:
        """
        if initial not in set(YP_INITIALS):
            raise Exception('Unknown initial: %s' % initial)
        self.initial = initial
        if tone not in set(YP_TONES):
            raise Exception('Unknown tone: %s' % tone)
        self.tone = tone
        self.rime, self.coda = self.__parse_final(final)

    def __parse_final(self, s):
        """
        Parse a YngPing final from string.
        :param s: String containing the final to be parsed.
        :return:
        """
        if s not in set(YP_FINALS):
            raise Exception('Unknown final: %s' % s)
        sorted_codas = sorted(YP_CODAS, reverse=True, key=lambda x: len(x))
        for coda in sorted_codas:
            if s.endswith(coda):
                return (s[:-len(coda)] if coda != '' else s), coda
        raise Exception('No matching coda')

    def get_vowels(self):
        output = []
        sorted_vowels = sorted(YP_VOWELS, reverse = True, key = lambda x: len(x))
        tmp = self.rime
        while len(tmp) > 0:
            for v in sorted_vowels:
                if tmp.startswith(v):
                    output.append(v)
                    tmp = tmp[len(v):]
        return output

    def to_handwritten(self):
        """轉換爲手寫方案"""
        mappings = {
                #  無調  55   53   33  212  242   23   5    21   24
            'a':  ['a', 'a', 'à', 'ā', 'ǎ', 'â', 'á', 'a', 'ǎ', 'á'],
            'o':  ['o', 'o', 'ò', 'ō', 'ǒ', 'ô', 'ó', 'o', 'ǒ', 'ó'],
            'e':  ['e', 'e', 'è', 'ē', 'ě', 'ê', 'é', 'e', 'ě', 'é'],
            'oe': ['ë', 'ë', 'ë̀', 'ë̄', 'ë̌', 'ë̂', 'ë́', 'ë', 'ë̌', 'ë́'],
            'i':  ['i', 'i', 'ì', 'ī', 'ǐ', 'î', 'í', 'i', 'ǐ', 'í'],
            'u':  ['u', 'u', 'ù', 'ū', 'ǔ', 'û', 'ú', 'u', 'ǔ', 'ú'],
            'y':  ['ü', 'ü', 'ǜ', 'ǖ', 'ǚ', 'ü̂', 'ǘ', 'ü', 'ǚ', 'ǘ']
        }

        # 元音帶調號的優先次序
        tone_priority = [
            'a', 'o', 'e', 'u', 'i', 'oe', 'y'
        ]

        vowels = self.get_vowels()

        vowel_with_tone = None
        for t in tone_priority:
            if t in vowels:
                vowel_with_tone = t
                break

        tone_order = YP_TONES.index(self.tone) + 1

        rime = "".join([
            mappings[v][0] if v != vowel_with_tone else mappings[v][tone_order]
            for v in vowels
        ])

        return normalise(self.initial + rime + self.coda)

    def to_typing(self):
        return self.initial + self.rime + self.coda + self.tone

    def __str__(self):
        return 'YngPingSyllable Initial=%s Rime=%s Coda=%s Tone=%s' % (self.initial, self.rime, self.coda, self.tone)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_string(cls, s):
        s = normalise(s).strip().lower()

        tone = None
        for t in YP_TONES:
            if s.endswith(t):
                tone = t
                s = s[:-len(t)]
                break
        if tone is None:
            raise Exception('No matching tone.')

        sorted_initials = sorted(YP_INITIALS, reverse=True, key=lambda x: len(x))
        initial = None
        for i in sorted_initials:
            if s.startswith(i):
                initial = i
                s = s[len(i):]
                break

        if initial is None:
            raise Exception('No matching initial')

        return YngPingSyllable(initial, s, tone)
