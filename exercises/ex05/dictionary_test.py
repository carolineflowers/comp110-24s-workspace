"""EX05: Dictionary Unit Tests Exercise."""

__author__ = "730431261"

import pytest
from exercises.ex05.dictionary import invert 
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_use_case_1() -> None:
    """Tests Invevrt Function with One Value Dict."""
    input: dict[str, str] = {"C": "Caroline"}
    expected_result: dict[str, str] = {"Caroline": "C"}
    assert invert(input) == expected_result


def test_invert_use_case_2() -> None:
    """Tests Invert Function with Two Value Dict."""
    input2 = {"C": "Caroline", "E": "Elila"}
    expected_result2 = {"Caroline": "C", "Elila": "E"}
    assert invert(input2) == expected_result2


def test_invert_edge_case_2() -> None:
    """Tests Invert Function with Empty Dict."""
    input2 = {}
    expected_result2 = {}
    assert invert(input2) == expected_result2


def test_invert_key_error() -> None:
    """Tests Invert Function Raising Key Error for Repeats."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_favorite_color_use_case_1() -> None:
    """Tests favorite_color function with same frq."""
    input = {"Caroline": "green", "Anna": "green", "Elila": "red", "Sophie": "red"}
    expected_result = {"green"}
    assert favorite_color(input) == expected_result


def test_favorite_color_use_case_2() -> None:
    """Tests favorite_color function with repeated color."""
    input2 = {"Caroline": "red", "Anna": "blue", "Elila": "red", "Sophie": "green"}
    expected_result2 = {"red"}
    assert favorite_color(input2) == expected_result2


def test_favorite_color_edge_case() -> None:
    """Tests favorite_color function with empty dict."""
    input = {}
    expected_result = {}
    assert favorite_color(input) == expected_result


def test_count_use_case_1() -> None:
    """Tests count function with 1 appearance."""
    input = ("Caroline", "Nikhi")
    expected_result: dict[str, int] = {"Caroline": 1, "Nikhi": 1}
    assert count(input) == expected_result


def test_count_use_case_2() -> None:
    """Tests count function with 2 appearances."""
    input2 = ("Caroline", "Nikhi", "Aud", "Aud")
    expected_result2: dict[str, int] = {"Caroline": 1, "Nikhi": 1, "Aud": 2}
    assert count(input2) == expected_result2


def test_count_edge_case() -> None:
    """Tests count function with one word dict."""
    input2 = ["Caroline"]
    expected_result2: dict[str, int] = {"Caroline": 1}
    assert count(input2) == expected_result2


def test_alphabetizer_use_case_1() -> None:
    """Tests alphabetizer function with one letter."""
    input = ["Laur", "Liv"]
    expected_result = {"l": ["Laur", "Liv"]}
    assert alphabetizer(input) == expected_result


def test_alphabetizer_use_case_2() -> None:
    """Tests alphabetizer function with two letters."""
    input2 = ["Laur", "Liv", "Caleb", "Caro"]
    expected_result2: dict[str, list[str]] = {"l": ["Laur", "Liv"], "c": ["Caleb", "Caro"]}
    assert alphabetizer(input2) == expected_result2


def test_alphabetizer_edge_case() -> None:
    """Tests alphabetizer function with empty dict."""
    input = {}
    expected_result = {}
    assert alphabetizer(input) == expected_result


def test_update_attendance_use_case_1() -> None:
    """Tests update_attendance function with empty dict."""
    input = {}
    day = "Tues"
    student = "Caro"
    update_attendance(input, day, student)
    assert student in input[day]


def test_update_attendance_use_case_2() -> None:
    """Tests update_attendance function with two days."""
    input2 = {"Tues": ["Caro"], "Wed": ["Megs"]}
    day2 = "Tues"
    student2 = "Allison"
    update_attendance(input2, day2, student2)
    assert student2 in input2[day2]


def test_update_attendance_edge_case() -> None:
    """Test update_attendance function with missing day."""
    input = {"Tues": ["Caro", "Allison"], "Wed": ["Megs"]}
    day = "Sun"
    student = "Lisa"
    update_attendance(input, day, student)
    assert student in input[day]