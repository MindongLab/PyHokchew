import unittest
from ..utils import normalise, denormalise
from ..convert import wuyixing_to_yngping, minjiang_to_yngping, hector_to_foochow_romanized_string, \
        hector_to_yngping, foochow_romanized_to_yngping_string, hector_to_foochow_romanized
from ..models.historical.FoochowRomanized import FoochowRomanizedSyllable

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
            ("uh4", "óh")
        ]

        for hector, fr in TESTS:
            with self.subTest(msg=" %s => %s" % (hector, fr)):
                self.assertEqual(fr, hector_to_foochow_romanized_string(hector))

    def test_historical_to_yngping(self):
        """測試歷史音系轉換
        """

        TESTS = [
            ("ung55", "ung1", "ung"),
            ("ung53", "ung5", "ùng"),
            ("ung33", "ung2", "ūng"),
            ("oung212", "ung3", "óng"),
            ("oung242", "ung7", "ông"),
            ("ouk23", "uk4", "ók"),
            ("uk5", "uk8", "uk"),
            ("ua55", "ua1", "ua"),
            ("ua53", "ua5", "uà"),
            ("ua33", "ua2", "uā"),
            ("ua212", "ua3", "uá"),
            ("ua242", "ua7", "uâ"),
            ("uah23", "uah4", "uáh"),
            ("uah5", "uah8", "uah"),
            ("yong55", "iong1", "iong"),
            ("yong53", "iong5", "iòng"),
            ("yong33", "iong2", "iōng"),
            ("yong212", "iong3", "ióng"),
            ("yong242", "iong7", "iông"),
            ("yok23", "iok4", "iók"),
            ("yok5", "iok8", "iok"),
            ("buong55", "biong1", "biong"),
            ("buong53", "biong5", "biòng"),
            ("buong33", "biong2", "biōng"),
            ("buong212", "biong3", "bióng"),
            ("buong242", "biong7", "biông"),
            ("buok23", "biok4", "biók"),
            ("buok5", "biok8", "biok"),
            ("iu55", "iu1", "iu"),
            ("iu53", "iu5", "iù"),
            ("iu33", "iu2", "iū"),
            ("iu212", "iu3", "éu"),
            ("iu242", "iu7", "êu"),
            #("iuh23", "iuh4", "éuh"),
            #("iuh5", "iuh8", "iuh"),
            ("ang55", "ang1", "ang"),
            ("ang53", "ang5", "àng"),
            ("ang33", "ang2", "āng"),
            ("ang212", "ang3", "áng"),
            ("ang242", "ang7", "âng"),
            ("ak23", "ak4", "ák"),
            ("ak5", "ak8", "ak"),
            ("ai55", "ai1", "ai"),
            ("ai53", "ai5", "ài"),
            ("ai33", "ai2", "āi"),
            ("ai212", "ai3", "ái"),
            ("ai242", "ai7", "âi"),
            #("aih23", "aih4", "áih"),
            #("aih5", "aih8", "aih"),
            ("a55", "a1", "a"),
            ("a53", "a5", "à"),
            ("a33", "a2", "ā"),
            ("a212", "a3", "á"),
            ("a242", "a7", "â"),
            ("ah23", "ah4", "áh"),
            ("ah5", "ah8", "ah"),
            ("ing55", "ing1", "ing"),
            ("ing53", "ing5", "ìng"),
            ("ing33", "ing2", "īng"),
            ("eing212", "ing3", "éng"),
            ("eing242", "ing7", "êng"),
            ("eik23", "ik4", "ék"),
            ("ik5", "ik8", "ik"),
            ("uang55", "uang1", "uang"),
            ("uang53", "uang5", "uàng"),
            ("uang33", "uang2", "uāng"),
            ("uang212", "uang3", "uáng"),
            ("uang242", "uang7", "uâng"),
            ("uak23", "uak4", "uák"),
            ("uak5", "uak8", "uak"),
            ("o55", "o1", "o̤"),
            ("o53", "o5", "ò̤"),
            ("o33", "o2", "ō̤"),
            ("o212", "o3", "ó̤"),
            ("o242", "o7", "ô̤"),
            ("oh23", "oh4", "ó̤h"),
            ("oh5", "oh8", "o̤h"),
            ("y55", "y1", "ṳ"),
            ("y53", "y5", "ṳ̀"),
            ("y33", "y2", "ṳ̄"),
            ("oey212", "y3", "é̤ṳ"),
            ("oey242", "y7", "ê̤ṳ"),
            ("oeyk23", "yk4", "é̤ṳk"),
            ("yk5", "yk8", "ṳk"),
            ("ui55", "uoi1", "uoi"),
            ("ui53", "uoi5", "uòi"),
            ("ui33", "uoi2", "uōi"),
            ("ui212", "uoi3", "uói"),
            ("ui242", "uoi7", "uôi"),
            #("uih23", "uoih4", "uóih"),
            #("uih5", "uoih8", "uoih"),
            ("u55", "u1", "u"),
            ("u53", "u5", "ù"),
            ("u33", "u2", "ū"),
            ("ou212", "u3", "ó"),
            ("ou242", "u7", "ô"),
            ("ouh23", "uh4", "óh"),
            ("uh5", "uh8", "uh"),
            ("eing55", "eng1", "eng"),
            ("eing53", "eng5", "èng"),
            ("eing33", "eng2", "ēng"),
            ("aing212", "eng3", "áing"),
            ("aing242", "eng7", "âing"),
            ("aik23", "ek4", "áik"),
            ("eik5", "ek8", "ek"),
            ("uong55", "uong1", "uong"),
            ("uong53", "uong5", "uòng"),
            ("uong33", "uong2", "uōng"),
            ("uong212", "uong3", "uóng"),
            ("uong242", "uong7", "uông"),
            ("uok23", "uok4", "uók"),
            ("uok5", "uok8", "uok"),
            ("ui55", "ui1", "ui"),
            ("ui53", "ui5", "ùi"),
            ("ui33", "ui2", "ūi"),
            ("ui212", "ui3", "ói"),
            ("ui242", "ui7", "ôi"),
            #("uih23", "uih4", "óih"),
            #("uih5", "uih8", "uih"),
            ("iu55", "ieu1", "ieu"),
            ("iu53", "ieu5", "ièu"),
            ("iu33", "ieu2", "iēu"),
            ("iu212", "ieu3", "iéu"),
            ("iu242", "ieu7", "iêu"),
            #("iuh23", "ieuh4", "iéuh"),
            #("iuh5", "ieuh8", "ieuh"),
            ("yng55", "yng1", "ṳng"),
            ("yng53", "yng5", "ṳ̀ng"),
            ("yng33", "yng2", "ṳ̄ng"),
            ("oeyng212", "yng3", "é̤ṳng"),
            ("oeyng242", "yng7", "ê̤ṳng"),
            ("oeyk23", "yk4", "é̤ṳk"),
            ("yk5", "yk8", "ṳk"),
            ("oung55", "ong1", "ong"),
            ("oung53", "ong5", "òng"),
            ("oung33", "ong2", "ōng"),
            ("aung212", "ong3", "áung"),
            ("aung242", "ong7", "âung"),
            ("auk23", "ok4", "áuk"),
            ("ouk5", "ok8", "ok"),
            ("i55", "i1", "i"),
            ("i53", "i5", "ì"),
            ("i33", "i2", "ī"),
            ("ei212", "i3", "é"),
            ("ei242", "i7", "ê"),
            ("eih23", "ih4", "éh"),
            ("ih5", "ih8", "ih"),
            ("oeyng55", "oeng1", "e̤ng"),
            ("oeyng53", "oeng5", "è̤ng"),
            ("oeyng33", "oeng2", "ē̤ng"),
            ("oyng212", "oeng3", "áe̤ng"),
            ("oyng242", "oeng7", "âe̤ng"),
            ("oyk23", "oek4", "áe̤k"),
            ("oeyk5", "oek8", "e̤k"),
            ("au55", "au1", "au"),
            ("au53", "au5", "àu"),
            ("au33", "au2", "āu"),
            ("au212", "au3", "áu"),
            ("au242", "au7", "âu"),
            ("auh23", "auh4", "áuh"),
            #("auh5", "auh8", "auh"),
            ("uo55", "uo1", "uo"),
            ("uo53", "uo5", "uò"),
            ("uo33", "uo2", "uō"),
            ("uo212", "uo3", "uó"),
            ("uo242", "uo7", "uô"),
            ("uoh23", "uoh4", "uóh"),
            ("uoh5", "uoh8", "uoh"),
            ("e55", "e1", "a̤"),
            ("e53", "e5", "à̤"),
            ("e33", "e2", "ā̤"),
            ("a212", "e3", "á̤"),
            ("a242", "e7", "â̤"),
            ("ah23", "eh4", "á̤h"),
            #("eh5", "eh8", "a̤h"),
            ("yo55", "io1", "io"),
            ("yo53", "io5", "iò"),
            ("yo33", "io2", "iō"),
            ("yo212", "io3", "ió"),
            ("yo242", "io7", "iô"),
            ("yoh23", "ioh4", "ióh"),
            ("yoh5", "ioh8", "ioh"),
            ("cuo55", "cio1", "chio"),
            ("cuo53", "cio5", "chiò"),
            ("cuo33", "cio2", "chiō"),
            ("cuo212", "cio3", "chió"),
            ("cuo242", "cio7", "chiô"),
            ("cuoh23", "cioh4", "chióh"),
            #("cuoh5", "cioh8", "chioh"),
            ("ie55", "ie1", "ie"),
            ("ie53", "ie5", "iè"),
            ("ie33", "ie2", "iē"),
            ("ie212", "ie3", "ié"),
            ("ie242", "ie7", "iê"),
            ("ieh23", "ieh4", "iéh"),
            #("ieh5", "ieh8", "ieh"),
            ("iang55", "iang1", "iang"),
            ("iang53", "iang5", "iàng"),
            ("iang33", "iang2", "iāng"),
            ("iang212", "iang3", "iáng"),
            ("iang242", "iang7", "iâng"),
            ("iak23", "iak4", "iák"),
            #("iak5", "iak8", "iak"),
            ("oey55", "oi1", "oi"),
            ("oey53", "oi5", "òi"),
            ("oey33", "oi2", "ōi"),
            ("oy212", "oi3", "ó̤i"),
            ("oy242", "oi7", "ô̤i"),
            ("oyh23", "oih4", "ó̤ih"),
            #("oeyh5", "oih8", "oih"),
            ("oe55", "oe1", "e̤"),
            ("oe53", "oe5", "è̤"),
            ("oe33", "oe2", "ē̤"),
            ("o212", "oe3", "áe̤"),
            ("o242", "oe7", "âe̤"),
            #("oeh23", "oe4", "e̤h"),
            #("oeh5", "oe8", "e̤h"),
            ("ieng55", "ieng1", "ieng"),
            ("ieng53", "ieng5", "ièng"),
            ("ieng33", "ieng2", "iēng"),
            ("ieng212", "ieng3", "iéng"),
            ("ieng242", "ieng7", "iêng"),
            ("iek23", "iek4", "iék"),
            #("iek5", "iek8", "iek"),
            ("ia55", "ia1", "ia"),
            ("ia53", "ia5", "ià"),
            ("ia33", "ia2", "iā"),
            ("ia212", "ia3", "iá"),
            ("ia242", "ia7", "iâ"),
            ("ieh23", "iah4", "iáh"),
            #("ieh5", "iah8", "iah"),
            ("uai55", "uai1", "uai"),
            ("uai53", "uai5", "uài"),
            ("uai33", "uai2", "uāi"),
            ("uai212", "uai3", "uái"),
            ("uai242", "uai7", "uâi"),
            #("uaih23", "uaih4", "uáih"),
            #("uaih5", "uaih8", "uaih"),
            ("eu55", "eu1", "eu"),
            ("eu53", "eu5", "èu"),
            ("eu33", "eu2", "ēu"),
            ("au212", "eu3", "áiu"),
            ("au242", "eu7", "âiu"),
            ("auh23", "eu4", "áiuh"),
            #("euh5", "eu8", "euh"),
        ]

        for yp, hector, fr in TESTS:
                with self.subTest(msg="測試歷史音系轉換 YP=%s HECTOR=%s FR=%s" % (yp, hector, fr)):
                    self.assertEqual(yp, hector_to_yngping(hector))
                    self.assertEqual(yp, foochow_romanized_to_yngping_string(fr, True))

                    # 擬音轉羅馬字
                    f1 = hector_to_foochow_romanized(hector)
                    f2 = FoochowRomanizedSyllable.from_string(fr, True)
                    self.assertEqual(f1.initial, f2.initial)
                    self.assertEqual(f1.final, f2.final)
                    self.assertEqual(f1.tone, f2.tone)
