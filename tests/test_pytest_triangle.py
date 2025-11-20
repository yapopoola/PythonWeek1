from person import Triangle
import pytest


def test_that_equlateral_traingle_has_expected_area(): 
    equilateral_trangle = Triangle(6, 6, 6, 6)
    area_of_triangle = equilateral_trangle.area()
    assert area_of_triangle == 18


def test_that_unequlateral_traingle_has_expected_area(): 
    equilateral_trangle = Triangle(4, 6, 6, 6)
    area_of_triangle = equilateral_trangle.area()
    assert area_of_triangle == 12


def tests_that_when_base_is_string_then_error_is_raised():
    with pytest.raises(TypeError):
        new_triangle = Triangle(base="five", height=6, side1=6, side2=6)
        new_triangle.area()
  
