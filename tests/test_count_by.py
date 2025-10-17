from unittest import TestCase
from person import count_by


class TestCountBy(TestCase):
    def test_that_inputs_are_integers_only(self):
        self.assertRaises(TypeError, count_by, "Rafi", "Bella")

    def test_that_when_x_is_2_and_n_is_5_then_result_has_5_items(self): 
        value_from_function = count_by(x=2, n=5)
        expected_outcome = [2,4,6,8,10]
        self.assertEquals(value_from_function, expected_outcome)
        self.assertEqual(len(value_from_function), 5)

    def test_that_when_x_is_1_and_n_is_10_then_result_has_10_items(self): 
        self.assertEqual(len(count_by(x=1, n=10)), 10)
        self.assertEquals(count_by(x=1, n=10), [1,2,3,4,5,6,7,8,9,10])

    def test_that_the_output_is_an_array(self):
        return_value = count_by(x=2, n=5)
        self.assertEquals(type(return_value),  list)
        self.assertIsInstance(return_value, list)

