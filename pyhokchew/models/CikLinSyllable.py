FINALS_CEIK = ['春','花','香','秋','山','開','嘉','賓','歡','歌',
               '須','杯','孤','燈','光','輝','燒','銀','釭','之',
               '東','郊','過','西','橋','雞','聲','催','初','天',
               '奇','歪','溝']

FINALS_LING = ['公','瓜','姜','周','干','哉','佳','京','官','高',
               '車','盃','姑','庚','光','龜','嬌','恭','綱','箕',
               '江','交','朱','街','嬝','圭','正','催','梳','堅',
               '迦','乖','勾','𤬣','伓']

INITIALS_CEIK = ['柳','邊','求','氣','低','波','他','曾','日','時',
                 '鶯','蒙','語','出','非']

INITIALS_LING = ['柳','邊','求','悉','聲','波','皆','之','女','授',
                 '亦','美','鳥','出','風']


TONE_NAMES = ['上平','上上','上去','上入','下平','下上','下去','下入']

class CikLinSyllable():
    """
    Presentation of a 戚林八音 syllable.
    """
    def __init__(self, initial, final, tone):
        if not(initial in range(len(INITIALS_CEIK)) and final in range(len(FINALS_CEIK)) and tone in range(1,9)):
            raise ValueError('Invalid CikLin syllable arguments.')
        self.initial = initial
        self.final = final
        self.tone = tone
        if self.tone == 6:
            self.tone = 2
    
    def __str__(self):
        i = INITIALS_CEIK[self.initial]
        f = FINALS_CEIK[self.final]
        t = TONE_NAMES[self.tone-1]
        return "%s%s切 %s" % (i,f,t)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_ciklin_string(cls, fanqie, tone_name):
        """
        解析戚林八音反切字.
        """
        fanqie = fanqie.strip()
        if fanqie.endswith('切'):
            fanqie = fanqie[:-1]
        
        def safe_index(the_list, item_to_find):
            try:
                return the_list.index(item_to_find)
            except ValueError:
                return -1

        def find(str_to_find, ceik, ling):
            if (safe_index(ceik, str_to_find)!=-1):
                return ceik.index(str_to_find)
            elif (safe_index(ling, str_to_find)!=-1):
                return ling.index(str_to_find)
            else:
                return None

        if (len(fanqie) not in [2,3,4]):
            raise ValueError("Invalid fanqie: "+fanqie)
        
        found = False
        for i in range(0, len(fanqie)-1):
            first = fanqie[:i+1]
            second = fanqie[i+1:]
            if len(first) > 1:
                initial = find(first[0], INITIALS_CEIK, INITIALS_LING) or find(first[1], INITIALS_CEIK, INITIALS_LING)
            else:
                initial = find(first, INITIALS_CEIK, INITIALS_LING)
            if len(second) > 1:
                final = find(second[0], FINALS_CEIK, FINALS_LING) or find(second[1], FINALS_CEIK, FINALS_LING)
            else:
                final = find(second, FINALS_CEIK, FINALS_LING)
            if (initial != None and final != None):
                found = True
                break
        if (not found):
            raise ValueError("Invalid fanqie: "+ fanqie)
        
        tone_id = safe_index(TONE_NAMES, tone_name.strip())
        
        if (tone_id == -1):
            raise ValueError("Invalid tone name: "+ tone_name)

        return CikLinSyllable(initial, final, tone_id+1)

