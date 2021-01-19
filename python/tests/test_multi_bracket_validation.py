import pytest
from challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_single_bracket():
    mult = multi_bracket_validation(")")
    actual = mult
    expected = False
    assert actual == expected

def test_two_opening_brackets():
    mult = multi_bracket_validation("({")
    actual = mult
    expected = False
    assert actual == expected

def test_three_balanced_pairs():
    mult = multi_bracket_validation("{}(){}")
    actual = mult
    expected = True
    assert actual == expected

def test_balanced_with_extra_char():
    mult = multi_bracket_validation("[[Extra Characters]]")
    actual = mult
    expected = True
    assert actual == expected

def test_balanced_with_extra_char_diff():
    mult = multi_bracket_validation("()[[Extra Characters]]")
    actual = mult
    expected = True
    assert actual == expected

def test_unbalanced():
    mult = multi_bracket_validation("[({}]")
    actual = mult
    expected = False
    assert actual == expected

def test_unbalanced_with_char():
    mult = multi_bracket_validation("[2)({d43}s]")
    actual = mult
    expected = False
    assert actual == expected
