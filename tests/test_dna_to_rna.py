from unittest import TestCase
from person import dna_to_rna


class TestRnaToDna(TestCase):
    def test_check_if_input_is_a_string(self):
        self.assertRaises(AttributeError, dna_to_rna, 123450)

    def test_check_if_input_is_a_string_not_float(self):
        self.assertRaises(AttributeError, dna_to_rna, 12345.55)

    def test_check_if_input_is_a_string_not_int(self):
        self.assertRaises(AttributeError, dna_to_rna, 12345)
    
    def test_check_if_input_is_a_string_not_bool(self):
        self.assertRaises(AttributeError, dna_to_rna, False)

    def test_replace_all_t_with_u1(self):
        word = "TAT"
        self.assertEqual(dna_to_rna(word), "UAU")

    def test_replace_all_t_with_u2(self):
        word = "BAT"
        self.assertEqual(dna_to_rna(word), "BAU")

    def test_replace_all_t_with_u3(self):
        word = "TATOO"
        self.assertEqual(dna_to_rna(word), "UAUOO")

    def test_replace_all_t_with_u4(self):
        word = "TEST"
        self.assertEqual(dna_to_rna(word), "UESU")

    def test_replace_all_t_with_u5(self):
        word = "TATA"
        self.assertEqual(dna_to_rna(word), "UAUA")

    def test_only_take_capital_letter6(self):
        word = "capital letter"
        self.assertEqual(dna_to_rna(word), "capital letter")


    