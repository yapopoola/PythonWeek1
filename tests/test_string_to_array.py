from unittest import TestCase
from person import string_to_array


class TestStringToArray(TestCase):
    def test_that_input_only_takes_a_string_not_num(self):
        self.assertRaises(AttributeError, string_to_array, 12345)

    def test_that_input_only_takes_a_string_not_float(self):
        self.assertRaises(AttributeError, string_to_array, 12345.12345)

    def test_that_input_only_takes_a_string_not_bool(self):
        self.assertRaises(AttributeError, string_to_array, True)

    def test_that_input_is_converted_to_split(self):
        word = "Robin Singh"
        self.assertEqual(string_to_array(word), ["Robin", "Singh"])

    def test_that_input_is_converted_to_splito(self):
        word = "Robin Singo"
        self.assertEqual(string_to_array(word), ["Robin", "Singo"])
    
    def test_that_input_is_converted_to_spliti(self):
        word = "Robin Sini"
        self.assertEqual(string_to_array(word), ["Robin", "Sini"])
        
    def test_that_input_is_converted_to_splitu(self):
        word = "Robin Siu"
        self.assertEqual(string_to_array(word), ["Robin", "Siu"])
        
    def test_that_input_is_converted_to_splity(self):
        word = "Robin Sy"
        self.assertEqual(string_to_array(word), ["Robin", "Sy"])
    
    def test_that_input_is_converted_to_splitr(self):
        word = "Robinr "
        self.assertEqual(string_to_array(word), ["Robinr"])
        
    def test_that_input_is_converted_to_splitt(self):
        word = "Robinn"
        self.assertEqual(string_to_array(word), ["Robinn"])
        
    def test_that_input_is_converted_to_splite(self):
        word = "Robie"
        self.assertEqual(string_to_array(word), ["Robie"])

    def test_that_when_a_string_is_given_then_a_list_is_returned(self):
        self.assertEqual(string_to_array("Robin Singhq"), ["Robin", "Singhq"])

    def test_that_when_an_empty_string_is_given_then_a_empty_list_is_returned(self):
        self.assertEqual(string_to_array(""), [""])

    def test_that_the_output_is_an_array(self):
        return_value = string_to_array("Robin Singhw")
        self.assertEqual(return_value, ["Robin", "Singhw"])