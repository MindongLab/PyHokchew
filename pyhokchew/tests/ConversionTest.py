import unittest
from ..utils import normalise, denormalise
from ..convert import wuyixing_to_yngping, minjiang_to_yngping, hector_to_foochow_romanized

class ConversionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_wuyixing_to_yngping(self):
        """測試烏衣行轉榕拼
        """

        TESTS = [
            ("kieuf", "giu33"),
            ("khov", "ko212"),
            ("eingx", "eing242"),
            ('khoeyng','koeyng55'),
            ('ngiuf','ngiu33')
        ]

        for wyx, yngping in TESTS:
            with self.subTest(msg="測試烏衣行轉榕拼 %s => %s" % (wyx, yngping)):
                self.assertEqual(yngping, wuyixing_to_yngping(wyx))

    def test_minjiang_to_yngping(self):
        """測試閩江學院轉榕拼
        """

        TESTS = [
            ('lëünɡ2','loeyng53'),
            ('ɑnɡ4','ang212'),
            ('hünɡ1','hyng55'),
            ('ɑi1', 'ai55')
        ]

        for mj, yngping in TESTS:
            with self.subTest(msg="測試閩江學院轉榕拼 %s => %s" % (mj, yngping)):
                self.assertEqual(yngping, minjiang_to_yngping(mj))

    def test_hector_to_foochow_romanized(self):
        """測試 only3km 擬音 code 轉羅馬字
        """

        TESTS = [
            ('iok4','iók'),
        ]

        for hector, fr in TESTS:
            with self.subTest(msg=" %s => %s" % (hector, fr)):
                self.assertEqual(fr, hector_to_foochow_romanized(hector))