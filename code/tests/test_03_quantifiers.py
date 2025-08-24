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
# TESTS FOR PLUS +
#
#

def test_plus_success_1():

    regex = "^a+$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_plus_fail_1():

    regex = "^a+b$"
    nfa, dfa = prepare_test(regex)
    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_plus_success_2():

    regex = "^a+b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_plus_success_3():

    regex = "^a+b+c$"
    nfa, dfa = prepare_test(regex)
    test_string = "abc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaabbbbbbbc"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_plus_fail_3():

    regex = "^a+b+c$"
    nfa, dfa = prepare_test(regex)
    test_string = "bc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "ac"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR QUESTIOMARK ?
#
#

def test_questionmark_success_1():

    regex = "^a?b$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_questionmark_fail_1():

    regex = "^a?b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_questionmark_success_2():

    regex = "^a?b?c$"
    nfa, dfa = prepare_test(regex)
    test_string = "abc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "ac"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "bc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_questionmark_fail_2():

    regex = "^a?b?c$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabc"

    base_test(test_string, nfa, dfa, expected_result=False)
    
    test_string = "abbc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aac"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "bbc"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR RANGE {a,b}
#
#

def test_range_success_1():

    regex = "^a{2,5}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_range_fail_1():

    regex = "^a{2,5}$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "a" * 6

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "a" * 15

    base_test(test_string, nfa, dfa, expected_result=False)

def test_range_success_2():

    regex = "^a{2,5}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_range_fail_2():

    regex = "^a{2,5}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "a" * 6 + "b"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "a" * 15 + "b"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_range_success_3():

    regex = "^a{2,5}b{1,3}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aabb"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aabbb"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_range_success_4():

    regex = "^a{2,5}b{1,3}c$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aabbbc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaabbbc"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_range_fail_4():

    regex = "^a{2,5}b{1,3}c$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabcc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR MIN {a,}
#
#

def test_min_success_1():

    regex = "^a{2,}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_min_fail_1():

    regex = "^a{2,}$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_min_success_2():

    regex = "^a{2,}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaaaaaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_min_fail_2():

    regex = "^a{2,}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_min_success_3():

    regex = "^a{2,}b{3,}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabbb"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbb"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_min_fail_3():

    regex = "^a{2,}b{3,}$"
    nfa, dfa = prepare_test(regex)
    test_string = "abbb"

    base_test(test_string, nfa, dfa, expected_result=False)
    
    test_string = "aabb"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "bbb"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_min_success_4():

    regex = "^a{2,}b{3,}c$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabbbc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbc"

    base_test(test_string, nfa, dfa, expected_result=True)

#
#
# TESTS FOR MAX {,a}
#
#

def test_max_success_1():

    regex = "^a{,3}$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaa"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_max_fail_1():

    regex = "^a{,3}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaaa"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_max_success_2():

    regex = "^a{,3}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_max_fail_2():

    regex = "^a{,3}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaaab"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_max_success_3():

    regex = "^a{,3}bc{,2}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaabcc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "bcc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_max_fail_3():

    regex = "^a{,3}bc{,2}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaaabcc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aabccc"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR EXACT {a}
#
#

def test_exact_success_1():

    regex = "^a{3}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaa"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_exact_fail_1():

    regex = "^a{3}$"
    nfa, dfa = prepare_test(regex)
    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aaaa"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_exact_success_2():

    regex = "^a{3}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_exact_fail_2():

    regex = "^a{3}b$"
    nfa, dfa = prepare_test(regex)
    test_string = "aab"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aaaab"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_exact_success_3():

    regex = "^a{3}b{2}c$"
    nfa, dfa = prepare_test(regex)
    test_string = "aaabbc"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_exact_fail_3():

    regex = "^a{3}b{2}c$"
    nfa, dfa = prepare_test(regex)
    test_string = "aabbc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aaabc"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR COMBINATION OF PLUS + AND QUESTIONMARK ?
#
#

def test_combined_1_success_1():

    regex = "^a+b?$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaaaa"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_combined_1_fail_1():

    regex = "^a+b?$"
    nfa, dfa = prepare_test(regex)
    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "abb"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_combined_1_success_2():

    regex = "^a+b+c?$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abc"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaabbbbbbbbbbbc"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_combined_1_fail_2():

    regex = "^a+b+c?$"
    nfa, dfa = prepare_test(regex)
    test_string = "bc"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "ac"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "abcc"

    base_test(test_string, nfa, dfa, expected_result=False)

#
#
# TESTS FOR COMBINATION OF PLUS + AND EXACT {a}
#
#

def test_combined_2_success_1():

    regex = "^a+b{1}$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_combined_2_success_2():

    regex = "^a+b{1}c{1}d+$"
    nfa, dfa = prepare_test(regex)
    test_string = "abcd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaabcd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abcdddddddddddddddd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaabcdddddddddddddddd"

    base_test(test_string, nfa, dfa, expected_result=True)

#
#
# TESTS FOR COMBINATION OF PLUS + AND RANGE {a,b}
#
#

def test_combined_3_success_1():

    regex = "^a+b{1,3}$"
    nfa, dfa = prepare_test(regex)
    test_string = "ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abb"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abbb"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaaaaaaabbb"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_combined_3_success_2():

    regex = "^a+b{1,3}c+d{1,2}$"
    nfa, dfa = prepare_test(regex)
    test_string = "abcd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abbcd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abbbcd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abbbcdd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaaaaaaaaaaabcd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "abccccccccccccccccccccccccd"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "aaaaaaaaaaaaaaabcccccccccccccccccccccd"

    base_test(test_string, nfa, dfa, expected_result=True)
