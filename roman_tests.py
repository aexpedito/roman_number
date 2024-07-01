import unittest
from roman_number import roman_to_int, acceptable_chars

#1. caracter invalido
#2. cada um dos valores
#3. Regex: ([I]{4,}|[V]{4,}|[X]{4,}|[L]{4,}|[C]{4,}|[D]{4,}|[M]{4,})

class RomanTestCases(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_roman_to_int_test_invalid_char(self):
        self.assertEqual(roman_to_int("XIB"), -1)

    def test_roman_to_int_test_I(self):
        self.assertEqual(roman_to_int("I"), 1)
    def test_roman_to_int_test_V(self):
        self.assertEqual(roman_to_int("V"), 5)
    def test_roman_to_int_test_X(self):
        self.assertEqual(roman_to_int("X"), 10)
    def test_roman_to_int_test_L(self):
        self.assertEqual(roman_to_int("L"), 50)
    def test_roman_to_int_test_C(self):
        self.assertEqual(roman_to_int("C"), 100)
    def test_roman_to_int_test_D(self):
        self.assertEqual(roman_to_int("D"), 500)
    def test_roman_to_int_test_M(self):
        self.assertEqual(roman_to_int("M"), 1000)

    def test_roman_to_int_test_char_count_regex(self):
        self.assertEqual(roman_to_int("XXXX"), -1)

    def test_roman_to_int_test_size1_1(self):
        self.assertEqual(roman_to_int("I"), 1)

    def test_roman_to_int_test_size1_10(self):
        self.assertEqual(roman_to_int("X"), 10)

    def test_roman_to_int_test_size2_4(self):
        self.assertEqual(roman_to_int("IV"), 4)

    def test_roman_to_int_test_size2_2(self):
        self.assertEqual(roman_to_int("II"), 2)

    def test_roman_to_int_test_size3_3(self):
        self.assertEqual(roman_to_int("III"), 3)

    def test_roman_to_int_test_size2_2(self):
        self.assertEqual(roman_to_int("II"), 2)

    def test_roman_to_int_test_size5_18(self):
        self.assertEqual(roman_to_int("XVIII"), 18)

    def test_roman_to_int_test_size5_19(self):
        self.assertEqual(roman_to_int("XIX"), 19)

    def test_roman_to_int_test_size9_88(self):
        self.assertEqual(roman_to_int("LXXXVIII"), 88)