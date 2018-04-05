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
    def __init__(self, initial, final, tone):
        if not(initial in range(len(INITIALS_CEIK)) and final in range(len(FINALS_CEIK)) and tone in [1,2,3,4,5,7,8]):
            raise ValueError('Invalid CikLin syllable arguments.')
        self.initial = initial
        self.final = final
        self.tone = tone
    
    def __str__(self):
        i = INITIALS_CEIK[self.initial]
        f = FINALS_CEIK[self.final]
        t = TONE_NAMES[self.tone-1]
        return "%s%s切 %s" % (i,f,t)