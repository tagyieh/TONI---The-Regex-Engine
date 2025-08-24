from bin.evaluator import evaluator
from bin.converter import converter
from bin.compiler import toniParserVisitor

import time
import sys
import re

def main():

    # Initialize this variable to whatever regex you want to test
    regex = None
    # Initialize this variable the string you want to test against the regex
    string = None

    # Compile
    compiler = toniParserVisitor.toniParserVisitor()
    nfa = compiler.compile(regex)
    dfa = converter.convert_nfa_to_dfa(nfa)

    start = time.time()
    # Traverse using NFA
    evaluator.traverse_NFA(nfa,string)
    print("NFA took ", time.time()-start)

    start = time.time()
    # Traverse using DFA
    evaluator.traverse_DFA(dfa,string)
    print("DFA took ", time.time()-start)

if __name__ == "__main__":
    main()
