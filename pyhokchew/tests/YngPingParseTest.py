import unittest
from ..models.yngping.YngPingTwo import YngPingSyllable
from ..utils import normalise


class YngPingParseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_yngping_should_parse_open_syllable(self):
        """測試基本的 YngPing 鍵入方案解析. 無韻尾. """
        s = YngPingSyllable.from_string('ba242')
        self.assertEqual(s.initial, 'b')
        self.assertEqual(s.rime, 'a')
        self.assertEqual(s.coda, '')
        self.assertEqual(s.tone, '242')
        s = YngPingSyllable.from_string('nga242')
        self.assertEqual(s.initial, 'ng')
        self.assertEqual(s.rime, 'a')
        self.assertEqual(s.coda, '')
        self.assertEqual(s.tone, '242')
        s = YngPingSyllable.from_string('siu55')
        self.assertEqual(s.initial, 's')
        self.assertEqual(s.rime, 'iu')
        self.assertEqual(s.coda, '')
        self.assertEqual(s.tone, '55')


    def test_yngping_should_parse_closed_syllable(self):
        """測試基本的 YngPing 鍵入方案解析. 入聲. """
        s = YngPingSyllable.from_string('ak23')
        self.assertEqual(s.initial, '')
        self.assertEqual(s.rime, 'a')
        self.assertEqual(s.coda, 'k')
        self.assertEqual(s.tone, '23')

        s = YngPingSyllable.from_string('ah23')
        self.assertEqual(s.initial, '')
        self.assertEqual(s.rime, 'a')
        self.assertEqual(s.coda, 'h')
        self.assertEqual(s.tone, '23')

        s = YngPingSyllable.from_string('ah5')
        self.assertEqual(s.initial, '')
        self.assertEqual(s.rime, 'a')
        self.assertEqual(s.coda, 'h')
        self.assertEqual(s.tone, '5')

        s = YngPingSyllable.from_string('goeh5')
        self.assertEqual(s.initial, 'g')
        self.assertEqual(s.rime, 'oe')
        self.assertEqual(s.coda, 'h')
        self.assertEqual(s.tone, '5')

    def test_yngping_should_parse_ng_syllable(self):
        """測試基本的 YngPing 鍵入方案解析. ng 尾. """
        s = YngPingSyllable.from_string('ang242')
        self.assertEqual(s.initial, '')
        self.assertEqual(s.rime, 'a')
        self.assertEqual(s.coda, 'ng')
        self.assertEqual(s.tone, '242')

        s = YngPingSyllable.from_string('doeyng55')
        self.assertEqual(s.initial, 'd')
        self.assertEqual(s.rime, 'oey')
        self.assertEqual(s.coda, 'ng')
        self.assertEqual(s.tone, '55')

    def test_yngping_should_convert_to_handwritten(self):
        """測試鍵入方案轉書寫方案. """
        self.assertEqual(YngPingSyllable.from_string('ging53').to_handwritten(), normalise('gìng'))
        self.assertEqual(YngPingSyllable.from_string('dyng53').to_handwritten(), normalise('dǜng'))
        self.assertEqual(YngPingSyllable.from_string('goeyng242').to_handwritten(), normalise('gë̂üng'))
        self.assertEqual(YngPingSyllable.from_string('hei33').to_handwritten(), normalise('hēi'))
