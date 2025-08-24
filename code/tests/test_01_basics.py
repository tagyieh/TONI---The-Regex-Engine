import pytest

from bin.compiler import toniParserVisitor
from bin.evaluator import evaluator
from bin.converter import converter

from lib import toni_classes

compiler = toniParserVisitor.toniParserVisitor()

def base_test(test_string: str, nfa: toni_classes.Partial_NFA, dfa: toni_classes.DFA_State, *, expected_result: bool) -> bool:

    assert evaluator.traverse_NFA(nfa, test_string) == expected_result
    assert evaluator.traverse_DFA(dfa, test_string) == expected_result
    
def prepare_test(regex: str):

    nfa = compiler.compile(regex)
    dfa = converter.convert_nfa_to_dfa(nfa)

    return nfa, dfa

#
#
# TESTS FOR SINGLE CHARACTERS (and if ^ and $ works)
#
#

def test_single_char_success_1():

    regex = "^a$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_single_char_fail_1():

    regex = "^a$"
    nfa, dfa = prepare_test(regex)
    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

# def test_single_char_success_2():

#     regex = "a$"
#     nfa, dfa = prepare_test(regex)
#     test_string = "this_is_not_problem_a"

#     base_test(test_string, nfa, dfa, expected_result=True)

def test_single_char_fail_2():

    regex = "a$"
    nfa, dfa = prepare_test(regex)
    test_string = "this_is_problem_ab"

    base_test(test_string, nfa, dfa, expected_result=False)

# def test_single_char_success_3():

#     regex = "^a"
#     nfa, dfa = prepare_test(regex)
#     test_string = "a_this_is_not_problem"

#     base_test(test_string, nfa, dfa, expected_result=True)

def test_single_char_fail_3():

    regex = "^a"
    nfa, dfa = prepare_test(regex)
    test_string = "b_this_is_a_problem"

    base_test(test_string, nfa, dfa, expected_result=False)

# def test_single_char_success_4():

#     regex = "a"
#     nfa, dfa = prepare_test(regex)
#     test_string = "this_is_not_problem_a_also_not_a_problemf"

#     base_test(test_string, nfa, dfa, expected_result=True)

def test_single_char_fail_4():

    regex = "a"
    nfa, dfa = prepare_test(regex)
    test_string = "this_is_problem_b_big_problem"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR STRINGS
#
#

def test_string_success_1():
    
    regex = "^ab$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_string_fail_1():

    regex = "^ab$"
    nfa, dfa = prepare_test(regex)
    test_string = "ba"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_string_success_2():

    regex = "^this_is_a_test$"
    nfa, dfa = prepare_test(regex)
    test_string = "this_is_a_test"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_string_fail_2():
    
    regex = "^this_is_a_test$"
    nfa, dfa = prepare_test(regex)
    test_string = "this_is_not_a_test"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_string_fail_3():

    regex = "^this_is_a_test$"
    nfa, dfa = prepare_test(regex)
    test_string = "this_is_a_tes"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR PIPE |
#
#

def test_pipe_success_1():

    regex = "^a|b$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_pipe_fail_1():
    
    regex = "^a|b$"
    nfa, dfa = prepare_test(regex)
    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_pipe_success_2():
    
    regex = "^a|b|c|d$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "d"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_pipe_fail_2():
    
    regex = "^a|b|c|d$"
    nfa, dfa = prepare_test(regex)
    test_string = "1"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_pipe_success_3():
    
    regex = "^aa|bb$"
    nfa, dfa = prepare_test(regex)
    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=True)
    
    test_string = "bb"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_pipe_fail_3():

    regex = "^aa|bb$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "cc"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR ASTERISK *
#
#

def test_asterisk_success_1():

    regex = "^a*$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_asterisk_fail_1():

    regex = "^a*$"
    nfa, dfa = prepare_test(regex)
    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_asterisk_success_2():

    regex = "^a*$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaaaaaaaaaaaaaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_asterisk_fail_2():

    regex = "^a*$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaaaaaaaaaaaaaaab"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_asterisk_success_3():

    regex = "^ab*$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_asterisk_fail_3():

    regex = "^ab*$"
    nfa, dfa = prepare_test(regex)
    test_string = "cb"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_asterisk_success_4():

    regex = "^ab*$"
    nfa, dfa = prepare_test(regex)
    test_string = "abbbbbbbbbbbbbbbbbbbbbbbbb"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_asterisk_fail_4():

    regex = "^ab*$"
    nfa, dfa = prepare_test(regex)
    test_string = "abbbbbbbbbbbbbbbbbbbc"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR COMBINATION OF PIPE | AND ASTERISK *
#
#

def test_combined_1_success_1():

    regex = "^a*|b*$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaaaaaaaaaaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "bbbbbbbbbb"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_combined_1_fail_1():

    regex = "^a*|b*$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "cccccccccccccc"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_combined_1_success_2():

    regex = "^abc*|ab*c|a*bc$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "ac"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "bc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abccccccccccccccc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abbbbbbbbbbbbbbbbbbbc"

    base_test(test_string, nfa, dfa, expected_result=True)
    
    test_string = "aaaaaaaaaaaaaaaaabc"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_combined_1_fail_2():

    regex = "^abc*|ab*c|a*bc$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabcccccccccccccccc"

    base_test(test_string, nfa, dfa, expected_result=False)
    
    test_string = "aabbbbbbbbbbbbbbbbc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aaaaaaaaaaaaaaaabcc"

    base_test(test_string, nfa, dfa, expected_result=False)
