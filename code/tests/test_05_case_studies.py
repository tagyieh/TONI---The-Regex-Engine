import pytest
import random

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
# TESTS FOR REGEX MATCHING A WHOLE NUMBER SUCH AS 9 OR 151
# ============================================================

def test_whole_number_success_1():

    regex = "^\\d+$"
    nfa, dfa = prepare_test(regex)
    test_string = "69"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "420"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.randint(0, 2**32-1))

    base_test(test_string, nfa, dfa, expected_result=True)

def test_whole_number_fail_1():

    regex = r"^\d+$"
    nfa, dfa = prepare_test(regex)
    test_string = "9.2"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "69.420"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = str(random.random())

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A DECIMAL NUMBER SUCH AS 3.14
# ============================================================

def test_decimal_number_success_1():

    regex = r"^\d*\.\d+$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "4.20"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "69.420"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "0.0"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.random())

    base_test(test_string, nfa, dfa, expected_result=True)

def test_decimal_number_fail_1():

    regex = r"^\d*\.\d+$"
    nfa, dfa = prepare_test(regex)

    test_string = "69"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = str(random.randint(0, 2**32-1))

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A WHOLE (9) OR DECIMAL (3.14)
# NUMBER
# ============================================================

def test_whole_and_decimal_number_success_1():

    regex = r"^\d*(\.\d+)?$"
    nfa, dfa = prepare_test(regex)

    test_string = "69"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "420"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.randint(0, 2**32-1))

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "6.9"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "4.20"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.random())

    base_test(test_string, nfa, dfa, expected_result=True)

def test_whole_and_decimal_number_fail_1():

    regex = r"^\d*(\.\d+)?$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "no_number"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "32e"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%69"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A NEGATIVE OR POSITIVE WHOLE NUMBER
# (-9, 9) OR DECIMAL (-3.14, 3.14) NUMBER
# ============================================================

def test_neg_pos_whole_and_decimal_success_1():

    regex = r"^-?\d*(\.\d+)?$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "69"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "-69"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "6.9"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "-6.9"

    base_test(test_string, nfa, dfa, expected_result=True)

# ============================================================
# TESTS FOR REGEX MATCHING A WHOLE (9), DECIMAL (3.14) OR
# FRACTION (3/4)
# ============================================================

def test_whole_decimal_fraction_success_1():

    regex = r"[-]?[0-9]+[,.]?[0-9]*([\/][0-9]+[,.]?[0-9]*)*"
    nfa, dfa = prepare_test(regex)
    
    test_string = "69"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "420"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.randint(0, 2**32-1))

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "6.9"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "4.20"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.random())

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "3/4"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "420/69"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.randint(0, 2*32-1)) + "/" + str(random.randint(0, 2*32-1))

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = str(random.random()) + "/" + str(random.random())

    base_test(test_string, nfa, dfa, expected_result=True)

# ============================================================
# TESTS FOR REGEX MATCHING A ALPHANUMERIC STRING EXCLUDING A
# SPACE
# ============================================================

def test_alphanumeric_without_space_success_1():

    regex = r"^[a-zA-Z0-9]*$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "Hello"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "123"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "456AnAlphaNumericStringWithoutSpaces123"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_alphanumeric_without_space_fail_1():

    regex = r"^[a-zA-Z0-9]*$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "Hello "

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = " Hello"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "Hel lo"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "Hello this is a sentence"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "123 hello"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A ALPHANUMERIC STRING INCLUDING A
# SPACE
# ============================================================

def test_alphanumeric_with_space_success_1():

    regex = r"^[a-zA-Z0-9 ]*$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "Hello "

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = " Hello"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "Hel lo"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "Hello this is a sentence"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "123 hello"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_alphanumeric_with_space_fail_1():

    regex = r"^[a-zA-Z0-9 ]*$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "%"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "\n"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING COMMON EMAIL IDS, MEANING THAT ONLY
# SPECIFIC CHARACTERS ARE ALLOWED, FOR EXAMPLE NO +, AND THAT
# THE TLD IS LIMITED TO 6 CHARACTERS
# ============================================================

def test_common_email_success_1():

    regex = r"^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})+$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "test@toni.se"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "test@gmail.com"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "test@thisIsALongNameWith-And8And.test.gov"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_common_email_fail_1():

    regex = r"^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})+$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "test@toni.exhaustion"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "test+notValid@gmail.com"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "test+notValid@gmail.com"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "toShortTLD@gmail.o"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "no space please@bad.com"

    base_test(test_string, nfa, dfa, expected_result=False)


# ============================================================
# TESTS FOR REGEX MATCHING AN IPV4 ADDRESS SUCH AS 192.168.1.1
# ============================================================

def test_ipv4_success_1():

    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "192.168.1.1"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "127.0.0.1"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "10.0.1.2"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "255.255.255.255"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "0.0.0.0"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_ipv4_fail_1():

    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    test_string = "192.168.1.1.1"
    nfa, dfa = prepare_test(regex)
    
    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "256.255.255.255"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "255.255.255"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "001.1.1.1"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "1.1.1.001"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "1.1. 1.001"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_ipv4_fail_2():

    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "2001:fe0c:0000:0000:0000:0000:00db:1dc0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "2001:fe0c::db:1dc0"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "2001:fe0c: :db:1dc0"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A DATE IN FORMAT YYYY-MM-dd
# ============================================================

def test_date_format_success_1():

    regex = r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"
    nfa, dfa = prepare_test(regex)
    
    test_string = "2012-08-01"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "2012-12-11"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "1965-01-01"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_date_format_fail_1():

    regex = r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"
    nfa, dfa = prepare_test(regex)
    
    test_string = "2012-08-1"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "2012-8-01"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "12-08-01"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "01-08-2012"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "01-JAN-2012"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A TIME IN THE TIME FORMAT
# HH:MM 12-hour, WITH AN OPTIONAL LEADING 0
# ============================================================

def test_time_format_1_success_1():

    regex = r"^(0?[1-9]|1[0-2]):[0-5][0-9]$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "12:00"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "08:00"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "8:00"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "8:31"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "11:51"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_time_format_1_fail_1():

    regex = r"^(0?[1-9]|1[0-2]):[0-5][0-9]$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "15:00"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "00:12"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "05:420"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = ":01"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "5:5"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A TIME IN THE TIME FORMAT
# HH:MM 12-hour, WITH AN OPTIONAL LEADING 0 AND A MANDATORY
# MERIDIEMS (AM/PM)
# ============================================================

def test_time_format_2_success_1():

    regex = r"^((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "12:00 PM"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "12:00 pm"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "11:00 AM"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "11:00 am"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "1:59 PM"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "09:00 aM"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "09:00 Am"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_time_format_2_fail_1():

    regex = r"^((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "11:00"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "09:00         pm"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A TIME IN THE TIME FORMAT
# HH:MM 24-hour, WITH A MANDATORY LEADING 0
# ============================================================

def test_time_format_3_success_1():

    regex = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "00:00"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "12:00"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "16:00"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "09:21"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "23:59"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_time_format_3_fail_1():

    regex = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "1:00"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "5:5"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "5:05"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "43:56"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = ":01"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "24:00"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING A TIME IN THE TIME FORMAT
# HH:MM:SS 24-hour, WITH A MANDATORY LEADING 0
# ============================================================

def test_time_format_4_success_1():

    regex = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "01:11:11"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "11:11:11"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "21:11:11"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "13:11:01"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "13:11:15"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "13:11:59"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "01:01:01"

    base_test(test_string, nfa, dfa, expected_result=True)


def test_time_format_4_fail_1():

    regex = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "12:00"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "1:00:59"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "5:5:59"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = ":01:01"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "23:59:"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "23:59:9"

    base_test(test_string, nfa, dfa, expected_result=False)

# TESTS FOR REGEX MATCHING UNCOMMON EMAIL IDS, MEANING THAT
# + IS ALLOWED AND THAT THE TLD CAN BE UP TO 15 CHARACTERS
# LONG
# ============================================================

def test_uncommon_email_success_1():

    regex = r"^([a-z0-9_\.\+-]+)@([\da-z\.-]+).([a-z\.]{2,15})$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "plus+is+now+possible@gmail.com"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "long+tld-now@gmail.loooooooooong"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "long+tld-now@gma1l.loooooooooong"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_uncommon_email_fail_1():

    regex = r"^([a-z0-9_\.\+-]+)@([\da-z\.-]+).([a-z\.]{2,15})$"
    nfa, dfa = prepare_test(regex)
    
    test_string = "test@site.CoM"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "test@aloltesthaha.cOm"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING AN IPV6 ADDRESS SUCH AS
# 2001:0db8:0000:0000:0000:0000:1428:07ab
# ============================================================

def test_ipv6_success_1():

    regex = r"(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{,4}){,4}%[0-9a-zA-Z]+|::(ffff(:0{1,4}){,1}:){,1}((25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9]))"
    nfa, dfa = prepare_test(regex)
    
    test_string = "1200:0000:AB00:1234:0000:2552:7777:1313"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "21DA:D3:0:2F3B:2AA:FF:FE28:9C5A"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "2001:0db8:0000:0000:0000:0000:1428:07ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "2001:0db8:0000:0000:0000::1428:07ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "2001:0db8:0:0:0:0:1428:07ab"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "2001:0db8::1428:07ab"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_ipv6_fail_1():

    regex = r"(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{,4}){,4}%[0-9a-zA-Z]+|::(ffff(:0{1,4}){,1}:){,1}((25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9]))"
    nfa, dfa = prepare_test(regex)
    
    test_string = "192.168.1.1"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "255.255.255.255"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "255.255.255"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "001.1.1.1"

    base_test(test_string, nfa, dfa, expected_result=False)

def test_ipv6_fail_2():

    regex = r"(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{,4}){,4}%[0-9a-zA-Z]+|::(ffff(:0{1,4}){,1}:){,1}((25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{,1}[0-9]){,1}[0-9]))"
    nfa, dfa = prepare_test(regex)
    
    test_string = "21DA:D3:0:2F3B:2AA:FK:FE28:9SAQ"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "21DA:D3:0:2F3B:2AA:FF.FE28.91A2"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "21DA:D3:0:2F3B:2AA:FF: ABC1:91A2"

    base_test(test_string, nfa, dfa, expected_result=False)

# ============================================================
# TESTS FOR REGEX MATCHING AN URL
# ============================================================

def test_url_success_1():

    regex = r"(https?://)?(www\.)[\-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([\-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    nfa, dfa = prepare_test(regex)
    
    test_string = "https://www.google.se"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "http://www.google.se"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "www.google.se"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "https://www.google.pt"

    base_test(test_string, nfa, dfa, expected_result=True)
    
    test_string = "www.google.looong"

    base_test(test_string, nfa, dfa, expected_result=True)
    
    test_string = "www.aweirdurl-8+#.se"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "www." + "a" * 256 + ".se"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "http://www.example.com/wpstyle/?p=364"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "https://www.training.dfirdiva.com/listing-category/digital-forensics"

    base_test(test_string, nfa, dfa, expected_result=True)

    test_string = "https://www.docs.astral.sh/ruff/rules/blind-except/"

    base_test(test_string, nfa, dfa, expected_result=True)

def test_url_fail_1():

    regex = r"(https?://)?(www\.)[\-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([\-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    nfa, dfa = prepare_test(regex)
    
    test_string = "http://142.42.1.1:8080/"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "http://-error-.invalid/"

    base_test(test_string, nfa, dfa, expected_result=False)

    test_string = "http://3628126748.se"

    base_test(test_string, nfa, dfa, expected_result=False)
