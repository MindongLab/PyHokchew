import unittest
from ...models.concurrent.matsu import WuyixingSyllable
from ...utils import normalise

class WuyixingParseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_parsing(self):
        """解析烏衣行音節
        """
        for s, expected in self.PARSE_TEST_CASES:
            with self.subTest(msg="解析烏衣行音節 s" , s=s):
                syllable = WuyixingSyllable.from_string(s)
                expectedInitial, expectedFinal, expectedTone = expected
                self.assertEqual(syllable.initial, expectedInitial)
                self.assertEqual(syllable.final, expectedFinal)
                self.assertEqual(syllable.tone, expectedTone)

    PARSE_TEST_CASES = [
        ('houv',('h','ou','212')),
        ('houx',('h','ou','242')),
        ('huangs',('h','uang','53')),
        ('huong',('h','uong','55')),
        ('hus',('h','u','53')),
        ('paukz',('p','auk','23')),
        ('phiakz',('ph','iak','23')),
        ('phouh',('ph','ouh','5')),
        ('pok',('p','ok','5')),
        ('pongf',('p','ong','33')),
        ('poungv',('p','oung','212')),
        ('poungx',('p','oung','242')),
        ('thiekz',('th','iek','23')),
        ('tsaikz',('ts','aik','23')),
        ('tshaikz',('tsh','aik','23')),
        ('oe',('','oe','55')),
    ]

    
