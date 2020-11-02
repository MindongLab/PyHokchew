from ...utils import normalise

HT_INITIALS = ['l', 'b', 'g', 'k', 'd',
               'p', 't', 'z', 'n', 's',
               '' , 'm','ng', 'c', 'h']

HT_FINALS  = [
    #   春      花      香      秋      山
    'ung',   'ua','iong',   'iu',  'ang',
    #   開      嘉      賓      歡      歌
    'ai' ,    'a', 'ing', 'uang',    'o',
    #   須      杯      孤      燈      光
    'y'  ,  'uoi',   'u',  'eng', 'uong',
    #   輝      燒      銀      缸      之
    'ui' ,  'ieu', 'yng',  'ong',    'i',
    #   東      郊      過      西      橋
    'oeng',  'au',  'uo',    'e',   'io',
    #   鷄      聲      催      初      天
    'ie',  'iang',  'oi',   'oe',  'ieng',
    #   奇      歪      溝
    'ia',  'uai',   'eu'
    # TODO 桸𤬣 ya
]

# 入聲
HT_FINALS_RU = [
    #   春      花      香      秋      山
    'uk' ,  'uah', 'iok',  'iuh',   'ak',
    #   開      嘉      賓      歡      歌
    'aih',   'ah',  'ik',  'uak',   'oh',
    #   須      杯      孤      燈      光
    'yh' , 'uoih',  'uh',   'ek',  'uok',
    #   輝      燒      銀      缸      之
    'uih', 'ieuh',  'yk',   'ok',   'ih',
    #   東      郊      過      西      橋
    'oek',  'auh', 'uoh',   'eh',  'ioh',
    #   鷄      聲      催      初      天
    'ieh',  'iak', 'oih',  'oeh',  'iek',
    #   奇      歪      溝
    'iah', 'uaih', 'euh'
]

class HectorSyllable:
    """
    only3km 的擬音code.
    https://github.com/only3km/ciklinbekin/blob/gh-pages/convert.tsv
    """
    TONE_MAPPING_REVERSE = [1,2,3,4,5,7,8]

    def __init__(self, initial, final, tone):
        if not (initial in range(len(HT_INITIALS)) and final in range(len(HT_FINALS)) \
                and tone in self.TONE_MAPPING_REVERSE):
            raise ValueError("Invalid syllable arguments.")

        self.initial = initial
        self.final = final
        self.tone = tone
        pass

    def __str__(self):
        return "HectorSyllable " + self.get_string() + \
               " [Initial=%d Final=%d Tone=%d]" % (self.initial, self.final, self.tone)

    def __repr__(self):
        return self.__str__()

    def get_initial(self):
        """
        Gets the initial of the syllable.
        獲取該音節的聲母.
        :return:
        """
        return HT_INITIALS[self.initial]

    def get_final(self):
        """
        Gets the final of the syllable without tonal marks.
        獲取該音節的韻母.
        :return:
        """
        return HT_FINALS_RU[self.final] if self.tone in [4,8] else HT_FINALS[self.final]

    def get_tone(self):
        """
        Gets the tone number.
        獲取該音節的聲調.
        :return:
        """
        return self.tone

    def get_string(self):
        return self.get_initial() + \
            self.get_final() + \
            str(self.tone)

    @classmethod
    def from_string(cls, s):
        """
        """
        s = normalise(s).strip().lower()

        # Try parse initial
        initials_list = sorted(HT_INITIALS, key = lambda x: len(x), reverse= True) # Longer matches first

        for i in initials_list:
            if s.startswith(i):
                initial = HT_INITIALS.index(i)
                remaining = s[len(i):]
                break

        # Try tone
        tone = None
        toneStr = remaining[-1:]
        remaining = remaining[:-1]
        try:
            tone = int(toneStr)
        except:
            raise ValueError("%s is not a valid Hector syllable: unknown tone")

        # Try parse final
        if remaining in HT_FINALS:
            final = HT_FINALS.index(remaining)
        elif remaining in HT_FINALS_RU and tone in [4,8]:
            final = HT_FINALS_RU.index(remaining)
        else:
            raise ValueError("%s is not a valid Hector syllable: %s not found in finals. " \
                                % (s, remaining))

        return cls(initial, final, tone)
