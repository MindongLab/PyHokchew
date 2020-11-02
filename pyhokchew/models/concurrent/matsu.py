
from ...utils import normalise

WYX_CONSONANTS = ['p', 'ph', 'm', 't', 'th', 'n', 'l', 'ts', 'tsh', 's', 'k', 'kh', 'ng', 'h']

WYX_VOWELS = ['a', 'o', 'e', 'oe', 'i', 'u', 'y']

WYX_CODAS = ['ng', 'h', 'k', '']

WYX_INITIALS = WYX_CONSONANTS + ['']


# Tones
# 55	
# 53	s
# 33	f
# 212	v
# 242	x
# 23	z
# 5	

class WuyixingSyllable:
    """烏衣行馬祖話輸入法的拼音方案
    """

    def __init__(self, initial, final, tone):
        """
        """
        if initial not in set(WYX_INITIALS):
            raise Exception('Unknown initial: %s' % initial)
        self.initial = initial
        self.final = final
        self.tone = tone

    def __str__(self):
        return 'WuyixingSyllable Initial=%s Final=%s Tone=%s' % (self.initial, self.final, self.tone)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_string(cls, s):
        s = normalise(s).strip().lower()

        # 需要先 match 較長的
        sorted_initials = sorted(WYX_INITIALS, reverse=True, key=lambda x: len(x))
        initial = None
        for i in sorted_initials:
            if s.startswith(i):
                initial = i
                s = s[len(i):]
                break

        if initial is None:
            raise Exception('No matching initial')

        rime = None
        sorted_vowels = sorted(WYX_VOWELS, reverse=True, key=lambda x: len(x))

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

        for c in WYX_CODAS:
            if s.startswith(c):
                coda = c
                s = s[len(c):]
                break

        if coda is None:
            raise Exception('No matching final')
        
        # the rest is the tone
        tone = None
        if s == "":
            if coda in ['h', 'k']:
                tone = "5"
            else:
                tone = "55"
        elif s == "s":
            tone = "53"
        elif s == "f":
            tone = "33"
        elif s == "v":
            tone = "212"
        elif s == "x":
            tone = "242"
        elif s == "z":
            if coda in ['h', 'k']:
                tone = "23"

        if tone is None:
            raise Exception('No matching tone.')

        return WuyixingSyllable(initial, rime+coda, tone)
