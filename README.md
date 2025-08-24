# Toni The Regex Engine (TTRE)

## Overview

TTRE is a simple regex engine which enables the user to convert a regex to an NFA or DFA, which can then be used to evaluate an input string. By having the ability to convert a regex to a DFA Toni prevents exponential ReDoS.

## Features

- Convert a regex to an NFA.
- Convert a regex to a DFA.
- Evaluate an input using the NFA or DFA (equivalent to `re.match()`).
- Find all matches in an input using the NFA or DFA (equivalent to `re.finditer()`).

## Setup

1. Clone the repository.
2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

1. Define a regex:

```python
    regex = "a|b"
```
2. Compile the regex to an NFA:
```python
    compiler = toniParserVisitor.toniParserVisitor()
    nfa = compiler.compile(regex)
```
3. (Optionally) Compile NFA to a DFA:
```python
    dfa = converter.convert_nfa_to_dfa(nfa)
```
4. Evaluate an input using the NFA or DFA:
```python
    string = "a"

    if evaluator.traverse_NFA(nfa,string):
        print("Success!")
    if evaluator.traverse_DFA(dfa,string):
        print("Success!")
```

## Testing

If you change the engine and you want to test if it still works as intended you can just go into `/langsec-p4-25/project` and simply run:

```sh
pytest
```

## Contributing

Feel free to contribute. Please open up an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
