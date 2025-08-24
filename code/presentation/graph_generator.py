from bin.evaluator import evaluator
from bin.converter import converter
from bin.compiler import toniParserVisitor

import time
import sys
import re
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**6)

def main():

    regex = "(a+)+$"

    # generate graph for re
    x = []
    y = []
    for i in range(1,31):
        print(i)
        cur_x = i
        time_start = time.time()
        re.match(regex,i * "a" + "!")
        cur_y = time.time() - time_start
        x.append(cur_x)
        y.append(cur_y)
    print("done")

    plt.plot(x,y, color='blue', label='re')
    plt.xlabel("String length")
    plt.ylabel("Time taken (s)")
    plt.title("Running time comparision with classic ReDoS example - (a+)+$")
    plt.savefig("classic_redos_re.png")
    
    compiler = toniParserVisitor.toniParserVisitor()
    nfa = compiler.compile(regex)
    dfa = converter.convert_nfa_to_dfa(nfa)

    x = []
    y = []

    for i in range(1,31):
        print(i)
        cur_x = i
        time_start = time.time()
        evaluator.traverse_DFA(dfa, i * "a" + "!")
        # re.match(regex,i * "a" + "!")
        cur_y = time.time() - time_start
        x.append(cur_x)
        y.append(cur_y)
    # should return "2" (simply the amount of matches, we don't really care about anything else)
    #compiler = toniParserVisitor.toniParserVisitor()
    #nfa = compiler.compile(regex)
    #print("Sanity check:",evaluator.traverse_NFA(nfa,string))

    plt.plot(x,y, color="orange", label="TONI")
    plt.xlabel("String length")
    plt.ylabel("Time taken (s)")
    plt.legend()
    plt.savefig("classic_redos_comparision")

    plt.clf()

    string = b'application/x-www-form-urlencoded; !=\"'

    SPECIAL_CHARS = re.escape(b'()<>@,;:\\"/[]?={} \t')
    QUOTED_STR = br'"(\\.|[^"])*"'
    VALUE_STR = br'([^' + SPECIAL_CHARS + br']+|' + QUOTED_STR + br')'
    OPTION_RE_STR = (
        br'(;|\^)\s*([^' + SPECIAL_CHARS + br']+)\s*=\s*(' + VALUE_STR + br')'
    )

    x = []
    y = []
    for i in range(1,45):
        print(i)
        cur_x = i
        time_start = time.time()
        for match in re.finditer(OPTION_RE_STR.decode(),(string + i * b"\\").decode()):
            pass
        cur_y = time.time() - time_start
        x.append(cur_x)
        y.append(cur_y)
    print("done")

    plt.plot(x,y, color="blue", label="re")
    plt.xlabel("String length")
    plt.ylabel("Time taken (s)")
    plt.title("Running time comparision for CVE-2024-24762")
    plt.savefig("redos_cve-2024-24762_re.png")
    
    compiler = toniParserVisitor.toniParserVisitor()
    nfa = compiler.compile(OPTION_RE_STR.decode())
    dfa = converter.convert_nfa_to_dfa(nfa)

    x = []
    y = []

    for i in range(1,45):
        print(i)
        cur_x = i
        time_start = time.time()
        evaluator.finditer_DFA(dfa,(string + i * b"\\").decode())
        # re.match(regex,i * "a" + "!")
        cur_y = time.time() - time_start
        x.append(cur_x)
        y.append(cur_y)

    plt.plot(x,y, color="orange", label="TONI")
    plt.xlabel("String length")
    plt.ylabel("Time taken (s)")
    plt.legend()
    plt.savefig("redos_cve-2024-24762_comparision.png")    

    plt.clf()

    regex = r"(\d+)x(\d+)(-anim)?.(\w+)"

    iterations = 2500000

    # generate graph for re
    x = []
    y = []
    for i in range(1,iterations,1000):
        print(i)
        cur_x = i
        time_start = time.time()
        re.match(regex,i * "0" + "A")
        cur_y = time.time() - time_start
        x.append(cur_x)
        y.append(cur_y)
    print("done")

    plt.plot(x,y, color='blue', label='re')
    plt.xlabel("String length")
    plt.ylabel("Time taken (s)")
    plt.title("Running time comparision with polynomial ReDoS example")
    plt.savefig("plot.png")
    
    compiler = toniParserVisitor.toniParserVisitor()
    nfa = compiler.compile(regex)
    dfa = converter.convert_nfa_to_dfa(nfa)

    x = []
    y = []

    for i in range(1,iterations,10000):
        print(i)
        cur_x = i
        time_start = time.time()
        evaluator.traverse_DFA(dfa, i * "0" + "A")
        # re.match(regex,i * "a" + "!")
        cur_y = time.time() - time_start
        x.append(cur_x)
        y.append(cur_y)
    # should return "2" (simply the amount of matches, we don't really care about anything else)
    #compiler = toniParserVisitor.toniParserVisitor()
    #nfa = compiler.compile(regex)
    #print("Sanity check:",evaluator.traverse_NFA(nfa,string))

    plt.plot(x,y, color="orange", label="TONI")
    plt.xlabel("String length")
    plt.ylabel("Time taken (s)")
    plt.legend()
    plt.savefig("plot_dfa.png")

main()
