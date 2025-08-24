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

# ============================================================
# TESTS FOR NEWLINE CHARACTER \n
# ============================================================

def test_newline_success_1():

    regex = "^\n$"
    nfa, dfa = prepare_test(regex)
    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_newline_fail_1():

    regex = "^\n$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\t"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_newline_fail_2():

    regex = "^\n$"
    nfa, dfa = prepare_test(regex)
    test_string = "\n\n"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR CARRIAGE RETURN \r
# ============================================================

def test_carriage_return_success_1():

    regex = "^\r$"
    nfa, dfa = prepare_test(regex)
    test_string = "\r"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_carriage_return_fail_1():

    regex = "^\r$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_carriage_return_fail_2():

    regex = "^\r$"
    nfa, dfa = prepare_test(regex)
    test_string = "\r\r"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR TAB \t
# ============================================================

def test_tab_success_1():

    regex = "^\t$"
    nfa, dfa = prepare_test(regex)
    test_string = "\t"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_tab_fail_1():

    regex = "^\t$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\r"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_tab_fail_2():

    regex = "^\t$"
    nfa, dfa = prepare_test(regex)
    test_string = "\t\t"

    base_test(test_string, nfa, dfa, expected_result=False)

