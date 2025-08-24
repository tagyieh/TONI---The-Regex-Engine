from bin.evaluator import evaluator
from bin.converter import converter
from bin.compiler import toniParserVisitor

import time
import sys
import re

def main():

    SPECIAL_CHARS = re.escape(b'()<>@,;:\\"/[]?={} \t')
    QUOTED_STR = br'"(\\.|[^"])*"'
    VALUE_STR = br'([^' + SPECIAL_CHARS + br']+|' + QUOTED_STR + br')'
    OPTION_RE_STR = (
        br'(;|\^)\s*([^' + SPECIAL_CHARS + br']+)\s*=\s*(' + VALUE_STR + br')'
    )
    string = b'application/x-www-form-urlencoded; !=\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'

    '''
    print("Starting re")
    for _ in re.finditer(OPTION_RE_STR, string):
        print("re happening!")
    print("Ending re")
    '''

    compiler = toniParserVisitor.toniParserVisitor()
    nfa = compiler.compile(OPTION_RE_STR.decode())
    dfa = converter.convert_nfa_to_dfa(nfa)
    
    print("Starting TONI")
    for _ in evaluator.finditer_DFA(dfa,string):
        print("TONI happening")
    print("Ending TONI")

main()
