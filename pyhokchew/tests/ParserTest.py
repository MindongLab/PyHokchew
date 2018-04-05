import unittest
from ..parser import parse_foochow_romanized, parse_ciklin
from ..convert import foochow_romanized_to_ciklin, ciklin_to_foochow_romanized
import unicodedata

def normalised(s):
    return unicodedata.normalize('NFKC',s)

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_foochow_romanized(self):
        fr = parse_foochow_romanized('sĭng')
        self.assertEqual(fr.get_initial(),'s')
        self.assertEqual(fr.get_final_without_tone(),'ing')
        self.assertEqual(fr.get_tone(), 1)


    def test_ciklin(self):
        #self.assertEqual
        pass

    def test_interop(self):
        cases = ['góng','hióng', 'cê','gă', 'gì', 'dĭ','sék', 'báik', 'gōng','biêng']
        for c in cases:
            parsed = parse_foochow_romanized(c)
            #self.assertEqual(c, parsed.get_string())
            converted = ciklin_to_foochow_romanized(foochow_romanized_to_ciklin(parsed))
            self.assertEquals(normalised(c), converted.get_string())
    