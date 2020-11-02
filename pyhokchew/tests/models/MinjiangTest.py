import unittest
from ...models.concurrent.minjiang import MinjiangSyllable
from ...utils import normalise

class MinjiangParseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_parsing(self):
        """解析閩江學院的音節
        """
        for s, expected in self.PARSE_TEST_CASES:
            with self.subTest(msg="解析閩江學院的音節 %s" % s):
                syllable = MinjiangSyllable.from_string(s)
                expectedInitial, expectedFinal, expectedTone = expected
                self.assertEqual(syllable.initial, expectedInitial)
                self.assertEqual(syllable.final, expectedFinal)
                self.assertEqual(syllable.tone, expectedTone)

    PARSE_TEST_CASES = [
        ('huɑnɡ1',('h','uang','55')),
        ('goüng5',('g','oüng','242')),
        ('gëü5',('g','ëü','242')),
        ('huak7',('h','uak','5')),
        ('kê1',('k','e','55')),
        ('ieng4',('','ieng','212'))
    ]

    
