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
    #caracter invalido
    def test_roman_to_int_test_invalid_char(self):
        self.assertEqual(roman_to_int("XIB"), -1)
    #caracters validos
    def test_roman_to_int_test_invalid_char_40(self):
        self.assertEqual(roman_to_int("XL"), 40)

    #mais de 3 caracteres iguais e consecutivos
    def test_roman_to_int_test_char_count_regex(self):
        self.assertEqual(roman_to_int("XXXX"), -1)
    #um unico caracter
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

    #2 caracteres e 1 subtracao
    def test_roman_to_int_test_size2_4(self):
        self.assertEqual(roman_to_int("IV"), 4)
    def test_roman_to_int_test_size2_2(self):
        self.assertEqual(roman_to_int("II"), 2)

    #3 caracteres e 1 subtracao
    def test_roman_to_int_test_size3_19(self):
        self.assertEqual(roman_to_int("XIX"), 19)
    def test_roman_to_int_test_size3_30(self):
        self.assertEqual(roman_to_int("XXX"), 30)

    #4 caracteres com 1 subtração
    def test_roman_to_int_test_size4_24(self):
        self.assertEqual(roman_to_int("XXIV"), 24)
    def test_roman_to_int_test_size4_26(self):
        self.assertEqual(roman_to_int("XXVI"), 26)

    #4 caracteres com 2 subtraçoes
    def test_roman_to_int_test_size4_490(self):
        self.assertEqual(roman_to_int("CDXC"), 490)
    def test_roman_to_int_test_size4_29(self):
        self.assertEqual(roman_to_int("XXIX"), 29)
