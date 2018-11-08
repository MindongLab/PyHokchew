from ...utils import normalise

MJ_CONSONANTS = ['b', 'p', 'm', 'd', 't', 'n', 'l', 'z', 'c', 's', 'g', 'k', 'ng', 'h']

MJ_VOWELS = ['a', 'o', 'e', 'ë', 'i', 'u', 'ü']

MJ_CODAS = ['ng', 'h', 'k', '']

MJ_INITIALS = MJ_CONSONANTS + ['']

TONE_MAPPINGS = {
    "1": "55",
    "2": "53",
    "3": "33",
    "4": "212",
    "5": "242",
    "6": "23",
    "7": "5"
}

MJ_TONES = list(TONE_MAPPINGS.keys())

def normalise_mj(s):
    # 正規化閩江學院的奇怪字符
    s = normalise(s).strip().lower()
    s = s.replace('ɑ','a').replace('ê','e').replace('ɡ','g')
    return s

# Tones
# 55	1
# 53	2
# 33	3
# 212	4
# 242	5
# 23	6
# 5	    7

class MinjiangSyllable:
    """閩江學院的拼音方案
    """

    def __init__(self, initial, final, tone):
        """
        """
        if initial not in set(MJ_INITIALS):
            raise Exception('Unknown initial: %s' % initial)
        self.initial = initial
        self.final = final
        self.tone = tone

    def __str__(self):
        return 'MinjiangSyllable Initial=%s Final=%s Tone=%s' % (self.initial, self.final, self.tone)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_string(cls, s):
        s = normalise_mj(s)

        # 需要先 match 較長的
        sorted_initials = sorted(MJ_INITIALS, reverse=True, key=lambda x: len(x))
        initial = None
        for i in sorted_initials:
            if s.startswith(i):
                initial = i
                s = s[len(i):]
                break

        if initial is None:
            raise Exception('No matching initial')

        rime = None
        sorted_vowels = sorted(MJ_VOWELS, reverse=True, key=lambda x: len(x))

        while True:
            found = False
            for v in sorted_vowels:
                if s.startswith(v):
                    rime = v if rime is None else rime + v
                    s = s[len(v):]
                    found = True                
                    break
            if not found:
                break
        
        if rime is None:
            raise Exception('No matching final')
        
        coda = None

        for c in MJ_CODAS:
            if s.startswith(c):
                coda = c
                s = s[len(c):]
                break

        if coda is None:
            raise Exception('No matching final')
        
        # the rest is the tone
        tone = None
        if s in MJ_TONES:
            tone = TONE_MAPPINGS[s]

        if tone is None:
            raise Exception('No matching tone.')

        return MinjiangSyllable(initial, rime+coda, tone)
