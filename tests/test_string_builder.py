from lib.string_builder import *

def test_string_builder_outputs_string_length():
    string = StringBuilder()
    string.add("hello")
    result = string.size()
    assert result == 5

def test_adding_mulitple_strings_returns_concatenated_strings():
    string = StringBuilder()
    string.add("hello")
    string.add(' ')
    string.add('world')
    result = string.output()
    assert result == "hello world"

def test_return_length_of_concatenated_strings():
    string = StringBuilder()
    string.add("hello")
    string.add(' ')
    string.add('world')
    result = string.size()
    assert result == 11
