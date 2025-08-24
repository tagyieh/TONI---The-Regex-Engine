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
# TESTS FOR CHARACTER CLASSES [ac-d]
# ============================================================

def test_character_class_success_1():

    regex = "^[ac-e]$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "d"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_character_class_fail_1():

    regex = "^[ac-e]$"
    nfa, dfa = prepare_test(regex)
    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_character_class_success_2():

    regex = "^[a-d0-8]$"
    nfa, dfa = prepare_test(regex)
    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "5"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_character_class_fail_2():

    regex = "^[a-d0-8]$"
    nfa, dfa = prepare_test(regex)
    test_string = "z"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "9"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR NEGATED CHARACTER CLASSES [ac-d]
# ============================================================

def test_negated_character_class_success_1():

    regex = "^[^ac-e]$"
    nfa, dfa = prepare_test(regex)
    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "z"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_negated_character_class_fail_1():

    regex = "^[^ac-e]$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "c"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "d"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_negated_character_class_success_2():

    regex = "^[^a-d0-8]$"
    nfa, dfa = prepare_test(regex)
    test_string = "e"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "9"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_negated_character_class_fail_2():

    regex = "^[^a-d0-8]$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "b"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "2"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR ONE DIGIT \d
# ============================================================

def test_one_digit_success_1():

    regex = "^\\d$"
    nfa, dfa = prepare_test(regex)
    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "9"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_one_digit_fail_1():

    regex = "^\\d$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "*"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "-"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_one_digit_fail_2():

    regex = "^\\d$"
    nfa, dfa = prepare_test(regex)
    test_string = "10"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "111"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR ONE NON DIGIT \D
# ============================================================

def test_one_non_digit_success_1():

    regex = "^\\D$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "*"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "-"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_one_non_digit_fail_1():

    regex = "^\\D$"
    nfa, dfa = prepare_test(regex)
    test_string = "1"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "9"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_one_non_digit_fail_2():

    regex = "^\\D$"
    nfa, dfa = prepare_test(regex)
    test_string = "10"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "111"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR ONE WHITESPACE \s
# ============================================================

def test_one_whitespace_success_1():

    regex = r"^\s$"
    nfa, dfa = prepare_test(regex)
    test_string = " "

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "\t"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "\r"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_one_whitespace_fail_1():

    regex = r"^\s$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = ")"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_one_whitespace_fail_2():

    regex = r"^\s$"
    nfa, dfa = prepare_test(regex)
    test_string = "  "

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\t\t"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n\n"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\r\r"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR ONE NON WHITESPACE \S
# ============================================================

def test_one_non_whitespace_success_1():

    regex = r"^\S$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "*"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "9"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "-"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_one_non_whitespace_fail_1():

    regex = r"^\S$"
    nfa, dfa = prepare_test(regex)
    test_string = " "

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\t"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\r"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_one_non_whitespace_fail_2():

    regex = r"^\S$"
    nfa, dfa = prepare_test(regex)
    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=False)
    
    test_string = "AA"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "**"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "99"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "--"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR ONE WORD CHARACTER \w
# ============================================================

def test_one_word_character_success_1():

    regex = r"^\w$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "d"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "D"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "7"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "_"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_one_word_character_fail_1():

    regex = r"^\w$"
    nfa, dfa = prepare_test(regex)
    test_string = "$"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "."

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = " "

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "+"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_one_word_character_fail_2():

    regex = r"^\w$"
    nfa, dfa = prepare_test(regex)
    test_string = "aa"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "dd"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "AA"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "DD"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "01"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "__"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR ONE NON WORD CHARACTER \W
# ============================================================

def test_one_non_word_character_success_1():

    regex = r"^\W$"
    nfa, dfa = prepare_test(regex)
    test_string = "$"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "."

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = " "

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "+"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_one_non_word_character_fail_1():

    regex = r"^\W$"
    nfa, dfa = prepare_test(regex)
    test_string = "a"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "d"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "A"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "D"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "7"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "_"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_one_non_word_character_fail_2():

    regex = r"^\W$"
    nfa, dfa = prepare_test(regex)
    test_string = "$$"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = ".."

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "  "

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n\n"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "++"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR WILDCARD CHARACTER .
# - Matches any character except newline \n
# ============================================================

def test_wildcard_character_success_1():

    regex = "^.$"
    nfa, dfa = prepare_test(regex)
    test_string = ""

    for i in range(256):

        if i == ord("\n"):
            continue       

        test_string = chr(i)

        base_test(test_string, nfa, dfa, expected_result=True)

def test_wildcard_character_fail_1():

    regex = "^.$"
    nfa, dfa = prepare_test(regex)
    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_wildcard_character_fail_2():

    regex = "^.$"
    nfa, dfa = prepare_test(regex)
    test_string = ""

    for i in range(256):

        test_string = chr(i) * 2

        base_test(test_string, nfa, dfa, expected_result=False)
