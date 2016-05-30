import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_add_6_and_7_is_12(self):
        self.assertEqual(extend.add(6, 7), 13)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(3, 7, 5), 7)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_median_five(self):
        self.assertEqual(extend.median([7,5,3,6]), 5.5)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_is_vovel_u_upper(self):
        self.assertTrue(extend.is_vovel('U'))

    def test_is_vovel_f(self):
        self.assertFalse(extend.is_vovel('f'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_kolbicie(self):
        self.assertEqual(extend.translate('kolbicie'), 'kovolbivicivieve')

    def test_translate_kolbiciie(self):
        self.assertEqual(extend.translate('kolbiciie'), 'kovolbiviciviivieve')

if __name__ == '__main__':
    unittest.main()
