from bin.evaluator import evaluator
from bin.converter import converter
from bin.compiler import toniParserVisitor

import time
import sys
import re

###############################################################################
#                                                                             #
# This file demonstrates how finditer is vulnerable in our NFA engine, but    #
# secure for the DFA. Below, you will find 3 tests for each engine. Two       #
# "sanity" checks and one actual check for the PoC malicious input. For       #
# demonstration purposes, the third test for the finditer in the NFA is       #
# commented, as it causes a ReDoS. However, one can uncomment it to check     #
# that it actually causes such an attack.                                     #
#                                                                             #
###############################################################################

#----------------------- NFA -----------------------
string = " abc def"
regex = "\w+"

# Should return "2" (simply the amount of matches, we don't really care about anything else)
compiler = toniParserVisitor.toniParserVisitor()
nfa = compiler.compile(regex)
print("Result A:",evaluator.finditer_NFA(nfa,string))


# Test again, check if it "truly" works
string = " abc def ghi"
print("Result B:",evaluator.finditer_NFA(nfa,string)) # should return "3"

# Now, let's see if we can DoS ourselves
# We had to remove the "?:" in front of "(" because it meant a non-capture group
# and also escape the ^ as to not match an actual start of string symbol (see grammar)
SPECIAL_CHARS = re.escape(b'()<>@,;:\\"/[]?={} \t')
QUOTED_STR = br'"(\\.|[^"])*"'
VALUE_STR = br'([^' + SPECIAL_CHARS + br']+|' + QUOTED_STR + br')'
OPTION_RE_STR = (
    br'(;|\^)\s*([^' + SPECIAL_CHARS + br']+)\s*=\s*(' + VALUE_STR + br')'
)
string = b'application/x-www-form-urlencoded; !=\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'

nfa = compiler.compile(OPTION_RE_STR.decode())

#!!!!!!!!!!!!!!!!!! UNCOMMENT THIS LINE FOR A REDOS DEMO !!!!!!!!!!!!!!!!
#print("Result C:",evaluator.finditer_NFA(nfa,string)) # should return "3"


#----------------------- DFA -----------------------
print("Now for the dfa")
string = " abc abc"
regex = "a.c"

# Should return "2" (simply the amount of matches, we don't really care about anything else)
compiler = toniParserVisitor.toniParserVisitor()
nfa = compiler.compile(regex)
dfa = converter.convert_nfa_to_dfa(nfa)
print("Result A for DFA:",evaluator.finditer_DFA(dfa,string))


# Test again, check if it "truly" works
string = " abc def abc ghi abc"
print("Result B for DFA:",evaluator.finditer_DFA(dfa,string)) # should return "3"

# Now, let's see if we can no longer DoS ourselves
SPECIAL_CHARS = re.escape(b'()<>@,;:\\"/[]?={} \t')
QUOTED_STR = br'"(\\.|[^"])*"'
VALUE_STR = br'([^' + SPECIAL_CHARS + br']+|' + QUOTED_STR + br')'
OPTION_RE_STR = (
    br'(;|\^)\s*([^' + SPECIAL_CHARS + br']+)\s*=\s*(' + VALUE_STR + br')'
)
string = b'application/x-www-form-urlencoded; !=\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'

nfa = compiler.compile(OPTION_RE_STR.decode())
dfa = converter.convert_nfa_to_dfa(nfa)
print("Result C for the DFA:",evaluator.finditer_DFA(dfa,string)) # should return "3"

