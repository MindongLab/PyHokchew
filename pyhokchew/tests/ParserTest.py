import unittest
from ..models.FoochowRomanized import FoochowRomanizedSyllable
from ..parser import parse_ciklin
from ..utils import normalise, denormalise
from ..convert import foochow_romanized_to_ciklin, ciklin_to_foochow_romanized


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_foochow_romanized(self):
        """測試基本的 Foochow Romanized 解析."""
        fr = FoochowRomanizedSyllable.from_string('sĭng')
        self.assertEqual(fr.get_initial(),'s')
        self.assertEqual(fr.get_final_without_tone(),'ing')
        self.assertEqual(fr.get_tone(), 1)

    def test_foochow_romanized_capital(self):
        """Ensures that we can parse Foochow Romanized syllables with capital letters."""
        fr = FoochowRomanizedSyllable.from_string('Sĭng')
        self.assertEqual(fr.get_initial(),'s')
        self.assertEqual(fr.get_final_without_tone(),'ing')
        self.assertEqual(fr.get_tone(), 1)

        fr = FoochowRomanizedSyllable.from_string('À̤')
        self.assertEqual(fr.get_initial(),'')
        self.assertEqual(fr.get_final_without_tone(),'a̤')
        self.assertEqual(fr.get_tone(), 5)

    def test_interop(self):
        """Ensures round-trip compatibility between FoochowRomanizedSyllable and CikLinSyllable."""
        cases = ['góng', 'hióng', 'cê', 'gă', 'gì', 'dĭ', 'sék', 'báik', 'gōng', 'biêng']
        for c in cases:
            parsed = FoochowRomanizedSyllable.from_string(c)
            converted = ciklin_to_foochow_romanized(foochow_romanized_to_ciklin(parsed))
            self.assertEqual(normalise(c), converted.get_string())
    
    def test_foochow_romanized_ingbing_omitting(self):
        """確保 FoochowRomanizedSyllable 可以解析省略陰平調號的音節."""
        errored = False
        try:
            fr = FoochowRomanizedSyllable.from_string('sing')
        except:
            errored = True
        self.assertTrue(errored)

        fr = FoochowRomanizedSyllable.from_string('sing', allow_omit_ingbing = True)
        self.assertEqual(fr.get_initial(),'s')
        self.assertEqual(fr.get_final_without_tone(),'ing')
        self.assertEqual(fr.get_tone(), 1)

    def test_ciklin(self):
        # self.assertEqual
        pass
