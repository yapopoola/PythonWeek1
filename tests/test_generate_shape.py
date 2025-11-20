import pytest
from person import generate_square

# --- Basic correctness ---
def test_one_by_one():
    assert generate_square(1) == "+"

def test_two_by_two():
    assert generate_square(2) == "++\n++"

def test_three_by_three():
    assert generate_square(3) == "+++\n+++\n+++"

def test_four_by_four():
    assert generate_square(4) == "++++\n++++\n++++\n++++"

def test_five_by_five():
    assert generate_square(5) == "+++++\n+++++\n+++++\n+++++\n+++++"

# --- Structural checks ---
def test_row_count_matches_n():
    n = 7
    result = generate_square(n)
    assert len(result.split("\n")) == n

def test_each_row_length_matches_n():
    n = 6
    result = generate_square(n)
    assert all(len(row) == n for row in result.split("\n"))

def test_all_plus_characters():
    n = 8
    result = generate_square(n)
    assert all(set(row) == {"+"} for row in result.split("\n"))

def test_consistency_across_rows():
    n = 9
    result = generate_square(n)
    rows = result.split("\n")
    assert all(row == rows[0] for row in rows)

def test_no_leading_or_trailing_newlines():
    result = generate_square(3)
    assert not result.startswith("\n")
    assert not result.endswith("\n")

# --- Boundary tests ---
def test_upper_bound_50_rows():
    result = generate_square(50)
    assert len(result.split("\n")) == 50

def test_upper_bound_50_columns():
    result = generate_square(50)
    assert all(len(row) == 50 for row in result.split("\n"))

def test_large_square_characters():
    result = generate_square(50)
    assert all(set(row) == {"+"} for row in result.split("\n"))

# --- Parameterized tests ---
@pytest.mark.parametrize("n", [6, 10, 12, 15, 20])
def test_various_sizes(n):
    result = generate_square(n)
    rows = result.split("\n")
    assert len(rows) == n
    assert all(len(row) == n for row in rows)

@pytest.mark.parametrize("n", [25, 30, 40])
def test_mid_large_sizes(n):
    result = generate_square(n)
    rows = result.split("\n")
    assert len(rows) == n
    assert all(len(row) == n for row in rows)

# --- Robustness checks ---
def test_string_output_type():
    assert isinstance(generate_square(5), str)

def test_split_rows_are_strings():
    result = generate_square(5)
    assert all(isinstance(row, str) for row in result.split("\n"))

def test_no_spaces_in_output():
    result = generate_square(5)
    assert all(" " not in row for row in result.split("\n"))

def test_exact_character_count():
    n = 10
    result = generate_square(n)
    # total characters should be n*n plus (n-1) newlines
    assert len(result) == n * n + (n - 1)
