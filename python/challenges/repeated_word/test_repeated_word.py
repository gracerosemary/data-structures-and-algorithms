import pytest
from repeated_word import repeated_word, cleaner, counter, add_to_hashtable
from hashtable import Hashtable

def test_cleaner_one_special_char():
    string = "grace is, awesome"
    actual = cleaner(string)
    expected = ['grace', 'is', 'awesome']
    assert actual == expected

def test_cleaner_mult_special_char():
    string = "grace. is, awesome."
    actual = cleaner(string)
    expected = ['grace', 'is', 'awesome']
    assert actual == expected

def test_cleaner_alpha():
    string = "GRACE IS AWESOME"
    actual = cleaner(string)
    expected = ['grace', 'is', 'awesome']
    assert actual == expected

def test_counter_one():
    one_list = ['grace', 'is', 'awesome']
    actual = counter(one_list)
    expected = {'awesome': 1, 'grace': 1, 'is': 1}
    assert actual == expected

def test_counter_two():
    one_list = ['grace', 'is', 'is', 'awesome', 'awesome', 'awesome']
    actual = counter(one_list)
    expected = {'awesome': 3, 'grace': 1, 'is': 2}
    assert actual == expected

def test_counter_three():
    one_list = ['grace', 'is', 'awesome', 'awesome', 'awesome']
    actual = counter(one_list)
    expected = {'awesome': 3, 'grace': 1, 'is': 1}
    assert actual == expected

def test_repeated_word_short():
    string = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(string)
    expected = "a"
    assert actual == expected

def test_repeated_word_long():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(string)
    expected = "it"
    assert actual == expected

def test_repeated_word_med():
    string = "The long night lasted through the summer, fall, winter, and back to spring"
    actual = repeated_word(string)
    expected = "the"
    assert actual == expected